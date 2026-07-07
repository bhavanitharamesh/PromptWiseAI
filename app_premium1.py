"""
PromptWise AI Pro — Premium UI (app_premium.py)
-------------------------------------------------
A standalone, industry-grade UI layer for PromptWise AI Pro.

This file is INTENTIONALLY separate from your existing app.py.
It does not modify, import-and-break, or replace anything in your
current stable v1 project. Run it side by side:

    streamlit run app_premium.py

WIRING TO YOUR REAL BACKEND
----------------------------
This file tries to import your real modules:
    utils/ml_recommender.py  -> get_recommendations(role, task, context, goal)
    utils/genai.py           -> generate_prompt(role, task, context, constraints, output_format, goal)

If those exact function names don't match what's in your utils files,
just edit the two `from utils...import...` lines near the top (marked
with # >>> ADAPT THIS) to match your real function names. Until then,
this file runs on realistic mock data so you can preview the full UI
immediately without touching your ML/Gemini code at all.

DEPENDENCIES
-------------
    pip install streamlit streamlit-extras

streamlit-extras is optional — if it's missing, the app still runs,
it just falls back to plain (non-bordered) containers for the cards.
"""

import time
import random
from contextlib import contextmanager

import streamlit as st

# ----------------------------------------------------------------------------
# Optional: streamlit-extras for properly scoped, uniform "card" containers.
# ----------------------------------------------------------------------------
try:
    from streamlit_extras.stylable_container import stylable_container
    HAS_EXTRAS = True
except ImportError:
    HAS_EXTRAS = False

    @contextmanager
    def stylable_container(key=None, css_styles=""):
        with st.container():
            yield


# ----------------------------------------------------------------------------
# Backend wiring — >>> ADAPT THIS if your real function names differ <<<
# ----------------------------------------------------------------------------
try:
    from utils.ml_recommender import get_recommendations  # noqa: F401
except ImportError:
    def get_recommendations(role, task, context, goal):
        """Mock fallback so the UI is fully previewable without the real ML model."""
        assistants = [
            "ChatGPT", "Claude", "Gemini", "Perplexity", "GitHub Copilot",
            "Microsoft Copilot", "Cursor AI", "DeepSeek", "Grok", "Qwen",
        ]
        picks = random.sample(assistants, 3)
        scores = sorted([random.uniform(0.58, 0.96) for _ in range(3)], reverse=True)
        return list(zip(picks, scores))

try:
    from utils.genai import generate_prompt  # noqa: F401
except ImportError:
    def generate_prompt(role, task, context, constraints, output_format, goal):
        """Mock fallback so the UI is fully previewable without calling Gemini."""
        return (
            f"ROLE\n{role}\n\n"
            f"TASK\n{task}\n\n"
            f"CONTEXT\n{context}\n\n"
            f"CONSTRAINTS\n{constraints}\n\n"
            f"OUTPUT FORMAT\n{output_format}\n\n"
            f"GOAL\n{goal}\n\n"
            f"---\n"
            f"(This is placeholder text. Connect utils/genai.py's real "
            f"generate_prompt() to replace this with an actual Gemini-crafted prompt.)"
        )


# ----------------------------------------------------------------------------
# Static reference data — assistant branding metadata for the results page
# ----------------------------------------------------------------------------
ASSISTANT_META = {
    "ChatGPT":            {"color": "#10A37F", "site": "https://chat.openai.com",              "glyph": "GPT"},
    "Claude":             {"color": "#D97757", "site": "https://claude.ai",                     "glyph": "CL"},
    "Gemini":             {"color": "#4285F4", "site": "https://gemini.google.com",              "glyph": "GM"},
    "Perplexity":         {"color": "#20808D", "site": "https://www.perplexity.ai",              "glyph": "PX"},
    "GitHub Copilot":     {"color": "#8957E5", "site": "https://github.com/features/copilot",    "glyph": "GH"},
    "Microsoft Copilot":  {"color": "#0078D4", "site": "https://copilot.microsoft.com",          "glyph": "MS"},
    "Cursor AI":          {"color": "#6C6C6C", "site": "https://www.cursor.com",                 "glyph": "CU"},
    "DeepSeek":           {"color": "#4D6BFE", "site": "https://www.deepseek.com",                "glyph": "DS"},
    "Grok":               {"color": "#1D9BF0", "site": "https://grok.x.ai",                      "glyph": "GK"},
    "Qwen":               {"color": "#615CED", "site": "https://qwenlm.ai",                      "glyph": "QW"},
}


