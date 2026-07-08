"""
PromptWise AI Pro — Ultra Premium UI (app_ultra.py)
-----------------------------------------------------------------
A standalone, industry-grade UI layer for PromptWise AI Pro.

This file is INTENTIONALLY separate from app.py. It never imports,
modifies, or breaks anything in the stable v1 project. Run it
side by side:

    streamlit run app_ultra.py

DESIGN CONCEPT — "The Drafting Table"
-----------------------------------------------------------------
PromptWise turns a rough idea into a structured spec, the same way
an engineering drawing turns an idea into a buildable blueprint.
The UI borrows the vocabulary of a technical drafting table:
title blocks, registration marks, ruler/dimension lines, and a
pen-plotter loading motion — instead of a generic dark SaaS dashboard.

Palette (named tokens, see CSS root below):
    ink      #080C18  base
    panel    #101A32  card surface
    brass    #D3A94D  primary action / premium accent (drafting instrument)
    cyan     #45D3E8  schematic / structural accent (blueprint line)
    indigo   #7C6FF0  intelligence / ML accent
    emerald  #34D399  success / completion

WIRING TO YOUR REAL BACKEND
-----------------------------------------------------------------
Tries to import the real modules:
    utils/ml_recommender.py -> recommend_ai_ml(role, task, context,
                                constraint, output_format, goal)
    utils/genai.py           -> generate_prompt(role, task, context,
                                constraint, output_format, goal)

utils/genai.py raises a plain Exception at import time if
GEMINI_API_KEY is missing (not just ImportError), so the fallback
below catches broad Exception on purpose. If those exact function
names differ, edit the two `# >>> ADAPT THIS` blocks near the top.
Until then, this file runs on realistic mock data so the full UI
previews immediately without any ML/Gemini calls.

DEPENDENCIES
-------------
    pip install streamlit streamlit-extras
"""

import time
import random
from contextlib import contextmanager

import streamlit as st

# ----------------------------------------------------------------------------
# Optional: streamlit-extras for properly scoped "card" containers.
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
    from utils.ml_recommender import recommend_ai_ml as _recommend_ai_ml

    def get_recommendations(role, task, context, constraints, output_format, goal):
        return _recommend_ai_ml(role, task, context, constraints, output_format, goal)
except Exception:
    def get_recommendations(role, task, context, constraints, output_format, goal):
        """Mock fallback — same shape as utils/ml_recommender.recommend_ai_ml."""
        assistants = [
            "ChatGPT", "Claude", "Gemini", "Perplexity", "GitHub Copilot",
            "Microsoft Copilot", "Cursor AI", "DeepSeek", "Grok", "Qwen",
        ]
        picks = random.sample(assistants, 3)
        raw = sorted([random.uniform(0.30, 0.95) for _ in range(3)], reverse=True)
        total = sum(raw)
        out = []
        for name, s in zip(picks, raw):
            out.append({
                "name": name,
                "confidence_score": round((s / total) * 100, 2),
                "reason": f"Your requirement closely matches tasks where {name} performs "
                          f"exceptionally well.",
                "official_website": ASSISTANT_META.get(name, {}).get("site", "#"),
            })
        return out

try:
    from utils.genai import generate_prompt as _generate_prompt

    def generate_prompt(role, task, context, constraints, output_format, goal):
        return _generate_prompt(role, task, context, constraints, output_format, goal)
except Exception:
    def generate_prompt(role, task, context, constraints, output_format, goal):
        """Mock fallback so the UI previews without calling Gemini."""
        return (
            f"ROLE\n{role}\n\n"
            f"TASK\n{task}\n\n"
            f"CONTEXT\n{context}\n\n"
            f"CONSTRAINTS\n{constraints}\n\n"
            f"OUTPUT FORMAT\n{output_format}\n\n"
            f"GOAL\n{goal}\n\n"
            f"---\n"
            f"(Placeholder text — GEMINI_API_KEY not detected, or utils/genai.py "
            f"could not be imported. Connect it to replace this with a real prompt.)"
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
    "Cursor AI":          {"color": "#6C6C6C", "site": "https://cursor.com",                     "glyph": "CU"},
    "DeepSeek":           {"color": "#4D6BFE", "site": "https://chat.deepseek.com",              "glyph": "DS"},
    "Grok":               {"color": "#1D9BF0", "site": "https://grok.com",                       "glyph": "GK"},
    "Qwen":               {"color": "#615CED", "site": "https://chat.qwen.ai",                   "glyph": "QW"},
}

