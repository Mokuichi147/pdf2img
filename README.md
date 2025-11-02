# pdf2img

pdfを画像に変換します

```shell
$ pdf2img --help                                            
usage: pdf2img [-h] [--out OUT] [--dpi DPI] pdf

Convert PDF pages to images (pure Python, no external deps)

positional arguments:
  pdf         Path to input PDF file

options:
  -h, --help  show this help message and exit
  --out OUT   Output directory (default: out)
  --dpi DPI   Image DPI (default: 200)
```

## コマンド例

```shell
uvx --from git+https://github.com/mokuichi147/pdf2img pdf2img document.pdf --out output --dpi 300
```


### インストールする場合

```shell
uv tool install git+https://github.com/mokuichi147/pdf2img
pdf2img document.pdf --out output --dpi 300
```

アンインストール

```shell
uv tool uninstall pdf2img
```
