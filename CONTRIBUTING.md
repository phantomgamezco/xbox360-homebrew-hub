# Contributing

Thanks for helping improve Xbox 360 Homebrew Hub. Keep contributions focused, documented, and based on verifiable Free60 libxenon behavior.

## Safety and project policy

- Use only the open-source [Free60 libxenon project](https://github.com/Free60Project/libxenon) for Xbox 360 homebrew builds. Do not reference, link, include, or depend on proprietary console SDKs or leaked SDK files.
- Do not submit or link piracy tools, copyrighted game assets, console keys, firmware dumps, or other proprietary console data.
- Homebrew from this project is intended only for compatible modified consoles (for example RGH/JTAG setups). Do not claim it runs on stock retail consoles.
- Do not claim emulator support. Real compatible hardware is the test target.
- Do not invent libxenon APIs, headers, or compiler flags. Link upstream documentation/example evidence for API claims; mark unverified code with `TODO(verify)`.

## Gallery submissions

Update `gallery/apps.json` with an app name, author, public repository URL, short description, and tested hardware details. Do not list binaries hosted outside GitHub Releases or GitHub Actions artifacts. Keep descriptions factual and free of copyrighted material. The gallery validation workflow must pass.

## Changes and checks

For documentation changes:

```sh
python -m pip install -r requirements-docs.txt
python scripts/render_gallery.py
mkdocs build --strict
```

For gallery changes, validate the JSON with the workflow or run:

```sh
python -m pip install jsonschema==4.23.0
python -m json.tool gallery/apps.json >/dev/null
python -c 'import json; from jsonschema import validate; validate(json.load(open("gallery/apps.json")), json.load(open("gallery/apps.schema.json")))'
```

For app or toolchain changes, explain what was built and tested. Hardware test reports should identify the console setup and should not imply testing on unmodified hardware.
