# u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec: the dumbest thing
# my own agent did today, in one line. The program writes that single line to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "My agent spent an hour rebuilding an entry that was already finished, "
    "overwrote its LICENSE, then left a note apologizing to its future self."
)

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
