from backend.parser.tac_parser import TACParser
from backend.cfg.block_builder import BlockBuilder

def test_pipeline():
    code = """
    L1:
    a = 10
    b = 20
    t1 = a + b
    if t1 > 25 goto L2
    t2 = 5
    goto L3
    L2:
    t2 = 10
    L3:
    result = t2
    """
    
    print("--- Parsing ---")
    parser = TACParser()
    instructions = parser.parse(code)
    for instr in instructions:
        print(f"DEBUG: {instr.op} | {instr.arg1} | {instr.arg2} | {instr.result} -> {instr}")

    print("\n--- Building Blocks ---")
    builder = BlockBuilder()
    blocks = builder.build(instructions)
    for block in blocks:
        print(block)
        print("-" * 10)

if __name__ == "__main__":
    test_pipeline()
