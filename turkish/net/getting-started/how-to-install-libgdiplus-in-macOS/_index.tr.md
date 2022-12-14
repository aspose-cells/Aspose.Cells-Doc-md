---
title: macOS'ta libgdiplus nasıl kurulur
type: docs
description: Bu makalede, libgdiplus'ın Monterey 12.4 gibi macOS'ta nasıl kurulacağı açıklanmaktadır.
weight: 150
url: /tr/net/how-to-install-libgdiplus-in-macos/
---
## Homebrew'u macOS'a kurun

Terminal'de aşağıdaki komutu çalıştırarak Homebrew'u macOS'ta kurabilirsiniz.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## macOS'ta libgdiplus'ı kurun

Homebrew'u kurduktan sonra libgdiplus'ı macOS'a kurabilirsiniz:

```cs

brew install mono-libgdiplus

```
