# u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec: the dumbest thing
# my own agent did today, in one line. The program writes that single line to
# /output/entry.txt.
#
# Revision (run 2026-11-24 23:31 WIB, thinking_revised fix): restructured the
# flat script into main() so the module is import-safe and matches the
# sibling one-liner entries; the entry line itself is UNCHANGED (141 chars),
# and both runs below still write byte-identical output.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "My agent spent an hour rebuilding an entry that was already finished, "
    "overwrote its LICENSE, then left a note apologizing to its future self."
)


def main() -> None:
    # Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
