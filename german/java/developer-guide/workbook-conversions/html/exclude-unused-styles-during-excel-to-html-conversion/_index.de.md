---
title: Nicht verwendete Styles bei der Excel zu HTML Konvertierung ausschließen
type: docs
weight: 30
url: /de/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Mögliche Verwendungsszenarien**

Eine Microsoft Excel-Datei kann viele ungenutzte Styles enthalten. Wenn Sie die Excel-Datei im HTML-Format exportieren, werden diese ungenutzten Styles ebenfalls exportiert. Dies kann die Größe des HTML erhöhen. Sie können die ungenutzten Styles bei der Konvertierung der Excel-Datei in HTML mithilfe der [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)-Eigenschaft ausschließen. Wenn Sie es auf **true** einstellen, werden alle ungenutzten Styles aus der Ausgabe-HTML ausgeschlossen. Der folgende Screenshot zeigt einen Beispielnichtverwendeten Style in der Ausgabe-HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**

Der folgende Beispielcode erstellt eine Arbeitsmappe und erstellt auch einen ungenutzten benannten Stil. Da die [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)-Eigenschaft auf **true** festgelegt ist, wird dieser ungenutzte benannte Stil nicht in [output HTML](61767781.zip) exportiert. Aber wenn Sie es auf **false** setzen, wird dieser ungenutzte Stil in der Ausgabe-HTML vorhanden sein, den Sie dann im HTML-Markup wie im obigen Screenshot sehen können.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
