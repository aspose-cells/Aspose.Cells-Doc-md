---
title: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 120
url: /de/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Mögliche Verwendungsszenarien**

Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei im Workbook-Objekt laden. Bitte setzen Sie die [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)-Eigenschaft zu **true** für diesen Zweck.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielcode lädt zunächst den Beispiel-HTML-Code ohne Ladeoptionen in Workbook und speichert ihn im XLSX-Format. Danach wird der Beispiel-HTML-Code erneut in Workbook geladen, diesmal jedoch nachdem die [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)-Eigenschaft auf **true** gesetzt wurde, und im XLSX-Format gespeichert. Bitte laden Sie beide Ausgabe-Excel-Dateien herunter, d.h. [Ausgabe Excel-Datei ohne AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabe Excel-Datei mit AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Der folgende Screenshot zeigt die Wirkung der [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)-Eigenschaft auf beide Ausgabe-Excel-Dateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

