---
title: Spalten und Zeilen automatisch anpassen, während HTML in die Arbeitsmappe geladen wird
type: docs
weight: 70
url: /de/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Mögliche Nutzungsszenarien**

 Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei in die Datei laden**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**Objekt. Bitte setzen Sie die**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** Eigentum zu**wahr**für diesen Zweck.

## **Spalten und Zeilen automatisch anpassen, während HTML in die Arbeitsmappe geladen wird**

 Der folgende Beispielcode lädt zunächst das Beispiel HTML ohne Ladeoptionen in die Arbeitsmappe und speichert es im Format XLSX. Es lädt dann erneut das Beispiel HTML in die Arbeitsmappe, aber dieses Mal lädt es das HTML nach dem Festlegen von**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** Eigentum zu**wahr**und speichert es im Format XLSX. Bitte laden Sie beide ausgegebenen Excel-Dateien herunter, dh[Excel-Datei ohne AutoFitColsAndRows ausgeben](outputWithout_AutoFitColsAndRows.xlsx) und[Excel-Datei mit AutoFitColsAndRows ausgeben](outputWith_AutoFitColsAndRows.xlsx) . Der folgende Screenshot zeigt die Wirkung von**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)**-Eigenschaft in beiden Excel-Ausgabedateien.

![todo: Bild_alt_Text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
