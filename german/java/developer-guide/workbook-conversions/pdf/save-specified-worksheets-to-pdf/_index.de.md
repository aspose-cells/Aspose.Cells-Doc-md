---
title: Gewählte Arbeitsblätter als PDF speichern
type: docs
weight: 51
url: /de/java/save-specified-worksheets-to-pdf/
---

Standardmäßig speichert Aspose.Cells alle **sichtbaren** Arbeitsblätter in einer Arbeitsmappe in einer PDF-Datei. Mit der Option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) können Sie bestimmte Arbeitsblätter in einer PDF-Datei speichern. z.B.: Sie können das aktive Arbeitsblatt in PDF speichern, alle Arbeitsblätter (sowohl sichtbare als auch ausgeblendete Arbeitsblätter) in PDF speichern, benutzerdefinierte mehrere Arbeitsblätter in PDF speichern.

## **Aktives Arbeitsblatt als PDF speichern**

Wenn Sie nur das aktive Tabellenblatt in PDF exportieren möchten, können Sie dies erreichen, indem Sie [**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--) an [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) übergeben.

Das Blatt `Blatt2` ist das aktive Blatt der Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **Alle Arbeitsblätter als PDF speichern**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--) zeigt die sichtbaren Blätter in einer Arbeitsmappe an, und [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) zeigt alle Blätter an, einschließlich sowohl der sichtbaren Blätter als auch der ausgeblendeten/unsichtbaren Blätter in einer Arbeitsmappe. Wenn Sie alle Blätter in PDF exportieren möchten, können Sie einfach [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) an [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) übergeben.

Die Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit dem versteckten Blatt `Blatt3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **Bestimmte Arbeitsblätter als PDF speichern**
Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter in PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattindizes an [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)-Option übergeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
