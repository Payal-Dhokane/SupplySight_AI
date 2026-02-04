import pandas as pd

def detect_shocks(df, window=7, threshold=2):
    df = df.sort_values("date")

    df["rolling_mean"] = df["sales"].rolling(window).mean()
    df["rolling_std"] = df["sales"].rolling(window).std()

    df["z_score"] = (df["sales"] - df["rolling_mean"]) / df["rolling_std"]

    df["shock"] = df["z_score"].abs() > threshold

    return df
