# Xbox 360 Homebrew Hub

A community hub for building original Xbox 360 homebrew with the open-source [Free60 libxenon](https://github.com/Free60Project/libxenon) toolchain. It includes a MkDocs documentation site, a minimal starter app, a containerized toolchain, CI build artifacts, and a small community gallery.

> **Hardware:** Homebrew built here runs only on compatible modified Xbox 360 consoles (such as RGH/JTAG setups). It does not run on stock retail consoles. Real hardware is the test target; emulator compatibility is not claimed.

## Quick start

1. Read [hardware requirements](docs/hardware-requirements.md) and [getting started](docs/getting-started.md).
2. Copy the contents of [`template/`](template/) into a new repository, or clone this repository and work in `template/`.
3. Push your app to GitHub. The root-level template workflow builds it with the published GHCR image and uploads `hello.elf32` as an Actions artifact.
4. Copy the artifact to FAT32 media and launch it on compatible homebrew-capable hardware using XeLL.

The toolchain image is built from the official Free60Project/libxenon source and its documented `build-xenon-toolchain` script. This project does not include proprietary console SDKs, keys, firmware dumps, game assets, or piracy tools.

## Documentation

Install Python dependencies and build the site locally:

```sh
python -m pip install -r requirements-docs.txt
python scripts/render_gallery.py
mkdocs serve
```

GitHub Pages deploys the MkDocs site from `main` after the Pages environment is configured for GitHub Actions.

## Build the toolchain image locally

From the repository root:

```sh
docker build -f toolchain/Dockerfile -t xbox360-homebrew-toolchain .
```

The upstream cross-compiler and library build is substantial and needs network access. The workflow publishes `ghcr.io/phantomgamezco/xbox360-homebrew-hub/libxenon-toolchain:latest` after changes to `toolchain/`.

## Verification

```sh
python scripts/render_gallery.py
python -m json.tool gallery/apps.json >/dev/null
python -m json.tool gallery/apps.schema.json >/dev/null
python -m pip install -r requirements-docs.txt
mkdocs build --strict
```

For a hardware test, build the template using the documented workflow, transfer the `.elf32` artifact to FAT32 media, and launch it on a compatible modified Xbox 360. This project does not claim Xenia or other emulator support.

## License

No license has been selected or included. Until a license is added, do not assume the project may be redistributed under an open-source license.
