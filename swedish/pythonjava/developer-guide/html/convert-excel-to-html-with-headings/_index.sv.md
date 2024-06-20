---
title: Konvertera Excel till HTML med rubriker
type: docs
weight: 10
url: /sv/python-java/convert-excel-to-html-with-headings/
---

## **Konvertera Excel till HTML med rubriker**
Aspose.Cells tillhandahåller alternativet att exportera rad- och kolumnrubriker vid konvertering av Excel till HTML. Detta kan åstadkommas genom att använda egenskapen [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) som tillhandahålls av API:et. Standardvärdet för [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) är **Falskt**. Ange **Sant** som parameter för att rendera rubriker i den genererade HTML-filen. Det följande exemplet visar den resulterande filen som genereras av koden.

![todo:image_alt_text](PrintHeadings.jpg)

Följande kodexempel visar användning av egenskapen [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) för att rendera rubriker i den genererade HTML-filen.
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}
