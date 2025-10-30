---
title: Wie installiert man libgdiplus in macOS
type: docs
description: Dieser Artikel erklärt, wie man libgdiplus in macOS installiert, z. B. Monterey 12.4.
weight: 150
url: /de/net/how-to-install-libgdiplus-in-macos/
---

## Übersicht

In einigen Situationen könnten Sie sich dafür entscheiden, Aspose.Cells zu verwenden und auf die Graphics-Bibliothek System.Drawing.Common zu vertrauen. Diese Situation tritt häufig bei älteren Versionen von .netcore auf (zum Beispiel .netcore31 oder früher).

Da die Graphics-Bibliothek System.Drawing.Common auf libgdiplus angewiesen ist, zeigt dieser Artikel, wie man libgdiplus auf macOS installiert.

## Homebrew in macOS installieren

Zuerst können Sie Homebrew auf macOS installieren, indem Sie den folgenden Befehl im Terminal ausführen.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## libgdiplus in macOS installieren

Nach der Installation von Homebrew können Sie libgdiplus in macOS installieren:

```cs

brew install mono-libgdiplus

```

## Empfohlene Lösung

Für die .NET6-Plattformen (oder später) gibt es im Vergleich zu früheren Plattformen (.netcore31 oder früher) einen wichtigen Unterschied in Bezug auf die Grafikbibliothek. 
In diesem offiziellen [Microsoft-Dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) wird erklärt, dass die Grafikbibliothek "System.Drawing.Common" für .NET6 oder spätere Versionen nur auf Windows unterstützt wird, und es werden Empfehlungen zur Ersetzung der Grafikbibliothek gegeben.

Daher bietet Aspose.Cells eine Lösung, die auf der SkiaSharp-Grafikbibliothek auf Nicht-Windows-Plattformen basiert. Wir empfehlen die Verwendung von SkiaSharp als Bibliothek auf macOS, was auch bedeutet, dass keine libgdiplus installiert werden muss.

Für Informationen zur Installation von Aspose.Cells auf Nicht-Windows-Plattformen und zur Verwendung von SkiaSharp als Grafikbibliothek, siehe den folgenden Artikel:
[So verwenden Sie Aspose.Cells für .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
