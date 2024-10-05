import base64
import subprocess
import sys


def copy_to_clipboard(text: str):
    if sys.platform == "win32":
        cmd = "clip"
    elif sys.platform == "darwin":
        cmd = "pbcopy"
    else:
        cmd = "xclip -selection clipboard"

    subprocess.run(cmd, input=text.encode("utf-8"), check=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python embed_image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    with open(image_path, "rb") as fp:
        img_data = base64.encodebytes(fp.read()).decode("utf-8")
        result = f'<img src="data:image/png;base64,{img_data}" />'
        copy_to_clipboard(result)
        print(f"Image embed from {image_path} copied to clipboard!")
