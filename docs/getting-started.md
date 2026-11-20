# Getting started

This guide builds the starter app with GitHub Actions and describes the documented transfer path for compatible modified hardware.

## 1. Create your app repository

Use **Use this template** if enabled, or copy this repository's `template/` directory into a new GitHub repository. The app source is `src/main.c`. The root-level workflow for this hub is `.github/workflows/template-build.yml`; when using the template in a separate repository, copy that workflow to the new repository's `.github/workflows/` directory and update the container image reference if you publish your own image.

## 2. Run the build

The template workflow runs on pushes that change `template/**` and can also be started manually from the Actions tab. It uses the GHCR image `ghcr.io/phantomgamezco/xbox360-homebrew-hub/libxenon-toolchain:latest` and uploads `hello.elf32` as a workflow artifact.

The first toolchain image build may take a long time. Wait for the **Build and publish libxenon toolchain** workflow to complete successfully before starting the template build. The GHCR package must be public, or the consuming workflow needs package read access.

## 3. Download the build

Open the successful template-build workflow run in the repository's Actions tab, download the `hello-elf32` artifact, and extract it. The expected executable is `hello.elf32`.

## 4. Run on compatible hardware

Copy `hello.elf32` to a FAT32 USB device and launch it using XeLL on a compatible modified Xbox 360. Homebrew does not run on stock retail consoles. Consult [hardware requirements](hardware-requirements.md) first.

## Releases

When a `v*` tag is pushed to this repository, the template workflow builds the app and attaches `hello.elf32` to the corresponding GitHub Release. Release binaries are distributed only through GitHub Releases and workflow artifacts.
