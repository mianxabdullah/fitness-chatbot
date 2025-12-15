# 🏋️ FitBuddy – Fitness Coach Chatbot (Gradio + Groq)

FitBuddy is a small but mighty fitness coach bot. Ask it about workouts, recovery, or nutrition, and it replies with concise, encouraging guidance. I built it with Gradio for the UI and Groq LLMs for fast, context-aware answers, then deployed it to Hugging Face Spaces so anyone can try it instantly.

## Why I built it
I wanted a lightweight assistant that keeps fitness advice clear and supportive without the fluff, and to learn the Gradio + Groq + HF Spaces stack end-to-end.

## What’s inside
- 🎚️ Tone control: pick Direct, Friendly, or Detailed responses.
- 💬 Chat history-aware answers via Groq chat completions.
- 🌐 Deployed on Hugging Face Spaces (Groq key stored as a secret).

## Try it live
- Hugging Face Space: https://huggingface.co/spaces/mianxabdullah/fitness_chatbot 
  Open it, pick a tone, ask a question, and see it respond in real time.

## 📂 Files
- `app.py` — Gradio UI + Groq chat logic.
- `requirements.txt` — dependencies.

## How it works (brief)
- `app.py` wires the Gradio Blocks UI to the Groq chat completions endpoint (`llama-3.1-8b-instant`).
- Chat state is passed to Groq so replies stay in context.
- `requirements.txt` keeps dependencies minimal (Gradio, requests).

## Dev quickstart (if you want to run it)
- `pip install -r requirements.txt`
- Set `GROQ_API_KEY`
- `python app.py`

## Notes
- If a model is ever deprecated, swap `MODEL_NAME` in `app.py` to a current Groq model (e.g., `llama-3.1-70b-versatile`).
- The tone dropdown is the UI tweak for the lab requirement; feel free to extend it (e.g., sliders for verbosity).
