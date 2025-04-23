---
title: كيفية تثبيت libgdiplus في نظام التشغيل macOS
type: docs
description: يشرح هذا المقال كيفية تثبيت libgdiplus في نظام التشغيل macOS، مثل Monterey 12.4.
weight: 150
url: /ar/net/how-to-install-libgdiplus-in-macos/
---

## تثبيت Homebrew في نظام التشغيل macOS

يمكنك تثبيت Homebrew في macOS عن طريق تشغيل الأمر التالي في Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## تثبيت libgdiplus في نظام التشغيل macOS

بعد تثبيت Homebrew ، يمكنك تثبيت libgdiplus في macOS:

```cs

brew install mono-libgdiplus

```
{{< app/cells/assistant language="csharp" >}}
