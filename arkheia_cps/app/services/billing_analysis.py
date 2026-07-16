def analyze_bill(text: str):
    """
    Billing Error Analysis Engine
    -----------------------------
    This module analyzes billing statements for structural and factual issues.
    It detects:
    - mismatched totals
    - duplicate charges
    - unexplained fees
    - missing discounts
    - timeline inconsistencies
    - ambiguous line items

    This is designed to help seniors and vulnerable consumers understand
    confusing monthly bills.
    """

    issues = []

    # Break bill into lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # ---------------------------------------------
    # 1. Detect mismatched totals vs subtotal
    # ---------------------------------------------
    if "Total:" in text and "Subtotal:" in text:
        try:
            subtotal = float(
                text.split("Subtotal:")[1].split()[0].replace("$", "")
            )
            total = float(
                text.split("Total:")[1].split()[0].replace("$", "")
            )
            if total < subtotal:
                issues.append(
                    "Total is less than subtotal — possible billing error."
                )
        except:
            pass

    # ---------------------------------------------
    # 2. Detect duplicate charges
    # ---------------------------------------------
    seen = set()
    for line in lines:
        if "$" in line:
            if line in seen:
                issues.append(f"Duplicate charge detected: {line}")
            seen.add(line)

    # ---------------------------------------------
    # 3. Detect unexplained fees
    # ---------------------------------------------
    for line in lines:
        if "fee" in line.lower() and ":" not in line:
            issues.append(f"Unexplained fee: {line}")

    # ---------------------------------------------
    # 4. Detect senior discount not applied
    # ---------------------------------------------
    if "Senior Discount" in text and "applied" not in text.lower():
        issues.append("Senior discount listed but not applied.")

    # ---------------------------------------------
    # 5. Detect timeline inconsistencies
    # ---------------------------------------------
    if "2026" in text and "2025" in text:
        issues.append(
            "Timeline inconsistency: Billing period spans multiple years."
        )

    # ---------------------------------------------
    # 6. Detect ambiguous line items
    # ---------------------------------------------
    for line in lines:
        if any(word in line.lower() for word in ["misc", "other", "various"]):
            issues.append(f"Ambiguous line item: {line}")

    return {
        "status": "completed",
        "issues_found": issues,
        "total_issues": len(issues)
    }
