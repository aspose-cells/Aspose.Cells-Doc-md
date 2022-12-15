---
title: Excel med kantstil till HTML som inte stöds
type: docs
weight: 80
url: /sv/python-java/excel-with-unsupported-border-style-to/
---
## **Excel med kantstil till HTML som inte stöds**
Microsoft Excel stöder någon typ av streckade kanter som inte stöds av webbläsare. När sådana filer konverteras till HTML med Aspose.Cells tas dessa gränser bort. Aspose.Cells for Python via Java stöder dock visning av liknande ramar med[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)fast egendom. Du kan ställa in värdet på[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) egendom till**Sann** att exportera gränser som inte stöds.

Följande exempelkod laddar[exempel på Excel-fil](sampleExportSimilarBorderStyle.xlsx)som innehåller några gränser som inte stöds som visas i följande skärmdump. Skärmdumpen illustrerar ytterligare effekten av[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)egendom inuti[mata ut HTML](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
