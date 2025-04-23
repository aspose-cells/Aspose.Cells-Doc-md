---
title: Nicht verwendete Styles bei der Excel zu HTML Konvertierung ausschließen
type: docs
weight: 30
url: /de/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Mögliche Verwendungsszenarien**

Eine Microsoft Excel-Datei kann viele unbenutzte Stile enthalten. Wenn Sie die Excel-Datei im HTML-Format exportieren, werden diese unbenutzten Stile ebenfalls exportiert. Dies kann die Größe von HTML erhöhen. Sie können die unbenutzten Stile während der Konvertierung der Excel-Datei in HTML mithilfe der [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles)-Eigenschaft ausschließen. Wenn Sie diese Eigenschaft auf true setzen, werden alle unbenutzten Stile aus der Ausgabe-HTML ausgeschlossen. Der folgende Screenshot zeigt einen Beispiel unbenutzter Stil in der Ausgabe-HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**

Der folgende Beispielscode erstellt eine Arbeitsmappe und erstellt auch einen unbenutzten benannten Stil. Da [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) auf true gesetzt ist, wird dieser unbenutzte benannte Stil nicht in der [Ausgabe-HTML](61767778.zip) exportiert. Wenn Sie es jedoch auf false setzen, wird dieser unbenutzte Stil in der Ausgabe-HTML enthalten sein, den Sie dann im HTML-Markup wie im obigen Screenshot sehen können.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
