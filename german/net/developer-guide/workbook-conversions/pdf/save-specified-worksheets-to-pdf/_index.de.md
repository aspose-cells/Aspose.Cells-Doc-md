---
title: Gewählte Arbeitsblätter als PDF speichern
type: docs
weight: 140
url: /de/net/save-specified-worksheets-to-pdf/
---

Standardmäßig speichert Aspose.Cells alle **sichtbaren** Arbeitsblätter in einer Arbeitsmappe in einer PDF-Datei. Mit der Option [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) können Sie bestimmte Arbeitsblätter in einer PDF-Datei speichern. z.B.: Sie können das aktive Arbeitsblatt in PDF speichern, alle Arbeitsblätter (sowohl sichtbare als auch ausgeblendete Arbeitsblätter) in PDF speichern, benutzerdefinierte mehrere Arbeitsblätter in PDF speichern.

## **Aktives Arbeitsblatt als PDF speichern**

Wenn Sie nur das aktive Tabellenblatt in PDF exportieren möchten, können Sie dies erreichen, indem Sie [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) an [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) übergeben.

Das Blatt `Blatt2` ist das aktive Blatt der Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Alle Arbeitsblätter als PDF speichern**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) zeigt die sichtbaren Blätter in einer Arbeitsmappe an, und [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) zeigt alle Blätter an, einschließlich sowohl der sichtbaren Blätter als auch der ausgeblendeten/unsichtbaren Blätter in einer Arbeitsmappe. Wenn Sie alle Blätter in PDF exportieren möchten, können Sie einfach [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) an [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) übergeben.

Die Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit dem versteckten Blatt `Blatt3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Bestimmte Arbeitsblätter als PDF speichern**
Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter in PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattindizes an [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)-Option übergeben.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **Arbeitsblätter nach PDF neu anordnen**

Wenn Sie Blätter (z. B. in umgekehrter Reihenfolge) nach PDF umordnen möchten, ohne die Quelldatei zu ändern, können Sie dies erreichen, indem Sie die umgeordneten Blattindizes an die [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) Option übergeben.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
