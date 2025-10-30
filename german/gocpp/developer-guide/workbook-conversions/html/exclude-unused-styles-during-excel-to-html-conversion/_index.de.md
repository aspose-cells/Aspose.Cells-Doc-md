---
title: Schließen Sie ungenutzte Stile während der Excel zu HTML Konvertierung mit Golang über C++ aus
linktitle: Unbenutzte Stile ausschließen
type: docs
weight: 30
url: /de/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Lernen, wie unbenutzte Stile während der Excel zu HTML Konvertierung mit Aspose.Cells for C++ ausgeschlossen werden.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel-Dateien können viele unbenutzte Stile enthalten. Beim Exportieren der Excel-Datei in HTML werden diese unbenutzten Stile ebenfalls exportiert, was die HTML-Größe erhöhen kann. Sie können unbenutzte Stile während der Konvertierung einer Excel-Datei in HTML mit der [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) Eigenschaft ausschließen. Wenn Sie sie auf **true** setzen, werden alle unbenutzten Stile vom Ausgab-HTML ausgeschlossen. Das folgende Bild zeigt einen Beispiel-Unbenutzten Stil im HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**

Der folgende Beispielcode erstellt eine Arbeitsmappe und einen unbenutzten benannten Stil. Da [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) auf **true** gesetzt ist, wird dieser unbenutzte Stil nicht in das [Ausgabe-HTML](61767778.zip) exportiert. Wenn Sie es auf **false** setzen, wird dieser unbenutzte Stil im Ausgabe-HTML sichtbar sein, was Sie im HTML-Markup sehen können, wie im oben genannten Screenshot.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
