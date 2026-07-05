import os
import json
import re

import streamlit as st
from dotenv import load_dotenv
from google import genai

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Configure it in .env (local) or Streamlit Secrets."
    )

client = genai.Client(api_key=api_key)

# ---------------------------------------------------
# Load PromptWise System Prompt
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SYSTEM_PROMPT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "system_prompt.txt"
)

with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# ---------------------------------------------------
# Prompt Generator
# ---------------------------------------------------

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

# ---------------------------------------------------
# AI Recommendation Engine
# ---------------------------------------------------

def recommend_ai(
    role,
    task,
    context,
    constraint,
    output_format,
    goal
):

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

    print("\n========== GEMINI RESPONSE ==========")
    print(response.text)
    print("=====================================\n")

    text = response.text.strip()

    # Remove markdown fences
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Extract JSON array
    match = re.search(r"\[.*\]", text, re.DOTALL)

    if not match:
        print("❌ No JSON array found.")
        print(text)
        return []

    json_text = match.group()

    try:

        result = json.loads(json_text)

        print("\n========== PARSED RESULT ==========")
        print(result)
        print("===================================\n")

        return result

    except Exception as e:

        print("\n========== JSON ERROR ==========")
        print(e)
        print(json_text)
        print("================================\n")

        return []