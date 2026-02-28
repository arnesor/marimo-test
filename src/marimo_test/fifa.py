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

    This is a test of visualizing a pandas dataframe with marimo.
    """)
    return


@app.cell
def _(mo, pd):
    def read_fifa_data() -> pd.DataFrame:
        # Assuming the CSV file is in the same directory as this script
        file = mo.notebook_location() / "public" / "cleaned_fifa21.csv"
        df = pd.read_csv(file)
        print(df.shape)
        print(df.columns)
        return df[
            [
                "Name",
                "Nationality",
                "Age",
                "Club",
                "↓OVA",
                "POT",
                "BOV",
                "Total Stats",
                "Base Stats",
                "Value",
                "Wage",
                "Sprint Speed",
                "Shot Power",
                "Interceptions",
                "Finishing",
                "Defending",
                "Hits",
            ]
        ]

    return


@app.cell
def _(mo, pd):
    @mo.cache
    def fetch_player_data():
        # A cleaned version where 'Value' and 'Wage' are already converted to floats
        url = "https://raw.githubusercontent.com/Dorianteffo/fifa21_datacleaning_python/main/cleaned_fifa21.csv"
        print(f"Fetching data from {url}...")
        # pd.read_csv() works with URLs in both regular Python and in Pyodide/WASM
        df = pd.read_csv(url)
        return df[
            [
                "Name",
                "Nationality",
                "Age",
                "Club",
                "↓OVA",
                "POT",
                "BOV",
                "Total Stats",
                "Base Stats",
                "Value",
                "Wage",
                "Sprint Speed",
                "Shot Power",
                "Interceptions",
                "Finishing",
                "Defending",
                "Hits",
            ]
        ]


    return (fetch_player_data,)


@app.cell
def _(fetch_player_data):
    print("Reading FIFA data...")
    # df = read_fifa_data()
    df = fetch_player_data()

    print("Fifa data loaded successfully.")
    df
    return


if __name__ == "__main__":
    app.run()
