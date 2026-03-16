from typing import List, Set
from backend.parser.tac_parser import Instruction

class BasicBlock:
    """A sequence of instructions with one entry and one exit."""
    def __init__(self, id: int, instructions: List[Instruction] = None):
        self.id = id
        self.instructions = instructions or []
        self.predecessors: Set['BasicBlock'] = set()
        self.successors: Set['BasicBlock'] = set()

    def __repr__(self):
        instr_str = "\n  ".join([str(i) for i in self.instructions])
        return f"Block {self.id}:\n  {instr_str}"

class BlockBuilder:
    """Groups TAC instructions into basic blocks."""
    
    @staticmethod
    def build(instructions: List[Instruction]) -> List[BasicBlock]:
        if not instructions:
            return []

        # 1. Identify leaders
        # - First instruction
        # - Target of any jump (goto/if)
        # - Instruction immediately following a jump
        
        leaders = {0} # Index of first instruction
        for i, instr in enumerate(instructions):
            if instr.op in ('goto', 'if'):
                # Successor of jump is a leader
                if i + 1 < len(instructions):
                    leaders.add(i + 1)
                
                # Target of jump is a leader
                target_label = instr.result
                for j, target_instr in enumerate(instructions):
                    if target_instr.op == 'label' and target_instr.result == target_label:
                        leaders.add(j)
                        break
        
        sorted_leaders = sorted(list(leaders))
        blocks = []
        for i in range(len(sorted_leaders)):
            start = sorted_leaders[i]
            end = sorted_leaders[i+1] if i+1 < len(sorted_leaders) else len(instructions)
            block_instrs = instructions[start:end]
            blocks.append(BasicBlock(id=i, instructions=block_instrs))
            
        return blocks
