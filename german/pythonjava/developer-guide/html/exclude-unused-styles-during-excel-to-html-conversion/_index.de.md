---
title: Nicht verwendete Styles bei der Excel zu HTML Konvertierung ausschließen
type: docs
weight: 30
url: /de/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**
Microsoft Excel-Dateien können viele nicht verwendete Stile enthalten. Wenn diese Dateien im HTML-Format exportiert werden, werden auch die nicht verwendeten Stile exportiert. Dies führt zu einer Erhöhung der Größe des Ausgab HTMLs. Aspose.Cells für Python via Java unterstützt das Ausschließen dieser Stile während der Konvertierung der Excel-Datei in HTML. Hierfür stellt die API die Eigenschaft [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) bereit. Durch Setzen des Werts der Eigenschaft [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) auf **True** werden alle nicht verwendeten Stile aus der Ausgabe-HTML ausgeschlossen.

Der folgende Screenshot zeigt nicht verwendete Stile in der HTML-Datei, die durch Setzen des Werts der Eigenschaft [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) auf **True** entfernt werden.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Der folgende Beispielcode demonstriert das Entfernen nicht verwendeter Stile während der Konvertierung von Excel nach HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
