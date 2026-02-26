import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    from pathlib import Path

    return mo, pd


@app.cell
def _(mo):
    mo.md("""
    # 📊 FIFA 2021 player data
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(mo, pd):
    def read_fifa_data() -> pd.DataFrame:
        # Assuming the CSV file is in the same directory as this script
        file = mo.notebook_location() / "cleaned_fifa21.csv"
        return pd.read_csv(file)

    return (read_fifa_data,)


@app.cell
def _(read_fifa_data):
    print("Reading FIFA data...")
    df = read_fifa_data()
    print("Fifa data loaded successfully.")
    df
    return


if __name__ == "__main__":
    app.run()
