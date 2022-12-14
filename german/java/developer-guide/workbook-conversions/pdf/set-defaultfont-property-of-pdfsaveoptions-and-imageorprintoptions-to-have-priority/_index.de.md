---
title: Setzen Sie die DefaultFont-Eigenschaft von PdfSaveOptions und ImageOrPrintOptions auf Priorität
type: docs
weight: 30
url: /de/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Mögliche Nutzungsszenarien**

 Beim Einstellen der**Standardschriftart** Eigentum von[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) und[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) Sie könnten erwarten, dass das Speichern in PDF oder Bild dies festlegen würde**Standardschriftart** auf den gesamten Text in der Arbeitsmappe, der eine fehlende (nicht installierte) Schriftart enthält.

 Im Allgemeinen versucht Aspose.Cells beim Speichern als PDF oder Bild zuerst, die Standardschriftart von Workbook festzulegen (d. h.[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). Wenn die Standardschriftart der Arbeitsmappe den Text immer noch nicht richtig anzeigen/rendern kann, versucht Aspose.Cells, mit der erwähnten Schriftart zu rendern**Standardschriftart** Attribut ein[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Um Ihrer Erwartung gerecht zu werden, haben wir eine boolesche Eigenschaft namens "**CheckWorkbookDefaultFont** " in[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . Sie können es auf "false" setzen, um die Standardschriftart der Arbeitsmappe zu deaktivieren, oder die**Standardschriftart** Einstellung in[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) Vorrang haben.

## **Legen Sie die DefaultFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions fest**

Der folgende Beispielcode öffnet eine Excel-Datei. Die A1-Zelle (im ersten Arbeitsblatt) hat einen Text, der auf „Schriftarttext für die Weihnachtszeit“ eingestellt ist. Der Schriftartname ist „Christmas Time Personal Use“, der nicht auf dem Gerät installiert ist. Legen wir fest**Standardschriftart**Attribut von[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)zu "Times New Roman". Wir setzen auch**CheckWorkbookDefaultFont**Boolesche Eigenschaft zu "**FALSCH**", wodurch sichergestellt wird, dass der Text der A1-Zelle mit der Schriftart "Times New Roman" gerendert wird und nicht die Standardschriftart der Arbeitsmappe (in diesem Fall "Calibri") verwenden sollte. Der Code rendert das erste Arbeitsblatt in den Bildformaten PNG und TIFF. Es wird schließlich in das PDF-Dateiformat gerendert.

{{% alert color="primary" %}}

 Der Standardwert von***CheckWorkbookDefaultFont*** Attribut ist**Stimmt**.

{{% /alert %}}

Dies ist der Screenshot der[Vorlagendatei](49446914.xlsx)im Beispielcode verwendet.

![todo: Bild_alt_Text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach dem Festlegen von[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)Eigentum an "Times New Roman".

![todo: Bild_alt_Text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Siehe Ausgabe[TIFF](out1_imageTIFF.tiff)Bild nach dem Einstellen der[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)Eigentum an "Times New Roman".

Siehe Ausgabe[Pdf](out1_pdf.pdf)Datei nach dem Festlegen der[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)Eigentum an "Times New Roman".

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
