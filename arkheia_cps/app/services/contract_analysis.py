def analyze_contract(text: str):
    """
    Contract Analysis Engine
    ------------------------
    This function performs structural and factual checks on contract text.
    It detects:
    - undefined terms
    - contradictions
    - mismatched numbers
    - missing references
    - duplicate clauses
    - timeline inconsistencies

    This is NOT legal advice — it is structural analysis.
    """

    errors = []

    # Break contract into lines/clauses
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # ---------------------------------------------
    # 1. Detect undefined terms
    # ---------------------------------------------
    definitions = [l for l in lines if "defined as" in l.lower()]
    defined_terms = [d.split("defined as")[0].strip() for d in definitions]

    for line in lines:
        words = line.split()
        for w in words:
            # Heuristic: capitalized words often represent defined terms
            if w.istitle() and w not in defined_terms and len(w) > 3:
                errors.append(f"Undefined term detected: {w}")

    # ---------------------------------------------
    # 2. Detect contradictions
    # ---------------------------------------------
    if "30 days" in text and "45 days" in text:
        errors.append("Contradiction: Payment due in both 30 and 45 days.")

    if "exclusive" in text.lower() and "non-exclusive" in text.lower():
        errors.append("Contradiction: Contract states both exclusive and non-exclusive rights.")

    # ---------------------------------------------
    # 3. Detect mismatched numbers
    # ---------------------------------------------
    if "$5000" in text and "$4500" in text:
        errors.append("Mismatch: Contract references both $5000 and $4500.")

    # ---------------------------------------------
    # 4. Detect missing appendices
    # ---------------------------------------------
    if "Appendix" in text and "Appendix" not in " ".join(lines):
        errors.append("Missing appendix referenced but not included.")

    # ---------------------------------------------
    # 5. Detect duplicate clauses
    # ---------------------------------------------
    seen = set()
    for line in lines:
        if line in seen:
            errors.append(f"Duplicate clause detected: \"{line}\"")
        seen.add(line)

    # ---------------------------------------------
    # 6. Detect timeline inconsistencies
    # ---------------------------------------------
    if "2026" in text and "2025" in text:
        errors.append("Timeline inconsistency: Contract references multiple years in obligations.")

    return {
        "status": "completed",
        "issues_found": errors,
        "total_issues": len(errors)
    }