RANK_ACCENTS = ["#D3A94D", "#45D3E8", "#7C6FF0"]  # brass, cyan, indigo — rank 1/2/3


# ----------------------------------------------------------------------------
# Page config — must be the first Streamlit call
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="PromptWise AI Pro | Drafting Table",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ----------------------------------------------------------------------------
# Global CSS — design tokens + component styling
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --ink: #080C18;
    --ink-2: #0D1428;
    --panel: #101A32;
    --panel-2: #16223F;
    --line: #223056;
    --brass: #D3A94D;
    --brass-bright: #F0C874;
    --cyan: #45D3E8;
    --indigo: #7C6FF0;
    --emerald: #34D399;
    --paper: #EDF1FB;
    --paper-muted: #8B96B8;
    --radius: 14px;
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.001ms !important; animation-iteration-count: 1 !important; transition-duration: 0.001ms !important; }
}

/* ---------- App shell ---------- */
[data-testid="stAppViewContainer"] {
    background-color: var(--ink);
    background-image:
        radial-gradient(720px circle at 12% -6%, rgba(124,111,240,0.10), transparent 55%),
        radial-gradient(620px circle at 92% 8%, rgba(69,211,232,0.08), transparent 50%),
        linear-gradient(rgba(69,211,232,0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(69,211,232,0.045) 1px, transparent 1px);
    background-size: auto, auto, 44px 44px, 44px 44px;
}
[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 780px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
    animation: pwFadeIn 0.5s ease;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: var(--paper);
}
h1, h2, h3, .pw-display {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--paper) !important;
    letter-spacing: -0.01em;
}
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] div { color: var(--paper); }

/* ---------- Title block (replaces plain brand header) ---------- */
.pw-titleblock {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 16px;
    margin-bottom: 2.2rem;
    border-bottom: 1px solid var(--line);
}
.pw-titleblock-left { display: flex; align-items: center; gap: 12px; }
.pw-mark-box {
    width: 36px; height: 36px;
    border: 1.5px solid var(--brass);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    color: var(--brass);
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    background: linear-gradient(180deg, rgba(211,169,77,0.14), transparent);
}
.pw-titleblock-name {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 0.98rem;
    line-height: 1.15;
}
.pw-titleblock-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.66rem;
    letter-spacing: 0.06em;
    color: var(--paper-muted);
}
.pw-titleblock-right {
    text-align: right;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.64rem;
    line-height: 1.7;
    letter-spacing: 0.04em;
    color: var(--paper-muted);
}
.pw-titleblock-right b { color: var(--cyan); font-weight: 600; }

/* ---------- Ruler-style step indicator ---------- */
.pw-ruler {
    position: relative;
    display: flex;
    justify-content: space-between;
    margin: 0 0 2.6rem 0;
    padding: 0 6px;
}
.pw-ruler::before {
    content: '';
    position: absolute;
    top: 9px; left: 6px; right: 6px;
    height: 1px;
    background: var(--line);
}
.pw-ruler-station {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    flex: 1;
}
.pw-ruler-dot {
    width: 18px; height: 18px;
    border-radius: 50%;
    background: var(--panel);
    border: 2px solid var(--line);
    transition: all 0.25s ease;
}
.pw-ruler-station.active .pw-ruler-dot {
    border-color: var(--brass);
    background: var(--brass);
    box-shadow: 0 0 0 5px rgba(211,169,77,0.16);
    animation: pwPulse 1.8s ease-in-out infinite;
}
.pw-ruler-station.done .pw-ruler-dot {
    border-color: var(--emerald);
    background: var(--emerald);
}
.pw-ruler-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.66rem;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: var(--paper-muted);
    white-space: nowrap;
}
.pw-ruler-station.active .pw-ruler-label { color: var(--brass-bright); }
.pw-ruler-station.done .pw-ruler-label { color: var(--emerald); }
@keyframes pwPulse {
    0%, 100% { box-shadow: 0 0 0 5px rgba(211,169,77,0.16); }
    50% { box-shadow: 0 0 0 9px rgba(211,169,77,0.05); }
}

