---
title: How to Install libgdiplus in macOS
type: docs
description: "This article explains how to install libgdiplus in macOS, such as Monterey 12.4."
weight: 150
url: /net/how-to-install-libgdiplus-in-macos/
---

## Overview

In some situations, you might choose to use Aspose.Cells and rely on the System.Drawing.Common graphics library. This situation often occurs in earlier versions of .netcore (for example .netcore31 or earlier).

Since System.Drawing.Common graphics library needs to depend on libgdiplus, this article guides how to install libgdiplus on macOS.

## Install Homebrew in macOS

First, you can install Homebrew in macOS by running the following command in Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Install libgdiplus in macOS

After installing Homebrew, you can install libgdiplus in macOS:

```cs

brew install mono-libgdiplus

```

## Recommended solution

For the .NET6 (or later) platforms, compare to previous platforms (.netcore31 or before), an important difference is about the graphics library. 
In this official [Microsoft Document](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), it explains for .NET6 or later releases the graphics library "System.Drawing.Common" will be only supported on Windows, and gives recommendations to replace the graphics library.

So, Aspose.Cells provides a solution that relies on the SkiaSharp graphics library on non-Windows platforms. We recommend using SkiaSharp as the library on macOS, which also means that there is no need to install libgdiplus.

For information on how to install Aspose.Cells on non-Windows platforms and use SkiaSharp as graphics library, please refer to the following article:
[How to Run Aspose.Cells for .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}