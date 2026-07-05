"""
====================================================
PromptWise AI
Dataset Generation Engine
====================================================

This module generates synthetic prompt engineering
datasets using the PromptWise Knowledge Base.

Workflow:
AI Role
    ↓
Task
    ↓
Context
    ↓
Constraint
    ↓
Output Format
    ↓
Goal
    ↓
Recommended AI
    ↓
Generated Prompt
"""

import random
import pandas as pd
from datetime import datetime

# Knowledge Base Imports
from utils.knowledge.ai_roles import AI_ROLES
from utils.knowledge.task_mapping import TASK_MAPPING
from utils.knowledge.context_mapping import CONTEXT_MAPPING
from utils.knowledge.constraints import CONSTRAINTS
from utils.knowledge.output_formats import OUTPUT_FORMATS
from utils.knowledge.goals import GOALS
from utils.knowledge.ai_tools import AI_TOOLS

def build_prompt(role,
                 task,
                 context,
                 constraint,
                 output_format,
                 goal):


    prompt = f"""
You are an {role}.

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

    return prompt.strip()

def recommend_ai(task, goal):

    task = task.lower()
    goal = goal.lower()

    scores = {
        "ChatGPT": 0,
        "Claude": 0,
        "Gemini": 0,
        "Perplexity": 0,
        "Gamma": 0,
        "NotebookLM": 0
    }

    # ---------- Task Based ----------

    if any(word in task for word in ["code", "python", "debug", "algorithm", "api"]):
        scores["ChatGPT"] += 3
        scores["Gemini"] += 2

    if any(word in task for word in ["machine learning", "model", "feature", "eda", "prediction"]):
        scores["ChatGPT"] += 3
        scores["Gemini"] += 2

    if any(word in task for word in ["research", "literature", "paper", "methodology"]):
        scores["Claude"] += 3
        scores["Perplexity"] += 2

    if any(word in task for word in ["presentation", "slides", "pitch"]):
        scores["Gamma"] += 4

    if any(word in task for word in ["document", "summary", "pdf"]):
        scores["NotebookLM"] += 4

    if any(word in task for word in ["analysis", "market", "business"]):
        scores["Claude"] += 2
        scores["Perplexity"] += 2

    # ---------- Goal Based ----------

    if "presentation" in goal:
        scores["Gamma"] += 4

    if "research" in goal:
        scores["Claude"] += 3
        scores["Perplexity"] += 3

    if "project" in goal:
        scores["ChatGPT"] += 2

    if "interview" in goal:
        scores["ChatGPT"] += 2

    if "learning" in goal:
        scores["Gemini"] += 2

    # ---------- Default ----------

    if max(scores.values()) == 0:
        scores["ChatGPT"] += 1
        scores["Gemini"] += 1
        scores["Claude"] += 1

    return max(scores, key=scores.get)

def generate_dataset(num_rows=1000):

    dataset = []

    for i in range(num_rows):

        # Select Role
        role = random.choice(AI_ROLES)

        # Select Task
        task = random.choice(TASK_MAPPING[role])

        
        # Select Context
        if task in CONTEXT_MAPPING:
            context = random.choice(CONTEXT_MAPPING[task])
        else:
            context = "General Professional Scenario"


        # Constraint
        constraint = random.choice(CONSTRAINTS)

        # Output Format
        output_format = random.choice(OUTPUT_FORMATS)

        # Goal
        goal = random.choice(GOALS)

        # AI Recommendation
        recommended_ai = recommend_ai(task, goal)

        # Prompt
        prompt = build_prompt(
            role,
            task,
            context,
            constraint,
            output_format,
            goal
        )

        # Prompt ID
        prompt_id = f"PW{i+1:05d}"

        # Timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        dataset.append({

            "Prompt_ID": prompt_id,

            "AI_Role": role,

            "Task": task,

            "Context": context,

            "Constraint": constraint,

            "Output_Format": output_format,

            "Goal": goal,

            "Recommended_AI": recommended_ai,

            "Generated_Prompt": prompt,

            "Timestamp": timestamp

        })

    df = pd.DataFrame(dataset)

    return df