/* ---------- Registration-mark corner brackets (signature motif) ---------- */
.pw-mark-corner {
    position: absolute;
    width: 13px; height: 13px;
    pointer-events: none;
    opacity: 0.55;
}
.pw-mark-corner.tl { top: 9px; left: 9px; border-top: 2px solid var(--brass); border-left: 2px solid var(--brass); }
.pw-mark-corner.br { bottom: 9px; right: 9px; border-bottom: 2px solid var(--brass); border-right: 2px solid var(--brass); }

/* ---------- Hero ---------- */
.pw-hero { text-align: center; padding: 2rem 0 1.6rem 0; }
.pw-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    color: var(--cyan);
    background: rgba(69, 211, 232, 0.08);
    border: 1px solid rgba(69, 211, 232, 0.28);
    padding: 5px 13px;
    border-radius: 999px;
    margin-bottom: 1.4rem;
    text-transform: uppercase;
}
.pw-hero h1 { font-size: 2.55rem; line-height: 1.14; margin: 0 0 1rem 0; }
.pw-hero h1 span {
    background: linear-gradient(135deg, var(--cyan), var(--brass-bright));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.pw-hero p {
    color: var(--paper-muted);
    font-size: 1.03rem;
    max-width: 480px;
    margin: 0 auto 0.5rem auto;
    line-height: 1.65;
}
.pw-chips { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 1.9rem; }
.pw-chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.02em;
    color: var(--paper-muted);
    border: 1px solid var(--line);
    padding: 6px 13px;
    border-radius: 8px;
    background: var(--panel);
    transition: border-color 0.2s ease, color 0.2s ease;
}
.pw-chip:hover { border-color: var(--brass); color: var(--brass-bright); }

/* ---------- Buttons: brass instrument, with shimmer sweep ---------- */
.stButton > button, .stDownloadButton > button {
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    background: linear-gradient(135deg, var(--brass), var(--brass-bright));
    color: #1A1404;
    border: none;
    border-radius: 11px;
    padding: 0.72rem 1.6rem;
    box-shadow: 0 12px 30px rgba(211, 169, 77, 0.28), inset 0 1px 0 rgba(255,255,255,0.35);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    width: 100%;
}
.stButton > button::after, .stDownloadButton > button::after {
    content: '';
    position: absolute;
    top: 0; left: -60%;
    width: 40%; height: 100%;
    background: linear-gradient(120deg, transparent, rgba(255,255,255,0.55), transparent);
    transform: skewX(-20deg);
    transition: left 0.55s ease;
}
.stButton > button:hover::after, .stDownloadButton > button:hover::after { left: 130%; }
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 16px 38px rgba(211, 169, 77, 0.42), inset 0 1px 0 rgba(255,255,255,0.4);
    color: #1A1404;
}
.stButton > button:active { transform: translateY(0); }
.stButton > button:focus-visible { outline: 2px solid var(--cyan); outline-offset: 2px; }
.stButton > button:disabled {
    background: var(--panel-2) !important;
    color: var(--paper-muted) !important;
    box-shadow: none !important;
}
button[kind="secondary"] {
    background: var(--panel) !important;
    color: var(--paper) !important;
    border: 1px solid var(--line) !important;
    box-shadow: none !important;
}
button[kind="secondary"]::after { display: none; }
button[kind="secondary"]:hover {
    border-color: var(--cyan) !important;
    color: var(--cyan) !important;
    transform: translateY(-1px);
}

