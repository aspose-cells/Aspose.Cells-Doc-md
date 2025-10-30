---
title: Konvertera Excel till HTML med verktygstips
type: docs
weight: 200
url: /sv/python-net/convert-excel-to-html-with-tooltip/
description: Denna artikel visar dig hur du konverterar Excel till HTML med verktygstips med Aspose.Cells for Python via NET.
keywords: Python konverterar Excel till HTML med verktygstips, Konvertera Excel till HTML med verktygstips Python via NET, Python via NET Excel till HTML med verktygstips, Python arbetsbok till HTML med verktygstips.
---

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten kapas i den genererade HTML:en och du vill visa hela texten som ett verktygstips vid händelsen för att hovra över. Aspose.Cells stödjer detta genom att tillhandahålla [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) egenskapen. Att sätta [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) egenskapen till **true** kommer att lägga till hela texten som ett verktygstips i den genererade HTML:en.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll-excelfilen](98107416.xlsx) och genererar [utdata-HTML-filen](98107417.zip) med verktygstipset.

Exempelkod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
