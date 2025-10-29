---
title: Как установить libgdiplus в macOS
type: docs
description: «В этой статье объясняется, как установить libgdiplus в macOS, таких как Monterey 12.4.»
weight: 150
url: /ru/net/how-to-install-libgdiplus-in-macos/
---

## Обзор

В некоторых ситуациях вы можете выбрать использование Aspose.Cells и полагаться на графическую библиотеку System.Drawing.Common. Эта ситуация часто возникает в более ранних версиях .NET Core (например, .NET Core 3.1 или ранее).

Поскольку графическая библиотека System.Drawing.Common зависит от libgdiplus, в этой статье показано, как установить libgdiplus на macOS.

## Установка Homebrew в macOS

Сначала вы можете установить Homebrew на macOS, выполнив следующую команду в Терминале.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Установка libgdiplus в macOS

После установки Homebrew вы можете установить libgdiplus в macOS:

```cs

brew install mono-libgdiplus

```

## Рекомендуемое решение

Для платформ .NET6 (или позднее) основное отличие по сравнению с предыдущими платформами (.netcore31 или ранее) заключается в графической библиотеке. 
В этом официальном [документе Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) объясняется, что для .NET6 или более поздних релизов графическая библиотека "System.Drawing.Common" будет поддерживаться только в Windows и даются рекомендации по замене графической библиотеки.

Итак, Aspose.Cells предоставляет решение, основанное на графической библиотеке SkiaSharp для платформ, отличных от Windows. Мы рекомендуем использовать SkiaSharp в качестве библиотеки на macOS, что также означает, что установка libgdiplus не требуется.

Для получения информации о том, как установить Aspose.Cells на платформах, отличных от Windows, и использовать SkiaSharp в качестве графической библиотеки, обратитесь к следующей статье:
[Как запустить Aspose.Cells для .NET6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
