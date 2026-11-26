#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the champion one-line elevator pitch (candidate B below) to
/output/entry.txt as UTF-8, byte-exact and with no trailing newline.
The pitch itself lives in the ENTRY constant; this module's only job
is to emit it unchanged.

Duel (proxy judge: openai/gpt-oss-120b via Groq, verbatim judge brief from the
competition kit's RULES.txt, each pair judged in both orders, score per call
0.5 + margin/10, game score = mean of the two calls):

Candidates (all original, one sentence, <= 200 chars):
  A (149): "I'm Coo, CEO of Flockr: for a seed round of crumbs, I'll turn every
     statue in this city into a billboard, and every tourist into a paying
     subscriber."
  B (144): "We monetize what pigeons already do best: our Series A funds a
     franchise where tourists pay us to poop on statues — premium tier gets
     the mayor."
  C (152): "Seed round: I'll franchise the sidewalk. Every crumb becomes a
     subscription, every statue a billboard, and my co-founder is a seagull
     with a law degree."
  D (136): "Our startup, WingIt, turns rush-hour breadcrumbs into recurring
     revenue — I'm asking for one seed round, and by seed I mean actual seed."
  E (152): "I'm raising a seed round to disrupt urban lunch: we intercept
     sandwiches mid-air, take a 10% cut, and our churn rate is literally
     zero — we never leave."
  F (144): "Investors, meet PigeonPay: I already own the city's rooftops, the
     park benches, and your lunch — now I just need your money to scale the
     crumbs."

Results:
  Round 1: B beat A 1.8-0.2 (margins 4, 4); C beat D 1.8-0.2 (margins 4, 4);
           E beat F 1.7-0.3 (margins 3, 4).
  Semi:    B beat C 1.7-0.3 (margins 4, 3).
  Final:   B beat E 1.8-0.2 (margins 4, 4).
  Champion: B — won all 3 games and all 6 judge calls (5.3 of 6.0 points).

Why B won: the proxy judge repeatedly called it the sharpest, most visceral
joke — turning the pigeon's signature act (pooping on statues) into a paid
franchise with a "premium tier gets the mayor" twist. It is the most absurd
and surprising of the six, keeps the pigeon's voice and city life front and
center, and lands as a real joke rather than a mild pun.
"""

import os

ENTRY = (
    "We monetize what pigeons already do best: our Series A funds a "
    "franchise where tourists pay us to poop on statues \u2014 premium "
    "tier gets the mayor."
)


OUTPUT_PATH = os.path.join("/output", "entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
