import streamlit as st

from utils.genai import generate_prompt
from utils.ml_recommender import recommend_ai_ml
from st_copy_to_clipboard import st_copy_to_clipboard

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="PromptWise AI Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------

defaults = {
    "generated_prompt": "",
    "recommendations": [],
    "role": "",
    "task": "",
    "context": "",
    "constraint": "",
    "output_format": "",
    "goal": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ----------------------------------------------------------
# THEME
# ----------------------------------------------------------

st.markdown("""
<style>

.stApp{
    background:linear-gradient(
    180deg,
    #FFFFFF 0%,
    #F7F3FF 50%,
    #EEF5FF 100%);
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #ECECEC;
}

/* Buttons */

.stButton>button{

    width:100%;
    height:56px;

    border:none;

    border-radius:14px;

    color:white;

    font-weight:600;

    font-size:16px;

    background:linear-gradient(
    90deg,
    #7C4DFF,
    #9C6DFF);

}

/* Text Inputs */

.stTextInput input{

    border-radius:14px;

}

.stTextArea textarea{

    border-radius:14px;

}

/* Cards */

.card{

    background:white;

    border-radius:20px;

    padding:30px;

    border:1px solid #ECECEC;

    box-shadow:0px 10px 25px rgba(0,0,0,.05);

}

.small-title{

    color:#7C4DFF;

    font-weight:600;

    font-size:18px;

}

.big-title{

    color:#1F2937;

    font-weight:800;

    font-size:58px;

    line-height:1.2;

}

.desc{

    color:#64748B;

    font-size:18px;

    line-height:1.8;

}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------

with st.sidebar:

    st.title("🤖 PromptWise AI")

    st.caption("Prompt Engineering Platform")

    st.divider()

    page = st.radio(

        "Navigation",

        [

            "🏠 Home",

            "🧠 Prompt Builder",

            "📊 Dashboard",

            "✨ Features",

            "ℹ About"

        ]

    )

    st.divider()

    st.success("Machine Learning + Generative AI")

# ----------------------------------------------------------
# HOME
# ----------------------------------------------------------

if page == "🏠 Home":

    st.markdown(
        '<div class="small-title">WELCOME TO PROMPTWISE AI PRO</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="big-title">Create Smarter Prompts<br>Choose Smarter AI.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="desc">

Generate professional prompts using Gemini and receive intelligent
AI Assistant recommendations powered by Machine Learning.

</div>
""",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns([1,1])

    with col1:

        st.button(
            "🚀 Get Started",
            use_container_width=True
        )

    with col2:

        st.button(
            "✨ Explore Features",
            use_container_width=True
        )

    st.write("")
    st.write("")
    st.write("")

    st.markdown("## Why PromptWise AI?")

    c1, c2 = st.columns(2)

    with c1:

        st.info("""
### 🤖 AI Prompt Generation

Professional prompts using Gemini AI.

✔ Structured Prompts

✔ Context Aware

✔ Professional Quality
""")

        st.info("""
### 🧠 ML Recommendation

Random Forest recommends the best AI Assistant.

✔ TF-IDF

✔ Top 3 Recommendations

✔ Fast Prediction
""")

    with c2:

        st.info("""
### ⚡ Premium Experience

Modern interface designed for productivity.

✔ Copy Prompt

✔ Download Prompt

✔ Responsive Layout
""")

        st.info("""
### 🚀 Multiple AI Platforms

Supports:

• ChatGPT

• Gemini

• Claude

• DeepSeek

• Grok

• Copilot
""")
