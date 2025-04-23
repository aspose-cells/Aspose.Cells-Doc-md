---
title: Konvertera Excel till HTML med verktygstips
type: docs
weight: 200
url: /sv/net/convert-excel-to-html-with-tooltip/
---

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten kapas i den genererade HTML:en och du vill visa hela texten som ett verktygstips vid händelsen för att hovra över. Aspose.Cells stödjer detta genom att tillhandahålla [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) egenskapen. Att sätta [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) egenskapen till **true** kommer att lägga till hela texten som ett verktygstips i den genererade HTML:en.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll-excelfilen](98107416.xlsx) och genererar [utdata-HTML-filen](98107417.zip) med verktygstipset.

Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
