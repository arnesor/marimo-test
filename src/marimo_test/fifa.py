import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # 📊 FIFA 2021 player data

    This is a test of visualizing a pandas dataframe with marimo.
    The notebook can also be published to html using the command:

    `uv run marimo export html-wasm ./src/marimo_test/fifa.py -o html --mode run`.

    Then the python code is run inside the web browser using Pyodide/WASM.
    See https://arnesor.github.io/marimo-test/ for the published html version.
    """)
    return


@app.cell
def _(pd):
    def filter_fifa_data(df: pd.DataFrame) -> pd.DataFrame:
        """Extract the relevant columns."""
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
        """Read FIFA data from a local file.

        The data files must be stored in a subdirectory called `public` to be
        available when published to html.

        When running in a web browser on GitHub pages, the normal file access does not work.
        The workaround is to load the content of the file using open_url.
        """
        filename = "cleaned_fifa21.csv"
        try:
            from pyodide.http import open_url

            csv_source = open_url(f"../public/{filename}")
        except ImportError:
            csv_source = mo.notebook_location() / "public" / filename
        df = pd.read_csv(csv_source)
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

    return


@app.cell
def _(read_fifa_data_from_file):
    print("Reading FIFA data...")
    # df = read_fifa_data_from_web()
    df = read_fifa_data_from_file()

    print("Fifa data loaded successfully.")
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Select columns
    """)
    return


@app.cell
def _(mo):
    economics_checkbox = mo.ui.checkbox(value=False, label="Economics")
    abilities_checkbox = mo.ui.checkbox(value=False, label="Abilities")
    mo.vstack([economics_checkbox, abilities_checkbox])
    return abilities_checkbox, economics_checkbox


@app.cell
def _(abilities_checkbox, df, economics_checkbox):
    base_columns = ["Name", "Nationality", "Age", "Club", "Total Stats"]
    economics_columns = ["Value", "Wage"]
    abilities_columns = [
        "Sprint Speed",
        "Shot Power",
        "Interceptions",
        "Finishing",
        "Defending",
        "Hits",
    ]
    selected_columns = base_columns
    if economics_checkbox.value:
        selected_columns.extend(economics_columns)
    if abilities_checkbox.value:
        selected_columns.extend(abilities_columns)
    df[selected_columns]
    return


if __name__ == "__main__":
    app.run()
