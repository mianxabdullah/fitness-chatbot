import os
import requests
import gradio as gr

# Set your unique bot theme/personality here
SYSTEM_PROMPT = """You are FitBuddy, a friendly fitness coach.
Provide clear, encouraging guidance on workouts, recovery, and nutrition.
Be concise, practical, and safety-conscious; avoid medical advice beyond general wellness tips."""

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"
def query_groq(message: str, chat_history: list, style: str):
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY is not set in environment."
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    style_prefix = {
        "Direct": "Keep answers brief and to the point.",
        "Friendly": "Keep answers warm, upbeat, and supportive.",
        "Detailed": "Provide more elaboration and examples, but stay concise.",
    }.get(style, "")
    messages = [{"role": "system", "content": f"{SYSTEM_PROMPT}\n{style_prefix}"}]
    messages.extend(chat_history or [])
    messages.append({"role": "user", "content": message})

    resp = requests.post(
        GROQ_API_URL,
        headers=headers,
        json={"model": MODEL_NAME, "messages": messages, "temperature": 0.7},
        timeout=30,
    )
    if resp.status_code == 200:
        return resp.json()["choices"][0]["message"]["content"]
    return f"Error {resp.status_code}: {resp.text}"

def respond(message, chat_history, style):
    chat_history = chat_history or []
    reply = query_groq(message, chat_history, style)
    chat_history = chat_history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": reply},
    ]
    return "", chat_history

with gr.Blocks(title="FitBuddy - Fitness Coach") as demo:
    gr.Markdown("## 🏋️ FitBuddy (Groq + Gradio)")
    with gr.Row():
        style = gr.Dropdown(
            choices=["Direct", "Friendly", "Detailed"],
            value="Friendly",
            label="Tone",
        )
        clear = gr.Button("Clear Chat")
    chatbot = gr.Chatbot(height=400)  # default message dict format
    msg = gr.Textbox(label="Ask a fitness question")

    state = gr.State([])

    msg.submit(respond, [msg, state, style], [msg, chatbot])
    clear.click(lambda: ([], []), None, [chatbot, state])

if __name__ == "__main__":
    demo.launch()