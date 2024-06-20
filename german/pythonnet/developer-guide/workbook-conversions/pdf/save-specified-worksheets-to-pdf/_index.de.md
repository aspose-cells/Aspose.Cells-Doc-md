---
title: Gewählte Arbeitsblätter als PDF speichern
type: docs
weight: 140
url: /de/python-net/save-specified-worksheets-to-pdf/
description: Erfahren Sie, wie Sie spezifische Arbeitsblätter mit der Aspose.Cells für Python via .NET API als PDF speichern können.
keywords: Python Aktives Arbeitsblatt als PDF speichern, Alle Arbeitsblätter als PDF speichern, Spezifische Arbeitsblätter als PDF speichern
---

Standardmäßig speichert Aspose.Cells für Python via .NET alle **sichtbaren** Arbeitsblätter in einer Arbeitsmappe in einer PDF-Datei. Mit [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)-Option können Sie bestimmte Arbeitsblätter in einer PDF-Datei speichern. z. B. Sie können ein aktives Arbeitsblatt in PDF speichern, alle Arbeitsblätter (sowohl sichtbare als auch ausgeblendete Arbeitsblätter) in PDF speichern, benutzerdefinierte Arbeitsblätter in PDF speichern.

## **Aktives Arbeitsblatt als PDF speichern**

Wenn Sie nur das aktive Tabellenblatt in PDF exportieren möchten, können Sie dies erreichen, indem Sie [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) an [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) übergeben.

Das Blatt `Blatt2` ist das aktive Blatt der Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Alle Arbeitsblätter als PDF speichern**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) zeigt die sichtbaren Blätter in einer Arbeitsmappe an, und [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) zeigt alle Blätter an, einschließlich sowohl der sichtbaren Blätter als auch der ausgeblendeten/unsichtbaren Blätter in einer Arbeitsmappe. Wenn Sie alle Blätter in PDF exportieren möchten, können Sie einfach [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) an [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) übergeben.

Die Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit dem versteckten Blatt `Blatt3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Bestimmte Arbeitsblätter als PDF speichern**
Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter in PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattindizes an [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)-Option übergeben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
