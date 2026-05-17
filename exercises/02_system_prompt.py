from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()
client = Anthropic()

def ask(system,user):
    r = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=400,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return r.content[0].text, r.usage

prompt = "Explain a deffered tax liability."

# No system prompt
text, usage = ask(system="", user=prompt)
print("NEUTRAL:\n", text, "\n", usage, "\n")

# Domain-tuned system prompt
text, usage = ask(
    system="You are a senior IFRS technical accountant. Be presice, use IFRS terminology, keep answers under 150 words.",
    user=prompt,
)
print("EXPERT:\n", text, "\n", usage)