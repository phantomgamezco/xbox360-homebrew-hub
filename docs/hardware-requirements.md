# Hardware requirements

## A compatible modified console is required

Homebrew produced by this project runs only on compatible **modified Xbox 360 consoles**, such as systems using an RGH or JTAG setup and a XeLL boot path. It does **not** run on a stock retail Xbox 360. This project does not modify consoles or provide instructions for bypassing console security.

## What you need

- A compatible Xbox 360 with a homebrew-capable setup and XeLL available.
- A FAT32-formatted USB storage device.
- A build artifact named `hello.elf32` (or your app's corresponding `.elf32` output), downloaded from the GitHub Actions run.
- A display and controller suitable for testing the app.

Hardware revisions, installed homebrew environments, and XeLL configurations differ. Confirm that your own setup supports launching the generated ELF before attempting to run it. Do not use a stock retail console as a test target.

## Testing

Real compatible hardware is the test target. Emulator support is not asserted; in particular, do not treat an emulator run as evidence that the app works on console hardware.
