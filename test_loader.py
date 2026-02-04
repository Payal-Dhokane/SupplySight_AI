from src.data_loader import load_data
from src.shock_detection import detect_shocks

df = load_data()

# filter one store + one product family
df = df[(df["store_nbr"] == 1) & (df["family"] == "AUTOMOTIVE")]

# create artificial shock for demo
df.loc[df.index[-3], "sales"] = df["sales"].mean() * 5


df = detect_shocks(df)

print(df[["date", "sales", "onpromotion", "z_score", "shock"]].tail(15))

from src.inventory_decision import inventory_action

df["action"] = df.apply(inventory_action, axis=1)

print(df[["date", "sales", "z_score", "shock", "action"]].tail(10))
