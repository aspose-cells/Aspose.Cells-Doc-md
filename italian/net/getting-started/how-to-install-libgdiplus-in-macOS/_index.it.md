---
title: Come installare libgdiplus su macOS
type: docs
description: "Questo articolo spiega come installare libgdiplus in macOS, come Monterey 12.4."
weight: 150
url: /it/net/how-to-install-libgdiplus-in-macos/
---

## Panoramica

In alcune situazioni, si può scegliere di usare Aspose.Cells affidandosi alla libreria grafica System.Drawing.Common. Questa situazione si verifica spesso nelle versioni più vecchie di .NET Core (ad esempio .NET Core 3.1 o versioni precedenti).

Dato che la libreria grafica System.Drawing.Common dipende da libgdiplus, questo articolo spiega come installare libgdiplus su macOS.

## Installare Homebrew in macOS

Per prima cosa, puoi installare Homebrew su macOS eseguendo il seguente comando nel Terminale.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Installare libgdiplus in macOS

Dopo aver installato Homebrew, è possibile installare libgdiplus in macOS:

```cs

brew install mono-libgdiplus

```

## Soluzione consigliata

Per le piattaforme .NET6 (o successive), a differenza delle piattaforme precedenti (.netcore31 o precedenti), una differenza importante riguarda la libreria grafica. 
In questo [Documento ufficiale di Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), si spiega che per le release di .NET6 o successive la libreria grafica "System.Drawing.Common" sarà supportata solo su Windows e fornisce raccomandazioni per sostituire la libreria grafica.

Quindi, Aspose.Cells fornisce una soluzione basata sulla libreria grafica SkiaSharp su piattaforme non Windows. Raccomandiamo di usare SkiaSharp come libreria su macOS, il che significa anche che non è necessario installare libgdiplus.

Per informazioni su come installare Aspose.Cells su piattaforme non Windows e usare SkiaSharp come libreria grafica, consultare il seguente articolo:
[Come eseguire Aspose.Cells per .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
