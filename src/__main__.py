import argparse
from pathlib import Path
from rich.console import Console
import fitz

console = Console()

def convert(pdf_path: Path, out_dir: Path, dpi: int):
    if not pdf_path.exists():
        console.print(f"[red]Error:[/red] File not found: {pdf_path}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    console.print(f"[bold green]Converting:[/bold green] {pdf_path}")

    pdf = fitz.open(pdf_path)
    for i, page in enumerate(pdf, start=1):
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        out_file = out_dir / f"page_{i:03d}.png"
        pix.save(out_file)
        console.print(f"  Saved: {out_file}")

    console.print(f"[bold cyan]Done![/bold cyan] {len(pdf)} pages converted → {out_dir}")

def main():
    parser = argparse.ArgumentParser(description="Convert PDF pages to images (pure Python, no external deps)")
    parser.add_argument("pdf", help="Path to input PDF file")
    parser.add_argument("--out", default="out", help="Output directory (default: out)")
    parser.add_argument("--dpi", type=int, default=200, help="Image DPI (default: 200)")
    args = parser.parse_args()

    convert(Path(args.pdf), Path(args.out), args.dpi)

if __name__ == "__main__":
    main()
