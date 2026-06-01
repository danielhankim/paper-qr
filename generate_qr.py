import argparse
import sys
from pathlib import Path
import qrcode


def generate_qr(url: str, output: str) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)
    print(f"QR code saved to {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code for a paper URL")
    parser.add_argument("url", help="URL of the paper")
    parser.add_argument(
        "-o", "--output",
        default="qr_code.png",
        help="Output file path (default: qr_code.png)",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    if output_path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".bmp", ".gif"}:
        print(f"Warning: unusual file extension '{output_path.suffix}', defaulting to .png")
        output_path = output_path.with_suffix(".png")

    generate_qr(args.url, str(output_path))


if __name__ == "__main__":
    main()
