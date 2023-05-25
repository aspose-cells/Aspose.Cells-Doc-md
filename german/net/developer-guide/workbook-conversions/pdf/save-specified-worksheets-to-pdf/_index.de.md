---
title: Speichern Sie die angegebenen Arbeitsblätter unter PDF
type: docs
weight: 140
url: /de/net/save-specified-worksheets-to-pdf/
---
 Standardmäßig ist Aspose.Cells alles speichern**sichtbar** Arbeitsblätter in einer Arbeitsmappe in eine PDF-Datei umwandeln. Mit**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** Mit dieser Option können Sie bestimmte Arbeitsblätter in einer PDF-Datei speichern. Sie können beispielsweise das aktive Arbeitsblatt im PDF-Format speichern, alle Arbeitsblätter (sowohl sichtbare als auch versteckte Arbeitsblätter) im PDF-Format speichern und mehrere benutzerdefinierte Arbeitsblätter im PDF-Format speichern.

##  **Speichern Sie das aktive Arbeitsblatt unter PDF**

 Wenn Sie nur das aktive Blatt als PDF exportieren möchten, können Sie dies durch Übergeben erreichen**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** Zu**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** Möglichkeit.

 Das Blatt `Sheet2` ist das aktive Blatt der Quelldatei[sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **Speichern Sie alle Arbeitsblätter unter PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** zeigt sichtbare Blätter in einer Arbeitsmappe an und**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** gibt alle Blätter an, einschließlich sichtbarer Blätter und ausgeblendeter/unsichtbarer Blätter in einer Arbeitsmappe. Wenn Sie alle Blätter als PDF exportieren möchten, können Sie einfach bestehen**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** Zu**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** Möglichkeit.

 Die Quelldatei[sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit verstecktem Blatt `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **Speichern Sie die angegebenen Arbeitsblätter unter PDF**
 Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter als PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattindizes an übergeben**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** Möglichkeit.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) auf, bevor Sie die Tabelle in das Format PDF rendern. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
