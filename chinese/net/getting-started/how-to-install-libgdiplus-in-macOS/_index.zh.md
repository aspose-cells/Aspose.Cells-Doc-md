---
title: 在 macOS 中安装 libgdiplus
type: docs
description: 本文介绍如何在 macOS（如 Monterey 12.4）中安装 libgdiplus。
weight: 150
url: /zh/net/how-to-install-libgdiplus-in-macos/
---

## 概述

在某些情况下，您可能选择使用Aspose.Cells并依赖System.Drawing.Common图形库。这种情况通常出现在较早版本的.netcore（例如.netcore31或更早版本）。

由于System.Drawing.Common图形库需要依赖libgdiplus，本文将指导如何在macOS上安装libgdiplus。

## 在 macOS 中安装 Homebrew

首先，您可以在macOS上通过在终端中运行以下命令安装Homebrew。

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## 在 macOS 中安装 libgdiplus

安装 Homebrew 后，您可以在 macOS 中安装 libgdiplus：

```cs

brew install mono-libgdiplus

```

## 推荐方案

对于 .NET6（或更高版本）平台，与之前的平台（.netcore31 或更早版本）相比，一个重要的区别是关于图形库。 
在这份官方[微软文档](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)中，它解释了对于 .NET6 或更高版本，图形库“System.Drawing.Common”将仅在 Windows 上受支持，并就替换图形库提出建议。

因此，Aspose.Cells 提供了依赖 SkiaSharp 图形库的解决方案，适用于非 Windows 平台。我们建议在 macOS 上使用 SkiaSharp 作为图形库，这也意味着无需安装 libgdiplus。

关于如何在非 Windows 平台安装 Aspose.Cells 并使用 SkiaSharp 作为图形库的详细信息，请参阅以下文章：
[如何在 .Net6 上运行 Aspose.Cells](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
