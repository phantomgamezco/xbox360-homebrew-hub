#!/usr/bin/env python3
"""Render gallery/apps.json into the MkDocs gallery page."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GALLERY_FILE = ROOT / "gallery" / "apps.json"
PAGE_FILE = ROOT / "docs" / "gallery.md"


def main():
    apps = json.loads(GALLERY_FILE.read_text(encoding="utf-8"))
    lines = [
        "# Community gallery",
        "",
        "The listings below are generated from [`gallery/apps.json`](https://github.com/phantomgamezco/xbox360-homebrew-hub/blob/main/gallery/apps.json). Submissions are validated against [`gallery/apps.schema.json`](https://github.com/phantomgamezco/xbox360-homebrew-hub/blob/main/gallery/apps.schema.json).",
        "",
    ]

    if not apps:
        lines.extend([
            "No community apps have been submitted yet. Contributions should follow the [gallery policy](../CONTRIBUTING.md#gallery-submissions).",
            "",
        ])
    else:
        for app in apps:
            # Escape Markdown table delimiters and line breaks in submitted text.
            description = " ".join(app["description"].replace("|", "\\|").split())
            tested_on = " ".join(app["tested_on"].replace("|", "\\|").split())
            lines.extend([
                f"## {app['name']}",
                "",
                f"By **{app['author']}** · [Source repository]({app['repo']})",
                "",
                description,
                "",
                f"**Tested on:** {tested_on}",
                "",
            ])

    PAGE_FILE.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
