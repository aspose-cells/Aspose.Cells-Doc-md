---
title: Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus
type: docs
weight: 30
url: /de/java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Mögliche Nutzungsszenarien**

Microsoft Excel-Datei enthält möglicherweise viele nicht verwendete Stile. Wenn Sie die Excel-Datei in das Format HTML exportieren, werden diese nicht verwendeten Stile ebenfalls exportiert. Dies kann die Größe von HTML erhöhen. Sie können die ungenutzten Stile während der Konvertierung der Excel-Datei in HTML mit ausschließen[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)Eigentum. Wenn Sie es einstellen**wahr**, werden alle nicht verwendeten Stile von der Ausgabe HTML ausgeschlossen. Der folgende Screenshot zeigt ein Beispiel für einen nicht verwendeten Stil in der Ausgabe HTML.

![todo: Bild_alt_Text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Schließen Sie nicht verwendete Stile während der Konvertierung von Excel in HTML aus**

Der folgende Beispielcode erstellt eine Arbeitsmappe und erstellt außerdem einen nicht verwendeten benannten Stil. Seit der[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)ist eingestellt auf**wahr**, sodass dieser unbenutzte benannte Stil nicht exportiert wird[Ausgang HTML](61767781.zip). Aber wenn du es einstellst**FALSCH**, dann ist dieser ungenutzte Stil in der Ausgabe HTML vorhanden, die Sie dann im Markup HTML sehen können, wie im obigen Screenshot gezeigt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