.stLinkButton > a {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    border-radius: 10px !important;
    border: 1px solid var(--line) !important;
    background: var(--panel-2) !important;
    color: var(--paper) !important;
    box-shadow: none !important;
    width: 100%;
    justify-content: center !important;
    transition: border-color 0.2s ease, color 0.2s ease;
}
.stLinkButton > a:hover { border-color: var(--cyan) !important; color: var(--cyan) !important; }

/* ---------- Field cards ---------- */
.pw-field-tag {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 8px;
}
.pw-field-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.09em;
    color: var(--cyan);
    text-transform: uppercase;
}
.pw-field-index {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    color: var(--paper-muted);
}
.stTextArea textarea, .stTextInput input,
[data-baseweb="textarea"] textarea, [data-baseweb="base-input"] input {
    background: var(--panel-2) !important;
    color: var(--paper) !important;
    -webkit-text-fill-color: var(--paper) !important;
    caret-color: var(--paper) !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextArea textarea::placeholder, .stTextInput input::placeholder {
    color: var(--paper-muted) !important;
    opacity: 1 !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: var(--brass) !important;
    box-shadow: 0 0 0 1px var(--brass), 0 0 16px rgba(211,169,77,0.18) !important;
}

/* ---------- Recommendation cards ---------- */
.pw-badge-hex {
    width: 44px; height: 44px;
    clip-path: polygon(25% 4%, 75% 4%, 100% 50%, 75% 96%, 25% 96%, 0% 50%);
    display: flex; align-items: center; justify-content: center;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.68rem;
    color: #0A0E18;
    flex-shrink: 0;
}
.pw-rec-name {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 1.06rem;
    margin: 0;
    color: var(--paper) !important;
}
.pw-rec-rank {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.66rem;
    letter-spacing: 0.08em;
    color: var(--paper-muted) !important;
}
.pw-rec-reason {
    font-size: 0.86rem;
    color: var(--paper-muted) !important;
    line-height: 1.55;
    margin: 8px 0 0 0;
}
.pw-gauge-track {
    position: relative;
    width: 100%;
    height: 7px;
    border-radius: 4px;
    background: var(--panel-2);
    background-image: repeating-linear-gradient(90deg, rgba(255,255,255,0.07) 0 1px, transparent 1px 10%);
    overflow: hidden;
    margin: 12px 0 5px 0;
}
.pw-gauge-fill { height: 100%; border-radius: 4px; transition: width 0.6s ease; }
.pw-gauge-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--paper-muted);
}

/* ---------- Prompt output ---------- */
.stCodeBlock, pre { border-radius: var(--radius) !important; border: 1px solid var(--line) !important; }
code, pre, .stCodeBlock * { font-family: 'JetBrains Mono', monospace !important; }

/* ---------- Drafting-pen loader / transition ---------- */
.pw-loader {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.3rem;
    padding: 4.6rem 0;
    animation: pwFadeIn 0.3s ease;
}
.pw-loader-track {
    position: relative;
    width: 220px;
    height: 2px;
    background: var(--line);
    border-radius: 2px;
}
.pw-loader-fill {
    position: absolute;
    inset: 0;
    border-radius: 2px;
    background: linear-gradient(90deg, var(--cyan), var(--brass));
    transform-origin: left;
    animation: pwFill 1.3s ease-in-out infinite;
}
.pw-loader-pen {
    position: absolute;
    top: -5px;
    width: 12px; height: 12px;
    border-radius: 50%;
    background: var(--brass-bright);
    box-shadow: 0 0 12px rgba(240, 200, 116, 0.9);
    animation: pwPen 1.3s ease-in-out infinite;
}
.pw-loader p {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--paper-muted);
}
@keyframes pwFill { 0% { transform: scaleX(0); } 100% { transform: scaleX(1); } }
@keyframes pwPen { 0% { left: -6px; } 100% { left: 214px; } }
@keyframes pwFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

