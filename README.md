# marimo-test
Test of marimo notebooks.

## Usage

```shell
uv run marimo edit src/marimo_test/fifa.py
```

## Export to html

```shell
uv run marimo export html-wasm .\src\marimo_test\fifa.py -o html --mode run
```

### Test the html file

```shell
uv run py -m http.server --directory html
```

And open web browser at `http://localhost:8000`.

