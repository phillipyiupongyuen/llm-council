"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# LLM backend: "openrouter" (pay per token, mixed providers) or
# "claude_cli" (runs `claude -p`, uses your Claude subscription, Claude-only).
LLM_BACKEND = os.getenv("LLM_BACKEND", "openrouter")

if LLM_BACKEND == "claude_cli":
    # Model names as accepted by `claude --model`. Must be unique per seat.
    COUNCIL_MODELS = [
        "claude-opus-5-5",
        "claude-fable-5-1",
        "claude-sonnet-5-5",
        "claude-haiku-4-5-20251001",
    ]
    CHAIRMAN_MODEL = "claude-fable-5-1"
else:
    # Council members - list of OpenRouter model identifiers
    COUNCIL_MODELS = [
        "openai/gpt-6-sol",
        "google/gemini-3.1-pro-preview",
        "anthropic/claude-opus-5.5",
        "x-ai/grok-4.7",
    ]

    # Chairman model - synthesizes final response
    CHAIRMAN_MODEL = "anthropic/claude-fable-5.1"

# Product council roles - one per council model (matched by position).
# Edit freely. Each entry: (display name, system prompt).
PRODUCT_CONTEXT = "Assume an early-stage B2B SaaS unless the user says otherwise."

ROLES = [
    ("Customer",
     "You are the target customer for the product described. Be blunt. "
     "Would you pay for this? What confuses you? What would make you churn? "
     "What do you use today instead? Ground every point in a realistic day-in-the-life."),
    ("Skeptical Investor",
     "You are a skeptical early-stage investor. Stress-test market size, "
     "willingness to pay, moat, distribution, and 'why now'. "
     "Name the single assumption most likely to kill this."),
    ("Eng Lead",
     "You are a pragmatic engineering lead. Assess feasibility, hidden complexity, "
     "data and integration dependencies, and the smallest buildable version. "
     "Flag anything that sounds easy but isn't."),
    ("Competitor",
     "You are the strongest competitor or incumbent in this space. "
     "How would you copy, undercut, or neutralise this product? "
     "What do you already have that makes this hard to win against?"),
]


# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
