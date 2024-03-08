---
title: Konvertera Excel till HTML med verktygstips
type: docs
weight: 200
url: /sv/python-net/convert-excel-to-html-with-tooltip/
description: Det här avsnittet visar hur du konverterar Excel till HTML med verktygstips med Aspose.Cells for Python via NET.
keywords: Python Convert Excel to HTML with tooltip, Convert Excel to HTML with tooltip Python via NET, Python via NET Excel to HTML with tooltip, Python Workbook to HTML with tooltip.
---
##  **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten klipps av i den genererade HTML och du vill visa hela texten som ett verktygstips på hovringshändelsen. Aspose.Cells stöder detta genom att tillhandahålla**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)** fast egendom. Ställa in**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)** egendom till**Sann** kommer att lägga till hela texten som ett verktygstips i den genererade HTML.

Följande bild visar verktygstipset i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 Följande kodexempel laddar[source excel-fil](98107416.xlsx) och genererar[utgång HTML fil](98107417.zip) med verktygstipset.

Exempelkod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
