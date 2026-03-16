# Intermediate Code Optimizer (ICO) - PRD

## Vision
A futuristic, professional developer tool for visualizing and explaining compiler optimization techniques on Intermediate Representation (IR).

## Core Requirements (College/Professional Hybrid)
- **Input:** Pseudo-IR / Three-Address Code (TAC).
- **Engine:** Python-based optimization passes (Constant Folding, CSE, DCE, etc.).
- **UI:** Streamlit-based (clean, minimalist, futuristic) for rapid deployment while showing deep technical logic.
- **Visualization:** Control Flow Graph (CFG) using NetworkX/Graphviz and step-by-step "diff" of code transformations.
- **Metrics:** Instruction count reduction and estimated complexity improvements.

## Dev Strategy
1. **Parser:** Robust regex-based TAC parser.
2. **Optimizer:** Modular "Pass" architecture.
3. **Frontend:** Streamlit with custom CSS for "Glassmorphism" / Dark Mode vibe.
4. **Sub-agents:** 
   - `ico-pm`: Documentation & PRD refinement.
   - `ico-dev-backend`: Python logic (parser, optimizer, CFG).
   - `ico-dev-frontend`: Streamlit UI & Visuals.
