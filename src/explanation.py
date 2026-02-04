def explain_decision(row):
    if row["shock"] and row["onpromotion"] == 1:
        return "Demand spike likely due to promotion"
    elif row["shock"]:
        return "Unusual demand detected without promotion"
    else:
        return "Normal demand pattern"
