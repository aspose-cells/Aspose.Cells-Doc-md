---
title: StandardFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions Priorität einräumen
type: docs
weight: 30
url: /de/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Mögliche Verwendungsszenarien**

Beim Setzen der **DefaultFont**-Eigenschaft von [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) könnte man erwarten, dass das Speichern in PDF oder Bild diese **DefaultFont** für den gesamten Text in der Arbeitsmappe setzt, der eine fehlende (nicht installierte) Schriftart hat.

Beim Speichern in PDF oder Bild wird Aspose.Cells zunächst versuchen, die Standard-Schriftart des Arbeitsbuchs zu setzen (d. h. [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font-)). Wenn die Standard-Schriftart des Arbeitsbuchs immer noch nicht richtig Text anzeigen oder rendern kann, versucht Aspose.Cells, mit der in [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) genannten Schriftart zu rendern.

Um Ihren Erwartungen gerecht zu werden, haben wir eine boolesche Eigenschaft namens "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions). Sie können diese auf false setzen, um das Festlegen der Standardschriftart der Arbeitsmappe zu deaktivieren, oder die Einstellung **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) priorisieren.

## **StandardFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions festlegen**

Der folgende Beispielcode öffnet eine Excel-Datei. Die Zelle A1 (im ersten Arbeitsblatt) enthält einen Text, der auf "Weihnachtszeit-Schrifttext" festgelegt ist. Der Schriftname lautet "Weihnachtszeit Persönlich", der nicht auf dem Rechner installiert ist. Wir setzen das **DefaultFont**-Attribut von [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) auf "Times New Roman". Außerdem setzen wir die boolesche Eigenschaft **CheckWorkbookDefaultFont** auf "**false**", um sicherzustellen, dass der Text der Zelle A1 mit der Schriftart "Times New Roman" gerendert wird und nicht die Standardschriftart der Arbeitsmappe (in diesem Fall "Calibri") verwendet wird. Der Code rendert das erste Arbeitsblatt in PNG- und TIFF-Bilddateiformaten. Schließlich wird in das PDF-Dateiformat gerendert.

{{% alert color="primary" %}}

Der Standardwert des ***CheckWorkbookDefaultFont***-Attributs ist **true**.

{{% /alert %}}

Dies ist der Screenshot der [Vorlagendatei](49446914.xlsx), die im Beispielcode verwendet wurde.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach Einstellung der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) auf "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Sehen Sie das Ausgabe [TIFF](out1_imageTIFF.tiff)-Bild nach Einstellung der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) auf "Times New Roman".

Sehen Sie die Ausgabe [PDF](out1_pdf.pdf)-Datei nach Einstellung der Eigenschaft [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) auf "Times New Roman".

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
