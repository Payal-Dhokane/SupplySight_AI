def inventory_action(row):
    if row["shock"] and row["z_score"] > 0:
        return "Increase inventory (demand spike)"
    elif row["shock"] and row["z_score"] < 0:
        return "Reduce inventory (demand drop)"
    else:
        return "No action"
