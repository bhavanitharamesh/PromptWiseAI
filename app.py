import streamlit as st
from utils.genai import generate_prompt
from utils.genai import recommend_ai
from st_copy_to_clipboard import st_copy_to_clipboard

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="PromptWise AI Pro",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------------------
# LOAD CSS
# ----------------------------------------------------

def load_css():
    with open("assets/styles.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ----------------------------------------------------
# NAVBAR
# ----------------------------------------------------

st.markdown("""
<div style="
background:white;
padding:18px 35px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.06);
margin-bottom:35px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<h2 style="margin:0;color:#111827;">
🤖 PromptWise <span style="color:#6D4AFF;">AI Pro</span>
</h2>

<div style="
display:flex;
gap:35px;
font-size:16px;
font-weight:600;
color:#6B7280;
">

<span>🏠 Home</span>

<span>✨ Prompt Builder</span>

<span>🤖 AI Advisor</span>

<span>📞 Contact</span>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HERO SECTION
# ----------------------------------------------------

left, right = st.columns([1.3,1])

with left:

    st.markdown("""
    <div class="badge">
    ✨ AI Powered Prompt Engineering Platform
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-title">
    Build Better Prompts with<br>
    <span>PromptWise AI Pro</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-subtitle">

    Transform your simple ideas into rich,
    professional AI prompts using

    <br><br>

    ✔ Generative AI

    <br>

    ✔ Prompt Engineering

    <br>

    ✔ Natural Language Processing

    <br>

    ✔ Machine Learning

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="display:flex;gap:15px;margin-top:25px;">

<div style="
background:#6D4AFF;
color:white;
padding:14px 24px;
border-radius:12px;
font-weight:700;
display:inline-block;
">
🚀 AI Powered
</div>

<div style="
background:white;
color:#6D4AFF;
border:2px solid #6D4AFF;
padding:14px 24px;
border-radius:12px;
font-weight:700;
display:inline-block;
">
⚡ Gemini Enabled
</div>

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""

<div class="card" style="text-align:center;">

<h1 style="font-size:90px;">🤖</h1>

<h2>Prompt Engineering Engine</h2>

<p style="color:#6B7280;">

Powered by Gemini AI

</p>

<hr>

<div style="text-align:left;line-height:2;">

✅ Professional Prompt Generation

<br>

✅ Dynamic AI Recommendation

<br>

✅ Streamlit Community Cloud Ready

<br>

✅ Modern AI Workspace

</div>

</div>

""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ----------------------------------------------------
# PROMPT BUILDER
# ----------------------------------------------------

st.markdown("""
<div class="card">

<div class="section-title">

✨ Prompt Builder

</div>

<p style="color:#6B7280;margin-bottom:20px;">
Describe your requirement and let PromptWise AI engineer a professional prompt.
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    role = st.text_input(
        "🤖 AI Role",
        placeholder="Example: Machine Learning Engineer"
    )

    task = st.text_input(
        "📋 Task",
        placeholder="Example: Build a Customer Churn Prediction Model"
    )

    goal = st.text_input(
        "🎯 Goal",
        placeholder="Example: Build an interview-ready project"
    )

with right:

    context = st.text_area(
        "🧠 Context",
        placeholder="Describe your project, scenario or problem in detail...",
        height=180
    )

    constraint = st.text_input(
        "⚙ Constraints",
        placeholder="Example: Beginner friendly, step-by-step explanation."
    )

    output_format = st.text_input(
        "📄 Output Format",
        placeholder="Example: Markdown Report"
    )

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:

    

st.markdown("<br><br>", unsafe_allow_html=True)

# ----------------------------------------------------
# GENERATE PROMPT
# ----------------------------------------------------

if generate:

    with st.spinner("🧠 Generating your professional prompt..."):

        try:

            prompt = generate_prompt(
                role=role,
                task=task,
                context=context,
                constraint=constraint,
                output_format=output_format,
                goal=goal
            )

            # Save everything for later
            st.session_state.generated_prompt = prompt
            st.session_state.role = role
            st.session_state.task = task
            st.session_state.context = context
            st.session_state.constraint = constraint
            st.session_state.output_format = output_format
            st.session_state.goal = goal

        except Exception as e:

            st.error(f"❌ Prompt Generation Error:\n\n{e}")
            st.stop()


# ----------------------------------------------------
# DISPLAY GENERATED PROMPT
# ----------------------------------------------------

if "generated_prompt" in st.session_state:

    st.success("✅ Prompt Generated Successfully")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
        📝 Generated Professional Prompt
    </div>
    """, unsafe_allow_html=True)

    st.text_area(
        "",
        value=st.session_state.generated_prompt,
        height=350,
        disabled=True
    )

    st_copy_to_clipboard(
        st.session_state.generated_prompt,
        "📋 Copy Prompt"
    )

    st.download_button(
        "📥 Download Prompt",
        st.session_state.generated_prompt,
        file_name="generated_prompt.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    recommend_ai_button = st.button(
        "🤖 Recommend Best AI Assistants",
        use_container_width=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st_copy_to_clipboard(
            prompt,
            "📋 Copy Prompt"
        )

    with c2:

        st.download_button(
            label="📄 Download TXT",
            data=prompt,
            file_name="PromptWise_Prompt.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_txt"
        )

    with c3:

        st.download_button(
            label="📑 Download Markdown",
            data=prompt,
            file_name="PromptWise_Prompt.md",
            mime="text/markdown",
            use_container_width=True,
            key="download_md"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

# ----------------------------------------------------
# AI RECOMMENDATIONS
# ----------------------------------------------------

# ----------------------------------------------------
# AI RECOMMENDATIONS
# ----------------------------------------------------

if recommend_ai_button:

    with st.spinner("🤖 Finding the best AI assistants for your task..."):

        try:

            recommendations = recommend_ai(
                role=st.session_state.role,
                task=st.session_state.task,
                context=st.session_state.context,
                constraint=st.session_state.constraint,
                output_format=st.session_state.output_format,
                goal=st.session_state.goal
            )

        except Exception as e:

            st.error(f"❌ Recommendation Error:\n\n{e}")
            st.stop()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
        🏆 Top AI Assistant Recommendations
    </div>

    <p style="color:#6B7280;margin-bottom:20px;">
        Based on your requirements, Gemini recommends these AI assistants.
    </p>
    """, unsafe_allow_html=True)

    medals = ["🥇", "🥈", "🥉"]

    if isinstance(recommendations, list):

        for i, ai in enumerate(recommendations):

            medal = medals[i] if i < 3 else "⭐"

            name = ai.get("name", "Unknown AI")
            score = ai.get("confidence_score", ai.get("score", "N/A"))
            reason = ai.get("reason", "No explanation available.")
            website = ai.get(
                "official_website",
                ai.get("url", "https://www.google.com")
            )

            st.markdown(f"""
            <div class="card">
                <h3>{medal} {name}</h3>
            </div>
            """, unsafe_allow_html=True)

            left, right = st.columns([4, 1])

            with left:

                st.metric(
                    "Confidence",
                    f"{score}%"
                )

                st.markdown("#### 💡 Why this AI?")

                st.write(reason)

            with right:

                st.link_button(
                    "🚀 Launch",
                    website,
                    use_container_width=True
                )

            st.markdown("<br>", unsafe_allow_html=True)

    else:

        st.warning("No recommendations returned.")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr>

<div class="footer">

<h2>🤖 PromptWise AI Pro</h2>

<p>

AI Powered Prompt Engineering Platform

</p>

<p>

Built using

<strong>Machine Learning</strong> •

<strong>Natural Language Processing</strong> •

<strong>Generative AI</strong> •

<strong>Gemini API</strong>

</p>

<p style="color:#6B7280;">

© 2026 PromptWise AI

</p>

</div>

""", unsafe_allow_html=True)