hr { border-color: var(--line) !important; }
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
def title_block():
    st.markdown("""
    <div class="pw-titleblock">
        <div class="pw-titleblock-left">
            <div class="pw-mark-box">P</div>
            <div>
                <div class="pw-titleblock-name">PromptWise AI Pro</div>
                <div class="pw-titleblock-sub">DRAFTING TABLE · STUDIO</div>
            </div>
        </div>
        <div class="pw-titleblock-right">
            DOC <b>PWA&#8209;01</b><br>REV 2026.07
        </div>
    </div>
    """, unsafe_allow_html=True)


def step_ruler(current):
    stations = [("01", "Build"), ("02", "Generate"), ("03", "Results")]
    order = ["home", "builder", "results"]
    # "home" and "builder" both map to station 0 ("Build") conceptually,
    # since the home screen is the entry to the builder step.
    idx = {"home": 0, "builder": 0, "results": 2}.get(current, 0)
    if current == "builder":
        idx = 0
    html = '<div class="pw-ruler">'
    for i, (num, label) in enumerate(stations):
        cls = "pw-ruler-station"
        if i == idx:
            cls += " active"
        elif i < idx:
            cls += " done"
        html += f'<div class="{cls}"><div class="pw-ruler-dot"></div><div class="pw-ruler-label">{num} · {label}</div></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def corner_marks():
    st.markdown(
        '<div class="pw-mark-corner tl"></div><div class="pw-mark-corner br"></div>',
        unsafe_allow_html=True,
    )


def transition_to(target_page, message="Preparing your workspace..."):
    """A branded pen-plotter loading interstitial between views, since
    Streamlit re-renders the whole script rather than animating natively."""
    placeholder = st.empty()
    with placeholder.container():
        st.markdown(f"""
        <div class="pw-loader">
            <div class="pw-loader-track">
                <div class="pw-loader-fill"></div>
                <div class="pw-loader-pen"></div>
            </div>
            <p>{message}</p>
        </div>
        """, unsafe_allow_html=True)
    time.sleep(0.85)
    st.session_state.page = target_page
    placeholder.empty()
    st.rerun()


def gauge_bar(pct, color):
    pct = max(0, min(100, round(pct)))
    st.markdown(f"""
    <div class="pw-gauge-track">
        <div class="pw-gauge-fill" style="width:{pct}%; background:linear-gradient(90deg, {color}, var(--cyan));"></div>
    </div>
    <div class="pw-gauge-label">{pct}% match confidence</div>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# PAGE: HOME
# ----------------------------------------------------------------------------
def render_home():
    title_block()
    st.markdown("""
    <div class="pw-hero">
        <span class="pw-eyebrow">&#9673; ML-Powered · Gemini-Generated</span>
        <h1>Engineer prompts<br><span>like blueprints.</span></h1>
        <p>Turn a rough idea into a structured, professional prompt —
        and let a trained model tell you exactly which AI assistant
        will run it best.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        if st.button("Start Building  →", key="start_btn", use_container_width=True):
            transition_to("builder", "Unrolling the blueprint...")

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
    ("role", "Role", "e.g. Senior backend engineer reviewing a pull request"),
    ("task", "Task", "e.g. Review this code for security vulnerabilities"),
    ("context", "Context", "e.g. Node.js REST API handling payment data"),
    ("constraints", "Constraints", "e.g. Keep feedback under 200 words, no rewrites"),
    ("output_format", "Output Format", "e.g. Bullet list grouped by severity"),
    ("goal", "Goal", "e.g. Ship a safer PR without blocking the release"),
]

FIELD_CARD_CSS = """
{
    position: relative;
    background-color: var(--panel);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 16px 18px 10px 18px;
    min-height: 172px;
}
"""


