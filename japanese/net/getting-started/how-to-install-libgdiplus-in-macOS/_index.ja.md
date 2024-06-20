---
title: macOS で libgdiplus をインストールする方法
type: docs
description: 「この記事では、Monterey 12.4 などの macOS に libgdiplus をインストールする方法について説明します。」
weight: 150
url: /ja/net/how-to-install-libgdiplus-in-macos/
---

## macOS で Homebrew をインストールする

以下のコマンドをターミナルで実行することで、macOS に Homebrew をインストールすることができます。

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## macOS で libgdiplus をインストールする

Homebrew をインストールした後、macOS に libgdiplus をインストールすることができます。

```cs

brew install mono-libgdiplus

```
