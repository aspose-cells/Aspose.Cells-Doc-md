---
title: Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus
type: docs
weight: 30
url: /de/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Mögliche Nutzungsszenarien**

Microsoft Excel-Datei enthält möglicherweise viele nicht verwendete Stile. Wenn Sie die Excel-Datei in das Format HTML exportieren, werden diese nicht verwendeten Stile ebenfalls exportiert. Dies kann die Größe von HTML erhöhen. Sie können die ungenutzten Stile während der Konvertierung der Excel-Datei in HTML mit ausschließen[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) Eigentum. Wenn Sie es einstellen**wahr**, werden alle nicht verwendeten Stile von der Ausgabe HTML ausgeschlossen. Der folgende Screenshot zeigt ein Beispiel für einen nicht verwendeten Stil in der Ausgabe HTML.

![todo: Bild_alt_Text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus**

Der folgende Beispielcode erstellt eine Arbeitsmappe und erstellt außerdem einen nicht verwendeten benannten Stil. Seit der[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) ist eingestellt auf**wahr** , wird dieser unbenutzte benannte Stil nicht exportiert[Ausgang HTML](61767778.zip) . Aber wenn man es einstellt**FALSCH**, dann ist dieser ungenutzte Stil in der Ausgabe HTML vorhanden, die Sie dann im Markup HTML sehen können, wie im obigen Screenshot gezeigt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