def render_builder():
    title_block()
    step_ruler("builder")

    st.markdown("### Structured Prompt Builder")
    st.markdown(
        '<p style="color:var(--paper-muted); margin-top:-8px;">'
        'Fill in each field below — these map directly to the recommendation model\'s '
        'feature set.</p>',
        unsafe_allow_html=True,
    )
    st.write("")

    total_fields = len(FIELD_SPEC)
    rows = [FIELD_SPEC[i:i + 2] for i in range(0, total_fields, 2)]
    for row in rows:
        cols = st.columns(2)
        for col, (key, label, placeholder) in zip(cols, row):
            field_num = FIELD_SPEC.index((key, label, placeholder)) + 1
            with col:
                with stylable_container(key=f"card_{key}", css_styles=FIELD_CARD_CSS):
                    corner_marks()
                    st.markdown(
                        f'<div class="pw-field-tag">'
                        f'<span class="pw-field-label">{label}</span>'
                        f'<span class="pw-field-index">{field_num:02d} / {total_fields:02d}</span>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
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
        if st.button("← Back to Home", key="back_home", use_container_width=True, type="secondary"):
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
            '<p style="color:var(--paper-muted); font-size:0.82rem; text-align:center;">'
            'Fill in all six fields to continue.</p>',
            unsafe_allow_html=True,
        )

    if generate_clicked and required_filled:
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("""
            <div class="pw-loader">
                <div class="pw-loader-track">
                    <div class="pw-loader-fill"></div>
                    <div class="pw-loader-pen"></div>
                </div>
                <p>Running ML recommendation + Gemini generation...</p>
            </div>
            """, unsafe_allow_html=True)

        recs = get_recommendations(
            st.session_state.role, st.session_state.task, st.session_state.context,
            st.session_state.constraints, st.session_state.output_format, st.session_state.goal,
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
    title_block()
    step_ruler("results")

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
        if st.button("Build Another Prompt  ↻", use_container_width=True, type="secondary"):
            st.session_state.page = "builder"
            st.rerun()

    st.write("")
    st.write("")
    st.markdown("### Recommended AI Assistants")
    st.markdown(
        '<p style="color:var(--paper-muted); margin-top:-8px;">'
        'Ranked by the Random Forest classifier\'s confidence score.</p>',
        unsafe_allow_html=True,
    )
    st.write("")

    recs = st.session_state.recommendations or []
    for rank, rec in enumerate(recs, start=1):
        # Support both dict-shaped (real backend) and tuple-shaped (legacy mock) records.
        if isinstance(rec, dict):
            name = rec.get("name", "Unknown")
            score = rec.get("confidence_score", 0)
            reason = rec.get("reason", "")
            site = rec.get("official_website")
        else:
            name, score = rec
            reason, site = "", None

        meta = ASSISTANT_META.get(name, {"color": "#6C5CE7", "site": "#", "glyph": name[:2].upper()})
        site = site or meta["site"]
        accent = RANK_ACCENTS[(rank - 1) % len(RANK_ACCENTS)]

        with stylable_container(
            key=f"rec_{rank}",
            css_styles="""
            {
                position: relative;
                background-color: var(--panel);
                border: 1px solid var(--line);
                border-radius: var(--radius);
                padding: 18px 20px;
                margin-bottom: 12px;
            }
            """,
        ):
            corner_marks()
            top = st.columns([0.14, 0.56, 0.3])
            with top[0]:
                st.markdown(
                    f'<div class="pw-badge-hex" style="background:{meta["color"]};">{meta["glyph"]}</div>',
                    unsafe_allow_html=True,
                )
            with top[1]:
                st.markdown(
                    f'<span class="pw-rec-rank" style="color:{accent} !important;">RANK {rank}</span>',
                    unsafe_allow_html=True,
                )
                st.markdown(f'<p class="pw-rec-name">{name}</p>', unsafe_allow_html=True)
            with top[2]:
                st.link_button("Visit Site ↗", site, use_container_width=True)
            gauge_bar(score, accent)
            if reason:
                st.markdown(f'<p class="pw-rec-reason">{reason}</p>', unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# Router
# ----------------------------------------------------------------------------
if st.session_state.page == "home":
    render_home()
elif st.session_state.page == "builder":
    render_builder()
elif st.session_state.page == "results":
    render_results()