# ----------------------------------------------------------------------------
# Page config — must be the first Streamlit call
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="PromptWise AI Pro | Studio",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ----------------------------------------------------------------------------
# Global CSS — design tokens + component styling
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --pw-bg: #0A0E1A;
    --pw-surface: #121830;
    --pw-surface-2: #171f3d;
    --pw-border: #262E4D;
    --pw-accent: #6C5CE7;
    --pw-accent-2: #22D3EE;
    --pw-gold: #F0B429;
    --pw-success: #34D399;
    --pw-text: #F1F3FA;
    --pw-text-muted: #8B93B0;
    --pw-radius: 16px;
}

/* ---------- App shell ---------- */
[data-testid="stAppViewContainer"] {
    background-color: var(--pw-bg);
    background-image:
        linear-gradient(rgba(108, 92, 231, 0.055) 1px, transparent 1px),
        linear-gradient(90deg, rgba(108, 92, 231, 0.055) 1px, transparent 1px);
    background-size: 42px 42px;
}
[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 760px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: var(--pw-text);
}
h1, h2, h3, .pw-display {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--pw-text) !important;
    letter-spacing: -0.01em;
}

/* ---------- Brand mark ---------- */
.pw-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    color: var(--pw-text-muted);
    margin-bottom: 2.2rem;
}
.pw-brand-mark {
    width: 28px; height: 28px;
    border: 1.5px solid var(--pw-accent);
    border-radius: 7px;
    display: flex; align-items: center; justify-content: center;
    color: var(--pw-accent-2);
    font-size: 0.75rem;
    font-weight: 700;
}

/* ---------- Step pills ---------- */
.pw-steps {
    display: flex;
    gap: 8px;
    margin-bottom: 2.4rem;
}
.pw-step {
    flex: 1;
    text-align: center;
    padding: 8px 6px;
    border-radius: 10px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    border: 1px solid var(--pw-border);
    color: var(--pw-text-muted);
    background: var(--pw-surface);
}
.pw-step.active {
    border-color: var(--pw-accent);
    color: var(--pw-accent-2);
    background: linear-gradient(180deg, rgba(108,92,231,0.18), rgba(108,92,231,0.05));
}
.pw-step.done {
    color: var(--pw-success);
    border-color: rgba(52, 211, 153, 0.4);
}

