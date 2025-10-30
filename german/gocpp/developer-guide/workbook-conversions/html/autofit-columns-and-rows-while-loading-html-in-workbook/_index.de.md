---
title: Automatisches Anpassen von Spalten und Zeilen beim Laden von HTML in Arbeitsmappen mit Golang via C++
linktitle: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 120
url: /de/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Lernen Sie, wie man Spalten und Zeilen automatisch anpasst, während HTML in eine Arbeitsmappe mit Aspose.Cells for C++ geladen wird.
---

## **Mögliche Verwendungsszenarien**

Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei im Workbook-Objekt laden. Bitte setzen Sie die [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/)-Eigenschaft zu **true** für diesen Zweck.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielcode lädt zunächst den Beispiel-HTML-Code ohne Ladeoptionen in Workbook und speichert ihn im XLSX-Format. Danach wird der Beispiel-HTML-Code erneut in Workbook geladen, diesmal jedoch nachdem die [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/)-Eigenschaft auf **true** gesetzt wurde, und im XLSX-Format gespeichert. Bitte laden Sie beide Ausgabe-Excel-Dateien herunter, d.h. [Ausgabe Excel-Datei ohne AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabe Excel-Datei mit AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Der folgende Screenshot zeigt die Wirkung der [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/)-Eigenschaft auf beide Ausgabe-Excel-Dateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}
