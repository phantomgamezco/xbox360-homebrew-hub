# Troubleshooting

## The Actions job cannot pull the toolchain image

The image must be published before the template workflow runs. Check the **Build and publish libxenon toolchain** workflow and ensure the GHCR package `libxenon-toolchain` is public, or that the workflow token has package read permission.

## The toolchain image build fails

The image builds Free60's upstream sources and downloads compiler dependencies. Check the failing command and upstream build log, then compare with the current [libxenon README](https://github.com/Free60Project/libxenon/blob/master/README.md). Upstream dependencies or source build instructions may have changed.

## The app build does not produce `hello.elf32`

Check that the `DEVKITXENON` environment and upstream `rules` are present in the image. The template Makefile follows the upstream example Makefile; consult its current version if upstream changes the target behavior.

## The app does not launch

Confirm the console is a compatible modified Xbox 360 with XeLL and that the file is the extracted `.elf32` artifact on FAT32 media. This project cannot make a stock console run homebrew. Do not use emulator behavior as a substitute for testing on real hardware.