/* ---------- Hero ---------- */
.pw-hero {
    text-align: center;
    padding: 2.4rem 0 1.6rem 0;
}
.pw-eyebrow {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    color: var(--pw-accent-2);
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.25);
    padding: 5px 12px;
    border-radius: 999px;
    margin-bottom: 1.3rem;
    text-transform: uppercase;
}
.pw-hero h1 {
    font-size: 2.5rem;
    line-height: 1.15;
    margin: 0 0 1rem 0;
}
.pw-hero h1 span {
    background: linear-gradient(135deg, var(--pw-accent-2), var(--pw-accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.pw-hero p {
    color: var(--pw-text-muted);
    font-size: 1.02rem;
    max-width: 480px;
    margin: 0 auto 0.5rem auto;
    line-height: 1.6;
}
.pw-chips {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 1.8rem;
}
.pw-chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--pw-text-muted);
    border: 1px solid var(--pw-border);
    padding: 6px 12px;
    border-radius: 8px;
    background: var(--pw-surface);
}

/* ---------- Buttons ---------- */
.stButton > button, .stDownloadButton > button {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    background: linear-gradient(135deg, var(--pw-accent), #8B7CF6);
    color: white;
    border: none;
    border-radius: 11px;
    padding: 0.7rem 1.6rem;
    box-shadow: 0 10px 28px rgba(108, 92, 231, 0.32);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    width: 100%;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 34px rgba(108, 92, 231, 0.45);
    color: white;
}
.stButton > button:focus-visible {
    outline: 2px solid var(--pw-accent-2);
    outline-offset: 2px;
}
button[kind="secondary"] {
    background: var(--pw-surface) !important;
    border: 1px solid var(--pw-border) !important;
    box-shadow: none !important;
}

.stLinkButton > a {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    border-radius: 10px !important;
    border: 1px solid var(--pw-border) !important;
    background: var(--pw-surface-2) !important;
    color: var(--pw-text) !important;
    box-shadow: none !important;
    width: 100%;
    justify-content: center !important;
}
.stLinkButton > a:hover {
    border-color: var(--pw-accent) !important;
    color: var(--pw-accent-2) !important;
}

/* ---------- Field cards ---------- */
.pw-field-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    color: var(--pw-accent-2);
    text-transform: uppercase;
    margin-bottom: 6px;
    display: block;
}
.stTextArea textarea, .stTextInput input,
[data-baseweb="textarea"] textarea, [data-baseweb="base-input"] input {
    background: var(--pw-surface-2) !important;
    color: var(--pw-text) !important;
    -webkit-text-fill-color: var(--pw-text) !important;
    caret-color: var(--pw-text) !important;
    border: 1px solid var(--pw-border) !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextArea textarea::placeholder, .stTextInput input::placeholder {
    color: var(--pw-text-muted) !important;
    opacity: 1 !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: var(--pw-accent) !important;
    box-shadow: 0 0 0 1px var(--pw-accent) !important;
}

/* ---------- Recommendation cards ---------- */
.pw-badge {
    width: 42px; height: 42px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.72rem;
    color: white;
    flex-shrink: 0;
}
.pw-rec-name {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 1.05rem;
    margin: 0;
    color: var(--pw-text) !important;
}
.pw-rec-rank {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--pw-text-muted) !important;
    letter-spacing: 0.08em;
}

/* Safety net: force readable color on any markdown text we didn't
   explicitly style, regardless of Streamlit's internal class hashing. */
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] div {
    color: var(--pw-text);
}
.pw-confidence-track {
    width: 100%;
    height: 6px;
    background: var(--pw-border);
    border-radius: 999px;
    overflow: hidden;
    margin: 10px 0 4px 0;
}
.pw-confidence-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--pw-accent), var(--pw-accent-2));
}
.pw-confidence-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--pw-text-muted);
}

/* ---------- Prompt output ---------- */
.stCodeBlock, pre {
    border-radius: var(--pw-radius) !important;
    border: 1px solid var(--pw-border) !important;
}
code, pre, .stCodeBlock * {
    font-family: 'JetBrains Mono', monospace !important;
}

/* ---------- Transition screen ---------- */
.pw-transition {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 5rem 0;
    animation: pwFadeIn 0.35s ease;
}
.pw-ring {
    width: 46px; height: 46px;
    border-radius: 50%;
    border: 3px solid var(--pw-border);
    border-top-color: var(--pw-accent-2);
    animation: pwSpin 0.8s linear infinite;
    margin-bottom: 1.2rem;
}
.pw-transition p {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.06em;
    color: var(--pw-text-muted);
    text-transform: uppercase;
}
@keyframes pwSpin { to { transform: rotate(360deg); } }
@keyframes pwFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

.block-container { animation: pwFadeIn 0.45s ease; }

