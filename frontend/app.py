import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="ICO | Intermediate Code Optimizer",
    page_icon="🦾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for futuristic dark theme (Glassmorphism + Neon)
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        color: #e0e0e0;
    }

    /* Glassmorphism containers */
    div.stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: #00ffcc !important;
        font-family: 'Courier New', Courier, monospace !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 52, 96, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 255, 204, 0.2);
    }

    /* Neon Buttons */
    div.stButton > button {
        background: linear-gradient(45deg, #00d2ff 0%, #3a7bd5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.5rem 2rem !important;
        font-weight: bold !important;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.6) !important;
        transform: translateY(-2px);
    }

    /* Headers and Titles */
    h1, h2, h3 {
        color: #00ffcc !important;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }

    /* Metrics highlight */
    [data-testid="stMetricValue"] {
        color: #00ffcc !important;
    }
    
    /* Tables/Diff highlight */
    .diff-added { color: #00ffcc; background-color: rgba(0, 255, 204, 0.1); }
    .diff-removed { color: #ff4b4b; background-color: rgba(255, 75, 75, 0.1); }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    st.subheader("Optimization Passes")
    fold = st.checkbox("Constant Folding", value=True)
    cse = st.checkbox("Common Subexpression Elimination", value=True)
    dce = st.checkbox("Dead Code Elimination", value=True)
    prop = st.checkbox("Copy Propagation", value=True)
    
    st.divider()
    st.subheader("Visuals")
    show_cfg = st.toggle("Generate CFG", value=True)
    theme_intensity = st.slider("Neon Intensity", 0, 100, 50)

# Main UI
st.title("🦾 Intermediate Code Optimizer")
st.markdown("### *Futuristic IR Optimization Engine*")

# Layout columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Input IR")
    default_ir = """L1:
  t1 = 10 + 5
  t2 = t1 * 2
  t3 = 10 + 5
  t4 = t3 * 2
  if t4 > 20 goto L2
  goto L3
L2:
  print t2
L3:
  exit"""
    ir_input = st.text_area("Enter Three-Address Code (TAC):", value=default_ir, height=300)
    
    if st.button("🚀 Run Optimization"):
        st.session_state['optimized'] = True
    else:
        st.session_state['optimized'] = False

# Results Section
if st.session_state.get('optimized'):
    with col2:
        st.subheader("📤 Optimized Output")
        mock_optimized = """L1:
  t1 = 15
  t2 = 30
  if 30 > 20 goto L2
  goto L3
L2:
  print 30
L3:
  exit"""
        st.text_area("Optimized TAC:", value=mock_optimized, height=300, disabled=True)

    st.divider()
    
    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Instructions", "11", "-4")
    m2.metric("Execution Cycles (est)", "45", "-12")
    m3.metric("Passes Applied", "3", "Constant Folding, DCE")

    # Optimization Diff (Mock)
    st.subheader("🔍 Transformation Diff")
    diff_data = [
        {"Line": 1, "Original": "t1 = 10 + 5", "Optimized": "t1 = 15", "Action": "Constant Folding"},
        {"Line": 3, "Original": "t3 = 10 + 5", "Optimized": "-", "Action": "CSE / Removed"},
        {"Line": 4, "Original": "t4 = t3 * 2", "Optimized": "-", "Action": "DCE / Propagated"},
    ]
    st.table(pd.DataFrame(diff_data))

    if show_cfg:
        st.subheader("🕸️ Control Flow Graph (Preview)")
        st.info("CFG Generation active. (Interactive graph will render here using Graphviz/NetworkX)")
        # Placeholder for graph
        st.image("https://via.placeholder.com/800x400.png?text=CFG+Visualization+Mockup+-+Neon+Nodes", use_container_width=True)

else:
    with col2:
        st.info("👈 Enter IR and click 'Run Optimization' to see the transformation.")
        st.image("https://via.placeholder.com/600x300.png?text=Optimization+Visualizer+Ready", use_container_width=True)
