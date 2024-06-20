---
title: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 70
url: /de/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Mögliche Verwendungsszenarien**

Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei im [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Objekt laden. Bitte setzen Sie die Eigenschaft [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) auf **true** für diesen Zweck.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielscode lädt zuerst das Beispiels-HTML in die Arbeitsmappe ohne Ladeoptionen und speichert es im XLSX-Format. Dann lädt er erneut das Beispiels-HTML in die Arbeitsmappe, aber diesmal lädt er das HTML, nachdem die Eigenschaft [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) auf **true** gesetzt wurde, und speichert es im XLSX-Format. Bitte laden Sie beide Ausgabedateien herunter, d.h. [Ausgabedatei ohne AutofitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabedatei mit AutofitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Der folgende Screenshot zeigt die Wirkung der Eigenschaft [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) auf beide Ausgabedateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
