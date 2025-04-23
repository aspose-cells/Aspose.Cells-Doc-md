---
title: Wie installiert man libgdiplus in macOS
type: docs
description: Dieser Artikel erklärt, wie man libgdiplus in macOS installiert, z. B. Monterey 12.4.
weight: 150
url: /de/net/how-to-install-libgdiplus-in-macos/
---

## Homebrew in macOS installieren

Sie können Homebrew in macOS installieren, indem Sie den folgenden Befehl in Terminal ausführen.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## libgdiplus in macOS installieren

Nach der Installation von Homebrew können Sie libgdiplus in macOS installieren:

```cs

brew install mono-libgdiplus

```
{{< app/cells/assistant language="csharp" >}}
