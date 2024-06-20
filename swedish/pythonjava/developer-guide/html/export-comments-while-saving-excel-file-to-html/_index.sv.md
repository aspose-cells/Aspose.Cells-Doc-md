---
title: Exportera kommentarer vid sparande av Excel fil till HTML
type: docs
weight: 60
url: /sv/python-java/export-comments-while-saving-excel-file-to/
---

## **Exportera kommentarer vid sparande av Excel-fil till HTML**
När Excel konverteras till HTML exporteras inte kommentarer. Aspose.Cells för Python via Java tillhandahåller funktionen att exportera kommentarer under konvertering från Excel till HTML. För att åstadkomma detta tillhandahåller API:et egenskapen [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments). Ange värdet för [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) till **Sant** för att exportera kommentarer i den resulterande HTML-filen.

Följande skärmbild visar den resulterande HTML-filen som genererats av kodexemplet.

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

Följande kodexempel demonstrerar export av kommentarer under konvertering från Excel till HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
