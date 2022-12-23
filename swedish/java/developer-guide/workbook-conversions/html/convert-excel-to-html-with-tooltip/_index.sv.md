---
title: Konvertera Excel till HTML med verktygstips
type: docs
weight: 150
url: /sv/java/convert-excel-to-html-with-tooltip/
---
## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten klipps av i den genererade HTML och du vill visa hela texten som ett verktygstips på hovringshändelsen. Aspose.Cells stöder detta genom att tillhandahålla**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**fast egendom. Ställa in**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**egendom till**Sann**kommer att lägga till hela texten som ett verktygstips i den genererade HTML.

Följande bild visar verktygstipset i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar[source excel-fil](AddTooltipToHtmlSample.xlsx)och genererar[utgång HTML fil](AddTooltipToHtmlSample_out.zip)med verktygstipset.

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
