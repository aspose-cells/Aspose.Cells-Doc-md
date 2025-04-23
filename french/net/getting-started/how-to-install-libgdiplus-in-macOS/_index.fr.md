---
title: Comment installer libgdiplus sur macOS
type: docs
description: "Cet article explique comment installer libgdiplus sur macOS, tel que Monterey 12.4."
weight: 150
url: /fr/net/how-to-install-libgdiplus-in-macos/
---

## Installer Homebrew dans macOS

Vous pouvez installer Homebrew dans macOS en exécutant la commande suivante dans le Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Installer libgdiplus dans macOS

Après avoir installé Homebrew, vous pouvez installer libgdiplus dans macOS :

```cs

brew install mono-libgdiplus

```
{{< app/cells/assistant language="csharp" >}}
