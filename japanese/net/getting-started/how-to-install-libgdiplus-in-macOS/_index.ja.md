---
title: macOS で libgdiplus をインストールする方法
type: docs
description: 「この記事では、Monterey 12.4 などの macOS に libgdiplus をインストールする方法について説明します。」
weight: 150
url: /ja/net/how-to-install-libgdiplus-in-macos/
---

## 概要

場合によっては、Aspose.Cellsを使用し、System.Drawing.Commonのグラフィックライブラリに依存することを選択するかもしれません。この状況は、特に古いバージョンの.NET Core（例：.NET Core 3.1以前）でよく発生します。

System.Drawing.Commonのグラフィックライブラリはlibgdiplusに依存しているため、この記事ではmacOS上でのlibgdiplusのインストール方法を案内します。

## macOS で Homebrew をインストールする

まず、macOSにHomebrewをインストールするには、ターミナルで次のコマンドを実行します。

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## macOS で libgdiplus をインストールする

Homebrew をインストールした後、macOS に libgdiplus をインストールすることができます。

```cs

brew install mono-libgdiplus

```

## 推奨ソリューション

.NET6（またはそれ以降）プラットフォームでは、以前のプラットフォーム（.netcore31 より前）と比較して、重要な違いはグラフィックスライブラリに関するものです。 
この公式[Microsoftドキュメント](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)では、.NET6 以降についてグラフィックスライブラリの「System.Drawing.Common」がWindowsでのみサポートされると説明され、グラフィックスライブラリの置換に関する推奨事項が示されています。

そのため、Aspose.CellsはWindows以外のプラットフォーム上でSkiaSharpグラフィックライブラリに依存するソリューションを提供しています。macOSではSkiaSharpをライブラリとして使用することを推奨しており、これによりlibgdiplusのインストールは不要になります。

非WindowsプラットフォームにおけるAspose.Cellsのインストール方法やSkiaSharpをグラフィックライブラリとして使用する方法については、以下の記事を参照してください：
[.Net6用Aspose.Cellsの実行方法](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
