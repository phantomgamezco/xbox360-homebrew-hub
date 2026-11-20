# API notes

This starter intentionally uses only calls and headers shown in the official [Free60Project/libxenon cube example](https://github.com/Free60Project/libxenon/blob/master/devkitxenon/examples/xenon/graphics/cube/source/main.c):

- `#include <xenos/xenos.h>`
- `#include <console/console.h>`
- `xenos_init(VIDEO_MODE_AUTO)`
- `console_init()`
- Standard C `printf()` for console output.

The names above are grounded in the upstream example source. Consult the current upstream project and installed headers for details and additional APIs. This short list is not a complete API reference. Do not infer signatures, supported headers, or build options that are not documented by upstream libxenon.
