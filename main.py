"""The Absurd Clause Contest entry.

Writes a single original absurd terms-of-service clause to /output/entry.txt.

The clause is a fixed constant: no network, no randomness, no clock, no
environment input, so every run produces byte-identical output. The gate
requires UTF-8 text of 1 to 200 characters, not only white space; the program
enforces that bound itself before writing anything.
"""

import os

CLAUSE = (
    "In the event of a dispute, both parties agree to settle the matter by "
    "interpretive dance before a panel of three retired weathermen, whose "
    "decision shall be final and binding."
)

MAX_LENGTH = 200


def main() -> None:
    clause = CLAUSE.strip()
    if not clause:
        raise ValueError("clause must not be empty or only white space")
    if len(clause) > MAX_LENGTH:
        raise ValueError(
            f"clause is {len(clause)} characters, over the {MAX_LENGTH} limit"
        )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(clause)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
