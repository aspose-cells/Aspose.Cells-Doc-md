---
title: How to Install libgdiplus in macOS
type: docs
description: "This article explains how to install libgdiplus in macOS, such as Monterey 12.4."
weight: 150
url: /net/how-to-install-libgdiplus-in-macos/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Overview

In some situations, you might choose to use Aspose.Cells and rely on the System.Drawing.Common graphics library. This situation often occurs in earlier versions of .NET Core (for example, .NET Core 3.1 or earlier).

Since the System.Drawing.Common graphics library depends on libgdiplus, this article guides you on how to install libgdiplus on macOS.

## Install Homebrew in macOS

First, you can install Homebrew in macOS by running the following command in Terminal.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Install libgdiplus in macOS

After installing Homebrew, you can install libgdiplus in macOS:

```bash
brew install mono-libgdiplus
```

## Recommended solution

For .NET 6 (or later) platforms, compared with previous platforms (.NET Core 3.1 or earlier), an important difference concerns the graphics library.  
In this official Microsoft document, it explains that for .NET 6 or later releases, the graphics library **System.Drawing.Common** is supported only on Windows, and provides recommendations for replacing the graphics library.

So, Aspose.Cells provides a solution that relies on the SkiaSharp graphics library on non‑Windows platforms. We recommend using SkiaSharp as the graphics library on macOS, which also means that there is no need to install libgdiplus.

For information on how to install Aspose.Cells on non‑Windows platforms and use SkiaSharp as the graphics library, please refer to the following article:  
[How to Run Aspose.Cells for .NET 6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
