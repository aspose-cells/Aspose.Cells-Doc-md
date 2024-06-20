---
title: Export von Kommentaren beim Speichern von Excel Datei in HTML
type: docs
weight: 60
url: /de/python-java/export-comments-while-saving-excel-file-to/
---

## **Kommentare beim Speichern einer Excel-Datei in HTML exportieren**
Beim Konvertieren von Excel in HTML werden Kommentare nicht exportiert. Aspose.Cells für Python via Java bietet die Funktion zum Exportieren von Kommentaren während der Konvertierung von Excel in HTML. Hierfür stellt die API die Eigenschaft [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) bereit. Durch Setzen des Werts der Eigenschaft [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) auf **True** werden Kommentare in der Ausgabe-HTML exportiert.

Der folgende Screenshot zeigt die Ausgabedatei HTML, die durch den Beispielcode-Schnipsel generiert wurde.

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

Der folgende Beispielcode demonstriert das Exportieren von Kommentaren während der Konvertierung von Excel in HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
