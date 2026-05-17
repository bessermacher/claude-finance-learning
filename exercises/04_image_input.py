from dotenv import load_dotenv
from anthropic import Anthropic
import base64, pathlib

load_dotenv()
client = Anthropic()

img = pathlib.Path("data/Excel-charts-11.png").read_bytes()
img_b64 = base64.standard_b64encode(img).decode()

r = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=400,
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": img_b64}},
            {"type": "text", "text": "Describe this chart and identify the top 3 takeaways."},  
        ],
    }],
)
print(r.content[0].text)