"""convertor light"""

from pathlib import Path
from time import sleep

from PIL import Image
from rich.console import Console
from tqdm import tqdm

console: Console = Console()


def load_files() -> list:
    """Load files"""
    files: list = []
    for file in Path(".").iterdir():
        if file.is_file() and file.suffix in {".jpeg", ".jpg"}:
            files.append(file)
    if not files:
        console.print("No files to convert", style="red")
        sleep(2)
        exit(0)
    else:
        console.print(f"Number of files: {len(files)}.", style="green")

    return files


def convertor(file_list: list, compress: int = 80) -> None:
    """Convertor"""
    try:
        for file in tqdm(
            file_list,
            desc="Converting",
            dynamic_ncols=True,
            bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} - Remaining:{" "remaining}",
            leave=True,
            unit="img",
            unit_scale=True,
            smoothing=0.1,
        ):
            sleep(0.1)
            with Image.open(file) as jpeg_image:
                temp = file.stem
                jpeg_image.save(
                    Path(".") / f"{temp}.webp", format="WEBP", quality=compress
                )

    except ValueError as e:
        console.print("Error", e, style="red")
        console.print("Closing program", style="green")
        sleep(3)
        exit(0)


def main() -> None:
    """Main function"""
    console.clear()
    files: list = load_files()
    compress_input: str = input("Enter compression level (0 - 100%) default(80%): ")
    compress:int = 80 if compress_input == '' else int(compress_input)
    convertor(files, compress)
    console.print("-- Done --", style="bold blue")
    sleep(3)


if __name__ == "__main__":
    main()
