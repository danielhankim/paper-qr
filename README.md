# paper-qr

Generate a QR code for a paper URL.

## Setup

```bash
uv sync
```

## Usage

```bash
uv run generate_qr.py <URL> [-o output.png]
```

**Example:**

```bash
uv run generate_qr.py "https://journals.aps.org/pre/abstract/10.1103/pk8t-px35"
```

Saves `qr_code.png` by default. Use `-o` to specify a custom output path.