hr { border-color: var(--pw-border) !important; }
</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------
defaults = {
    "page": "home",
    "role": "", "task": "", "context": "",
    "constraints": "", "output_format": "", "goal": "",
    "generated_prompt": None,
    "recommendations": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ----------------------------------------------------------------------------
# Shared UI helpers
# ----------------------------------------------------------------------------
def brand_header():
    st.markdown("""
    <div class="pw-brand">
        <div class="pw-brand-mark">P</div>
        PromptWise AI Pro &nbsp;·&nbsp; Studio
    </div>
    """, unsafe_allow_html=True)


def step_pills(current):
    steps = ["01 · Build", "02 · Generate", "03 · Results"]
    order = ["home", "builder", "results"]
    idx = order.index(current) if current in order else 0
    html = '<div class="pw-steps">'
    for i, label in enumerate(steps):
        cls = "pw-step"
        if i == idx:
            cls += " active"
        elif i < idx:
            cls += " done"
        html += f'<div class="{cls}">{label}</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def transition_to(target_page, message="Preparing your workspace..."):
    """A short, branded loading interstitial — gives the 'premium smooth
    transition' feel between views, since Streamlit re-renders the whole
    script rather than animating between components natively."""
    placeholder = st.empty()
    with placeholder.container():
        st.markdown(f"""
        <div class="pw-transition">
            <div class="pw-ring"></div>
            <p>{message}</p>
        </div>
        """, unsafe_allow_html=True)
    time.sleep(0.85)
    st.session_state.page = target_page
    placeholder.empty()
    st.rerun()


def confidence_bar(score):
    pct = max(0, min(100, round(score * 100)))
    st.markdown(f"""
    <div class="pw-confidence-track">
        <div class="pw-confidence-fill" style="width:{pct}%;"></div>
    </div>
    <div class="pw-confidence-label">{pct}% match confidence</div>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# PAGE: HOME
# ----------------------------------------------------------------------------
def render_home():
    brand_header()
    st.markdown("""
    <div class="pw-hero">
        <span class="pw-eyebrow">ML-Powered · Gemini-Generated</span>
        <h1>Engineer prompts<br><span>like blueprints.</span></h1>
        <p>Turn a rough idea into a structured, professional prompt —
        and let a trained model tell you exactly which AI assistant
        will run it best.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        if st.button("Start Building  →", key="start_btn", use_container_width=True):
            transition_to("builder", "Loading the prompt builder...")

    st.markdown("""
    <div class="pw-chips">
        <div class="pw-chip">RANDOM FOREST + TF-IDF</div>
        <div class="pw-chip">TOP 3 RECOMMENDATIONS</div>
        <div class="pw-chip">GEMINI 2.5 FLASH</div>
    </div>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# PAGE: BUILDER
# ----------------------------------------------------------------------------
FIELD_SPEC = [
    ("role", "Field 01 · Role", "e.g. Senior backend engineer reviewing a pull request"),
    ("task", "Field 02 · Task", "e.g. Review this code for security vulnerabilities"),
    ("context", "Field 03 · Context", "e.g. Node.js REST API handling payment data"),
    ("constraints", "Field 04 · Constraints", "e.g. Keep feedback under 200 words, no rewrites"),
    ("output_format", "Field 05 · Output Format", "e.g. Bullet list grouped by severity"),
    ("goal", "Field 06 · Goal", "e.g. Ship a safer PR without blocking the release"),
]

FIELD_CARD_CSS = """
{
    background-color: var(--pw-surface);
    border: 1px solid var(--pw-border);
    border-radius: 14px;
    padding: 16px 18px 10px 18px;
    min-height: 168px;
}
"""


def render_builder():
    brand_header()
    step_pills("builder")

    st.markdown("### Structured Prompt Builder")
    st.markdown(
        '<p style="color:var(--pw-text-muted); margin-top:-8px;">'
        'Fill in each field below — these map directly to the recommendation model\'s '
        'feature set.</p>',
        unsafe_allow_html=True,
    )
    st.write("")

    rows = [FIELD_SPEC[i:i + 2] for i in range(0, len(FIELD_SPEC), 2)]
    for row in rows:
        cols = st.columns(2)
        for col, (key, label, placeholder) in zip(cols, row):
            with col:
                with stylable_container(key=f"card_{key}", css_styles=FIELD_CARD_CSS):
                    st.markdown(f'<span class="pw-field-label">{label}</span>', unsafe_allow_html=True)
                    st.session_state[key] = st.text_area(
                        label=key,
                        value=st.session_state[key],
                        placeholder=placeholder,
                        height=100,
                        label_visibility="collapsed",
                        key=f"input_{key}",
                    )
        st.write("")

    required_filled = all(st.session_state[k].strip() for k, _, _ in FIELD_SPEC)

    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("← Back to Home", key="back_home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    with c2:
        generate_clicked = st.button(
            "Generate Prompt  →",
            key="generate_btn",
            use_container_width=True,
            disabled=not required_filled,
        )

    if not required_filled:
        st.markdown(
            '<p style="color:var(--pw-text-muted); font-size:0.82rem; text-align:center;">'
            'Fill in all six fields to continue.</p>',
            unsafe_allow_html=True,
        )

    if generate_clicked and required_filled:
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("""
            <div class="pw-transition">
                <div class="pw-ring"></div>
                <p>Running ML recommendation + Gemini generation...</p>
            </div>
            """, unsafe_allow_html=True)

        recs = get_recommendations(
            st.session_state.role, st.session_state.task,
            st.session_state.context, st.session_state.goal,
        )
        prompt = generate_prompt(
            st.session_state.role, st.session_state.task, st.session_state.context,
            st.session_state.constraints, st.session_state.output_format, st.session_state.goal,
        )
        time.sleep(0.6)

        st.session_state.recommendations = recs
        st.session_state.generated_prompt = prompt
        st.session_state.page = "results"
        placeholder.empty()
        st.rerun()


# ----------------------------------------------------------------------------
# PAGE: RESULTS
# ----------------------------------------------------------------------------
def render_results():
    brand_header()
    step_pills("results")

    st.markdown("### Your Generated Prompt")
    st.write("")
    st.code(st.session_state.generated_prompt or "", language=None)

    dcol1, dcol2 = st.columns(2)
    with dcol1:
        st.download_button(
            "Download as .txt",
            data=st.session_state.generated_prompt or "",
            file_name="promptwise_prompt.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with dcol2:
        if st.button("Build Another Prompt  ↻", use_container_width=True):
            st.session_state.page = "builder"
            st.rerun()

    st.write("")
    st.write("")
    st.markdown("### Recommended AI Assistants")
    st.markdown(
        '<p style="color:var(--pw-text-muted); margin-top:-8px;">'
        'Ranked by the Random Forest classifier\'s confidence score.</p>',
        unsafe_allow_html=True,
    )
    st.write("")

    recs = st.session_state.recommendations or []
    for rank, (name, score) in enumerate(recs, start=1):
        meta = ASSISTANT_META.get(name, {"color": "#6C5CE7", "site": "#", "glyph": name[:2].upper()})
        with stylable_container(
            key=f"rec_{rank}",
            css_styles="""
            {
                background-color: var(--pw-surface);
                border: 1px solid var(--pw-border);
                border-radius: 14px;
                padding: 18px 20px;
                margin-bottom: 12px;
            }
            """,
        ):
            top = st.columns([0.14, 0.56, 0.3])
            with top[0]:
                st.markdown(
                    f'<div class="pw-badge" style="background:{meta["color"]};">{meta["glyph"]}</div>',
                    unsafe_allow_html=True,
                )
            with top[1]:
                st.markdown(f'<span class="pw-rec-rank">RANK {rank}</span>', unsafe_allow_html=True)
                st.markdown(f'<p class="pw-rec-name">{name}</p>', unsafe_allow_html=True)
            with top[2]:
                st.link_button("Visit Site ↗", meta["site"], use_container_width=True)
            confidence_bar(score)


# ----------------------------------------------------------------------------
# Router
# ----------------------------------------------------------------------------
if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "builder":
    render_builder()
elif st.session_state.page == "results":
    render_results()
