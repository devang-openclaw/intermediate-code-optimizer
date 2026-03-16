import re
from typing import List, Optional, Union

class Instruction:
    """Represents a Three-Address Code (TAC) instruction."""
    def __init__(self, op: str, arg1: Optional[str] = None, arg2: Optional[str] = None, result: Optional[str] = None, label: Optional[str] = None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result
        self.label = label

    def __repr__(self):
        if self.op == 'label':
            return f"{self.result}:"
        elif self.op == 'assign':
            return f"{self.result} = {self.arg1}"
        elif self.op in ('+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!='):
            return f"{self.result} = {self.arg1} {self.op} {self.arg2}"
        elif self.op == 'goto':
            return f"goto {self.result}"
        elif self.op == 'if':
            return f"if {self.arg1} goto {self.result}"
        elif self.op == 'if_rel':
            # arg1 is condition (e.g., 'a > b'), result is label
            return f"if {self.arg1} goto {self.result}"
        return f"{self.result} = {self.op} {self.arg1} {self.arg2}"

class TACParser:
    """Parses Three-Address Code string into Instruction objects."""
    
    # regex for different patterns
    # 1. Label: L1:
    LABEL_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):$')
    # 2. Assignment: t1 = 10 or t1 = a
    ASSIGN_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*([A-Za-z0-9_]+)$')
    # 3. Binary Op: t1 = a + b
    BINOP_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*([A-Za-z0-9_]+)\s*([\+\-\*/<>!=]=?)\s*([A-Za-z0-9_]+)$')
    # 4. Goto: goto L1
    GOTO_RE = re.compile(r'^goto\s+([A-Za-z_][A-Za-z0-9_]*)$')
    # 5. If: if a > b goto L1 or if a goto L1
    IF_RE = re.compile(r'^if\s+(.*?)\s+goto\s+([A-Za-z_][A-Za-z0-9_]*)$')

    @staticmethod
    def parse_line(line: str) -> Optional[Instruction]:
        line = line.strip()
        if not line or line.startswith('#'):
            return None

        # Try Label
        match = TACParser.LABEL_RE.match(line)
        if match:
            return Instruction(op='label', result=match.group(1))

        # Try Binary Op (check this before assign to catch 'a + b' correctly)
        match = TACParser.BINOP_RE.match(line)
        if match:
            res, arg1, op, arg2 = match.groups()
            return Instruction(op=op, arg1=arg1, arg2=arg2, result=res)

        # Try Assign
        match = TACParser.ASSIGN_RE.match(line)
        if match:
            res, arg1 = match.groups()
            return Instruction(op='assign', arg1=arg1, result=res)

        # Try Goto
        match = TACParser.GOTO_RE.match(line)
        if match:
            return Instruction(op='goto', result=match.group(1))

        # Try If
        match = TACParser.IF_RE.match(line)
        if match:
            cond, label = match.groups()
            return Instruction(op='if', arg1=cond, result=label)

        return None

    @staticmethod
    def parse(text: str) -> List[Instruction]:
        instructions = []
        for line in text.splitlines():
            instr = TACParser.parse_line(line)
            if instr:
                instructions.append(instr)
        return instructions
