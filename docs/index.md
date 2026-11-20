# Xbox 360 Homebrew Hub

Create original Xbox 360 homebrew using the open-source Free60 libxenon toolchain.

!!! warning "Modified console required"
    Apps produced here run only on compatible modified Xbox 360 consoles (such as RGH/JTAG setups). They do not run on stock retail consoles. Real hardware is the test target; emulator compatibility is not claimed.

This project provides a starter app, an Actions build workflow, and a containerized libxenon toolchain. Builds produce an `.elf32` artifact for use on compatible hardware.

## Start building

- [Check hardware requirements](hardware-requirements.md) before building.
- [Follow the getting started guide](getting-started.md) to create a project, build it in GitHub Actions, and transfer the artifact.
- Browse the [API notes](api/index.md) and [community gallery](gallery.md).

## Open-source toolchain only

Builds use [Free60 libxenon](https://github.com/Free60Project/libxenon) and its upstream build script. This hub does not provide proprietary SDKs, console keys or dumps, copyrighted game content, or piracy tools.
