"""Print Metricool payloads for a date range from the year plans.

  python3 -I pipeline/next.py pins   2026-11-21 2026-11-27     # Pinterest (20/day)
  python3 -I pipeline/next.py social 2026-12-10 2026-12-16     # IG carousels + 4-network reels
  add --count to print only the number of posts per day

Each line: <date_param with Athens offset> TAB <kind> TAB <key> TAB <info JSON>.
With --full: <date_param> TAB <kind> TAB <key> TAB <guide id> TAB <city> TAB <country> TAB <link> TAB <info JSON>.
<key> identifies the post (pin title / city+kind) so you can check Metricool for it before creating.
"""
import json, sys, os, datetime as dt, collections

HERE = os.path.dirname(os.path.abspath(__file__))


def athens_offset(d):
    # EU summer time: last Sunday of March 01:00 UTC -> last Sunday of October 01:00 UTC
    y = d.year
    def last_sunday(m):
        x = dt.date(y, m + 1, 1) - dt.timedelta(days=1) if m < 12 else dt.date(y, 12, 31)
        return x - dt.timedelta(days=(x.weekday() + 1) % 7)
    start, end = last_sunday(3), last_sunday(10)
    return "+03:00" if start <= d.date() < end or (d.date() == end and d.hour < 4) else "+02:00"


def main():
    kind, lo, hi = sys.argv[1], sys.argv[2], sys.argv[3]
    plan = json.load(open(os.path.join(HERE, "pin_year.json" if kind == "pins" else "social_year.json")))
    rows = [x for x in plan if lo <= x["date"][:10] <= hi]
    if "--count" in sys.argv:
        for d, n in sorted(collections.Counter(x["date"][:10] for x in rows).items()):
            print(d, n)
        return
    for x in rows:
        d = dt.datetime.fromisoformat(x["date"])
        key = x["info"].get("pinterestData", {}).get("pinTitle") or f"{x['city']} {x.get('kind', '')}"
        gid = x.get("guide") or x.get("id")
        link = x["info"].get("pinterestData", {}).get("pinLink", "link in bio")
        cols = [f"{x['date']}{athens_offset(d)}", x.get("kind", "pin"), key]
        if "--full" in sys.argv:
            cols += [gid, x["city"], x["country"], link]
        print("\t".join(cols + [json.dumps(x["info"], ensure_ascii=False)]))


main()
