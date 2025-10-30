---
title: Konvertera Excel till HTML med verktygstips med C++
linktitle: Konvertera Excel till HTML med verktygstips
type: docs
weight: 200
url: /sv/go-cpp/convert-excel-to-html-with-tooltip/
description: Konvertera Excel till HTML samtidigt som du lägger till verktygstips med Aspose.Cells med C++.
---

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten klipps av i den genererade HTML och du vill visa hela texten som ett verktygstips vid hover-händelsen. Aspose.Cells stöder detta genom att tillhandahålla [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/)-egenskapen. Att sätta [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) till **true** kommer att lägga till hela texten som ett verktygstips i den genererade HTML.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll-Excel-filen](98107416.xlsx) och genererar [utdata-HTML-filen](98107417.zip) med verktygstips.

Exempelkod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
