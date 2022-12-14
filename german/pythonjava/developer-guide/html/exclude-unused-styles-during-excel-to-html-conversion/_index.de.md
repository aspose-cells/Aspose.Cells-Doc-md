---
title: Schließen Sie nicht verwendete Stile während der Excel-zu-HTML-Konvertierung aus
type: docs
weight: 30
url: /de/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Schließen Sie nicht verwendete Stile während der Excel-zu-HTML-Konvertierung aus**
Microsoft Excel-Dateien können viele ungenutzte Stile enthalten. Wenn diese Dateien in das HTML-Format exportiert werden, werden die nicht verwendeten Stile ebenfalls exportiert. Dies führt zu einer erhöhten Größe des Ausgabe-HTML. Aspose.Cells für Python über Java unterstützt das Ausschließen dieser Stile während der Konvertierung von Excel-Dateien in HTML. Dafür sorgt die API[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)Eigentum. Festlegen des Werts von[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) Eigentum zu**WAHR** schließt alle nicht verwendeten Stile aus dem Ausgabe-HTML aus.

Der folgende Screenshot zeigt ungenutzte Stile in der HTML-Datei, die durch Setzen des Werts von entfernt werden[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) Eigentum zu**WAHR**.

![todo: Bild_alt_Text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Der folgende Beispielcode demonstriert das Entfernen nicht verwendeter Stile während der Konvertierung von Excel in HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
