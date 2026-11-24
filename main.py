"""Letting Go of the Rope: one line of earned pride.

The program writes one line of text, a single sentence of at most 240
characters (161 characters), to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR
locally, /output in the grader). The text is a fixed constant with no
trailing newline, so both of the grader's runs write byte-identical output.
"""
import os

LINE = "Her grandfather had rowed her out every dawn for a year; this morning she took the oars, cut straight through the harbour chop, and he simply let go of the rope."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
