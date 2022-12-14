---
title: Konvertera Excel till HTML med verktygstips
type: docs
weight: 200
url: /sv/net/convert-excel-to-html-with-tooltip/
---
## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten är avskuren i den genererade HTML-koden och du vill visa hela texten som ett verktygstips för hovringshändelsen. Aspose.Cells stöder detta genom att tillhandahålla**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** fast egendom. Ställa in**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** egendom till**Sann** kommer att lägga till hela texten som ett verktygstips i den genererade HTML-koden.

Följande bild visar verktygstipset i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 Följande kodexempel laddar[source excel-fil](98107416.xlsx) och genererar[utdata HTML-fil](98107417.zip) med verktygstipset.

Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
