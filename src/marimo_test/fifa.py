import marimo

__generated_with = "0.20.2"
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
def _(pd):
    def filter_fifa_data(df: pd.DataFrame) -> pd.DataFrame:
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

    return (filter_fifa_data,)


@app.cell
def _(filter_fifa_data, mo, pd):
    def read_fifa_data_from_file() -> pd.DataFrame:
        # The data files must be stored in a subdirectory called `public` to be available when published to html
        file = mo.notebook_location() / "public" / "cleaned_fifa21.csv"
        df = pd.read_csv(file)
        return filter_fifa_data(df)

    return (read_fifa_data_from_file,)


@app.cell
def _(filter_fifa_data, mo, pd):
    @mo.cache
    def read_fifa_data_from_web():
        url = "https://raw.githubusercontent.com/Dorianteffo/fifa21_datacleaning_python/main/cleaned_fifa21.csv"
        print(f"Fetching data from {url}...")
        # pd.read_csv() works with URLs in both regular Python and in Pyodide/WASM
        df = pd.read_csv(url)
        return filter_fifa_data(df)

    return (read_fifa_data_from_web,)


@app.cell
def _(read_fifa_data_from_file, read_fifa_data_from_web):
    print("Reading FIFA data...")
    df = read_fifa_data_from_web()
    df = read_fifa_data_from_file()

    print("Fifa data loaded successfully.")
    df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
