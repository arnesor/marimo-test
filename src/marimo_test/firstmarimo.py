import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    import httpx
    from io import BytesIO
    import plotly.express as px
    return BytesIO, httpx, mo, pl, px


@app.cell
def _(mo):
    mo.md("""
    # 📊 FIFA 2021 player data
    """)
    return


@app.cell
def _(BytesIO, httpx, mo, pl):
    @mo.cache
    def fetch_player_data():
        # A cleaned version where 'Value' and 'Wage' are already converted to floats
        url = "https://raw.githubusercontent.com/Dorianteffo/fifa21_datacleaning_python/main/cleaned_fifa21.csv"
        response = httpx.get(url)

        # We use Polars to load it and select the 'core' numerical stats
        return pl.read_csv(BytesIO(response.content)).select([
            "Name", "Nationality", "Age", "Club", "↓OVA", "POT", "BOV",
            "Total Stats", "Base Stats",
            "Value", "Wage", "Sprint Speed", "Shot Power", 
            "Interceptions", "Finishing", "Defending", "Hits"
        ])

    df = fetch_player_data()
    df
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Speed vs finishing accuracy

    The graph shows:

    **X-axis** *Sprint speed*: The maximum top speed a player can reach once they are fully into their stride.<br>
    **Y-axis** *Finishing:* Measures a player's accuracy with shots inside the penalty area.<br>
    **Point Size:** Determined by value (bigger circle = more expensive).<br>
    **Point Color:** Determined by overall rating, OVA (Brighter/Different color = Higher current rating)<br>
    """)
    return


@app.cell
def _(mo):
    speed_slider = mo.ui.slider(0, 100, label="Min Sprint Speed", value=70)
    finishing_slider = mo.ui.slider(0, 100, label="Min Finishing", value=60)

    # Sliders for the graph below
    mo.hstack([speed_slider, finishing_slider])
    return finishing_slider, speed_slider


@app.cell
def _(df, finishing_slider, mo, pl, px, speed_slider):
    def render_scouting_chart(data):
        filtered_df = data.filter(
            (pl.col("Sprint Speed") >= speed_slider.value) & 
            (pl.col("Finishing") >= finishing_slider.value)
        )

        if filtered_df.is_empty():
            return mo.md("### ⚠️ No players match these criteria.")

        fig = px.scatter(
            filtered_df,
            x="Sprint Speed",
            y="Finishing",
            size="Value", 
            color="↓OVA",
            hover_name="Name",
            # Including your requested columns in hover data
            hover_data=["Club", "Age", "POT", "BOV", "Wage"],
            title="Sprint Speed vs. Finishing",
            template="plotly_dark",
            color_continuous_scale="Viridis"
        )

        return mo.ui.plotly(fig)

    render_scouting_chart(df)
    return


if __name__ == "__main__":
    app.run()
