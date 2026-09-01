"""Expense reporting."""
 
TOTALS = {}


def _parse_and_filter(rows, category):
    parsed = []
    for r in rows:
        if len(r) != 3:
            continue
        try:
            amount = float(r[1])
        except ValueError:
            continue
        if amount < 0:
            continue
        parsed.append({"name": r[0], "amount": amount, "category": r[2]})

    if category is not None:
        kept = []
        for p in parsed:
            if p["category"] == category:
                kept.append(p)
        parsed = kept

    return parsed


def generate_report(rows, category=None, include_tax=True):
    parsed = _parse_and_filter(rows, category)

    total = 0.0
    for p in parsed:
        if include_tax:
            total = total + p["amount"] * 1.2
        else:
            total = total + p["amount"]
    TOTALS[category or "all"] = total
 
    lines = ["EXPENSE REPORT", "--------------"]
    for p in parsed:
        if include_tax:
            lines.append(p["name"] + ": " + str(round(p["amount"] * 1.2, 2)))
        else:
            lines.append(p["name"] + ": " + str(round(p["amount"], 2)))
    lines.append("TOTAL: " + str(round(total, 2)))
    return "\n".join(lines)
 
 
def generate_summary(rows, category=None, include_tax=True):
    parsed = _parse_and_filter(rows, category)

    total = 0.0
    for p in parsed:
        if include_tax:
            total = total + p["amount"] * 1.2
        else:
            total = total + p["amount"]
 
    return str(len(parsed)) + " items, total " + str(round(total, 2))
