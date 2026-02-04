def forecast_sales(df, days=7):
    """
    Simple rolling-average based forecast
    """

    last_avg = df["sales"].tail(7).mean()

    forecast = [round(last_avg, 2)] * days
    return forecast
