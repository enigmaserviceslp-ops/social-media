# Steal My Guide social plan, Oct 2026 – Oct 2027

- `pin_year.json`: 7,300 Pinterest pins, 20 a day from 31 Oct 2026 to 30 Oct 2027 (09:00–21:40 Athens, every 40 min).
  Images in `pinterest/year/`. Every hook comes from the guide preview or the guide's own subtitle; no city twice in a day,
  the same guide at least 14 days apart; each hook runs in two layouts months apart.
- `social_year.json`: Instagram carousels (12:30) and reels (18:30, Instagram, Facebook, TikTok, YouTube Shorts),
  10 Dec 2026 to 30 Oct 2027. Reels run 3 days after their carousel. Media in `instagram/year/` and `reels/year/`.
- `next.py`: prints the Metricool payloads for a date range (`pins` or `social`).

A scheduled task ("Steal My Guide weekly social top-up", Mondays 08:54 Athens) creates whatever is missing:
pins 28 days ahead, social 42 days ahead, and logs each post in the "SMG posting log" sheet.
