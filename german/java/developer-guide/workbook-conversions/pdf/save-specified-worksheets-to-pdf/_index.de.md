---
title: Speichern Sie die angegebenen Arbeitsblätter unter PDF
type: docs
weight: 51
url: /de/java/save-specified-worksheets-to-pdf/
---
 Standardmäßig ist Aspose.Cells alles speichern**sichtbar** Arbeitsblätter in einer Arbeitsmappe in eine PDF-Datei umwandeln. Mit**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** Mit dieser Option können Sie bestimmte Arbeitsblätter in einer PDF-Datei speichern. Sie können beispielsweise das aktive Arbeitsblatt im PDF-Format speichern, alle Arbeitsblätter (sowohl sichtbare als auch versteckte Arbeitsblätter) im PDF-Format speichern und mehrere benutzerdefinierte Arbeitsblätter im PDF-Format speichern.

##  **Speichern Sie das aktive Arbeitsblatt unter PDF**

 Wenn Sie nur das aktive Blatt als PDF exportieren möchten, können Sie dies durch Übergeben erreichen**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** Zu**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** Möglichkeit.

 Das Blatt `Sheet2` ist das aktive Blatt der Quelldatei[sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **Speichern Sie alle Arbeitsblätter unter PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** zeigt sichtbare Blätter in einer Arbeitsmappe an und**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** gibt alle Blätter an, einschließlich sichtbarer Blätter und ausgeblendeter/unsichtbarer Blätter in einer Arbeitsmappe. Wenn Sie alle Blätter als PDF exportieren möchten, können Sie einfach bestehen**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** Zu**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** Möglichkeit.

 Die Quelldatei[sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit verstecktem Blatt `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **Speichern Sie die angegebenen Arbeitsblätter unter PDF**
 Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter als PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattindizes an übergeben**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** Möglichkeit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) auf, bevor Sie die Tabelle in das Format PDF rendern. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
