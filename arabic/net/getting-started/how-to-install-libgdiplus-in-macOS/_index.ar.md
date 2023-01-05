---
title: كيفية تثبيت libgdiplus في macOS
type: docs
description: تشرح هذه المقالة كيفية تثبيت libgdiplus في macOS ، مثل Monterey 12.4
weight: 150
url: /ar/net/how-to-install-libgdiplus-in-macos/
---
## قم بتثبيت Homebrew في macOS

يمكنك تثبيت Homebrew في macOS عن طريق تشغيل الأمر التالي في Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## قم بتثبيت libgdiplus في macOS

بعد تثبيت Homebrew ، يمكنك تثبيت libgdiplus في macOS:

```cs

brew install mono-libgdiplus

```
