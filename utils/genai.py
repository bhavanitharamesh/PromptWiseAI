import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)
# ----------------------------
# Load PromptWise System Prompt
# ----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SYSTEM_PROMPT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "system_prompt.txt"
)

with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


# ----------------------------
# Prompt Generator
# ----------------------------

def generate_prompt(
    role,
    task,
    context,
    constraint,
    output_format,
    goal,
):

    user_prompt = f"""
AI Role:
{role}

Task:
{task}

Context:
{context}

Constraints:
{constraint}

Output Format:
{output_format}

Goal:
{goal}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\n\n" + user_prompt
    )

    return response.text

def recommend_ai(
    role,
    task,
    context,
    constraint,
    output_format,
    goal
):

    # Load AI Consultant Prompt

    RECOMMENDER_PROMPT_PATH = os.path.join(
        BASE_DIR,
        "assets",
        "recommender_prompt.txt"
    )

    with open(RECOMMENDER_PROMPT_PATH, "r", encoding="utf-8") as f:
        recommender_prompt = f.read()


    user_prompt = f"""
User Requirement

Role:
{role}

Task:
{task}

Context:
{context}

Constraints:
{constraint}

Output Format:
{output_format}

Goal:
{goal}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=recommender_prompt + "\n\n" + user_prompt
    )

       
    import re

    text = response.text.strip()

    # Remove markdown fences
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Extract JSON array
    match = re.search(r"\[.*\]", text, re.DOTALL)

    if not match:
        print("Gemini Response:")
        print(text)
        return []

    json_text = match.group()

    try:
        return json.loads(json_text)

    except Exception as e:
        print("JSON Error:", e)
        print(json_text)
        return []