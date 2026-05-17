from dotenv import load_dotenv
from anthropic import Anthropic
import base64, pathlib

load_dotenv()
client = Anthropic()

doc = pathlib.Path("data/ifrs16_summary.txt").read_text()
r = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=500,
    messages=[{"role": "user", "content": f"<doc>\n{doc}\n</doc>\n\nList the 5 main accounting requirements from the document above"}],
)
print(r.content[0].text)
print(r.usage)