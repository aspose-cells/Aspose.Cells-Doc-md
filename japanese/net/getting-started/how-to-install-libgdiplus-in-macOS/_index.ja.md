---
title: macOS に libgdiplus をインストールする方法
type: docs
description: この記事では、Monterey 12.4 などの macOS に libgdiplus をインストールする方法について説明します。
weight: 150
url: /ja/net/how-to-install-libgdiplus-in-macos/
---
## macOS に Homebrew をインストールする

ターミナルで次のコマンドを実行して、macOS に Homebrew をインストールできます。

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## macOS に libgdiplus をインストールする

Homebrew をインストールしたら、macOS に libgdiplus をインストールできます。

```cs

brew install mono-libgdiplus

```
