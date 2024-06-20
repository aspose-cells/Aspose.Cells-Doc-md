---
title: Excel med icke supporterad kantstil till HTML
type: docs
weight: 80
url: /sv/python-java/excel-with-unsupported-border-style-to/
---

## **Excel med icke-supporterad kantstil till HTML**
Microsoft Excel stöder vissa typer av streckade kanter som inte stöds av webbläsare. När sådana filer konverteras till HTML med hjälp av Aspose.Cells tas dessa kanter bort. Aspose.Cells för Python via Java stöder dock visning av liknande kanter med egenskapen [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle). Du kan ange värdet för [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) till **Sant** för att exportera icke-supporterade kanter.

Följande kodexempel laddar den [exempelvis filen i Excel-format](sampleExportSimilarBorderStyle.xlsx) som innehåller vissa icke-supporterade kanter som visas i följande skärmbild. Skärmbilden illustrerar ytterligare effekten av egenskapen [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) inuti [utmatnings-HTML-filen](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
