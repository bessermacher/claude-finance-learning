from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()
client = Anthropic()

history = []

def chat(user_msg, system="You are a helpful FP&A analyst."):
    history.append({"role": "user", "content": user_msg})
    r = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=400,
        system=system,
        messages=history,
    )
    assistant_msg = r.content[0].text
    history.append({"role": "assistant", "content": assistant_msg})
    return assistant_msg

print(chat("I have a EUR 1.2M unfavourable variance in IT_COSTS for Q1."))
print(chat("What three questions should I ask the cost center owner?"))
print(chat("Now draft a one-paragraph email to them."))