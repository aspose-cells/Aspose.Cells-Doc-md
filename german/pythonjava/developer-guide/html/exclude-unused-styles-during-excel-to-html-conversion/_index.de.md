---
title: Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus
type: docs
weight: 30
url: /de/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus**
Microsoft Excel-Dateien können viele ungenutzte Stile enthalten. Wenn diese Dateien in das Format HTML exportiert werden, werden die nicht verwendeten Stile ebenfalls exportiert. Dies führt zu einer erhöhten Größe der Ausgabe HTML. Aspose.Cells for Python via Java unterstützt das Ausschließen dieser Stile während der Konvertierung der Excel-Datei in HTML. Dafür bietet die API die[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)Eigentum. Festlegen des Werts von[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) Eigentum zu**Wahr** schließt alle ungenutzten Styles aus der Ausgabe HTML aus.

Der folgende Screenshot zeigt unbenutzte Stile in der Datei HTML, die durch Setzen des Werts von entfernt werden[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) Eigentum zu**Wahr**.

![todo: Bild_alt_Text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Der folgende Beispielcode demonstriert das Entfernen nicht verwendeter Stile während der Konvertierung von Excel in HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
