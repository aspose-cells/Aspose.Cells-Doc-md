---
title: 在 macOS 中安装 libgdiplus
type: docs
description: 本文介绍如何在 macOS（如 Monterey 12.4）中安装 libgdiplus。
weight: 150
url: /zh/net/how-to-install-libgdiplus-in-macos/
---

## 在 macOS 中安装 Homebrew

您可以通过在终端中运行以下命令来在 macOS 中安装 Homebrew。

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## 在 macOS 中安装 libgdiplus

安装 Homebrew 后，您可以在 macOS 中安装 libgdiplus：

```cs

brew install mono-libgdiplus

```
{{< app/cells/assistant language="csharp" >}}
