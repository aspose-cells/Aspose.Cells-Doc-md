---
title: Konvertera Excel till HTML med verktygstips
type: docs
weight: 150
url: /sv/java/convert-excel-to-html-with-tooltip/
---

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten skärs av i den genererade HTML-filen och du vill visa hela texten som ett verktygstips vid händelse av hovring. Aspose.Cells stödjer detta genom att tillhandahålla [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)-egenskapen. Om du ställer in [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)-egenskapen till **true** kommer hela texten att läggas till som en tooltip i den genererade HTML-filen.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll excelfilen](AddTooltipToHtmlSample.xlsx) och genererar [utdata HTML-filen](AddTooltipToHtmlSample_out.zip) med en tooltip.

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
