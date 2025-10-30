---
title: Hur man installerar libgdiplus i macOS
type: docs
description: "Denna artikel förklarar hur man installerar libgdiplus i macOS, som Monterey 12.4."
weight: 150
url: /sv/net/how-to-install-libgdiplus-in-macos/
---

## Översikt

I vissa situationer kan du välja att använda Aspose.Cells och förlita dig på grafikbiblioteket System.Drawing.Common. Denna situation inträffar ofta i äldre versioner av .netcore (till exempel .netcore31 eller äldre).

Eftersom System.Drawing.Common grafikbibliotek behöver bero på libgdiplus, visar denna artikel hur man installerar libgdiplus på macOS.

## Installera Homebrew i macOS

Först kan du installera Homebrew på macOS genom att köra följande kommando i Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## Installera libgdiplus i macOS

Efter att ha installerat Homebrew kan du installera libgdiplus i macOS:

```cs

brew install mono-libgdiplus

```

## Rekommenderad lösning

För .Net6 (eller senare) plattformar, jämfört med tidigare plattformar (.netcore31 eller tidigare) är en viktig skillnad gällande grafikbiblioteket. 
I detta officiella [Microsoft-dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) förklaras det att för .Net6 eller senare versioner kommer grafikbiblioteket "System.Drawing.Common" endast stödjas på Windows och ger rekommendationer om att ersätta grafikbiblioteket.

Så Aspose.Cells erbjuder en lösning som är beroende av SkiaSharp-ritbiblioteket på icke-Windows plattformar. Vi rekommenderar att använda SkiaSharp som bibliotek på macOS, vilket också innebär att det inte är nödvändigt att installera libgdiplus.

För information om hur man installerar Aspose.Cells på icke-Windows plattformar och använder SkiaSharp som grafikbibliotek, hänvisar vi till följande artikel:
[Hur man kör Aspose.Cells för .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
