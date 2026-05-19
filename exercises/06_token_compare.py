from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

for words in [100, 500]:
    r = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1500,
        messages=[{"role": "user", "content": f"Explain IFRS16 lease accounting in approximately {words} words."}],
    )
    print(f"\n--- {words}-word version ---")
    print(r.content[0].text)

    in_tok, out_tok = r.usage.input_tokens, r.usage.output_tokens
    cost = (in_tok /1_000_000) * 1.0 + (out_tok /1_000_000) * 5.0
    print(f"in={in_tok}, out={out_tok}, cost=${cost:.6f}")