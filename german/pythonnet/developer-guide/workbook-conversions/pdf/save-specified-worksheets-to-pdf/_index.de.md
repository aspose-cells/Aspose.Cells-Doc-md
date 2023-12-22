---
title: Speichern Sie die angegebenen Arbeitsblätter unter PDF
type: docs
weight: 140
url: /de/python-net/save-specified-worksheets-to-pdf/
description: Erfahren Sie, wie Sie bestimmte Arbeitsblätter unter PDF mit Aspose.Cells for Python via .NET API speichern.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 Standardmäßig Aspose.Cells for Python via .NET Alle speichern**sichtbar** Arbeitsblätter in einer Arbeitsmappe in eine PDF-Datei umwandeln. Mit**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** Mit dieser Option können Sie bestimmte Arbeitsblätter in einer PDF-Datei speichern. Sie können beispielsweise das aktive Arbeitsblatt im PDF-Format speichern, alle Arbeitsblätter (sowohl sichtbare als auch versteckte Arbeitsblätter) im PDF-Format speichern und mehrere benutzerdefinierte Arbeitsblätter im PDF-Format speichern.

##  **Speichern Sie das aktive Arbeitsblatt unter PDF**

Wenn Sie nur das aktive Blatt als PDF exportieren möchten, können Sie dies durch Übergeben erreichen**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** Zu**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** Möglichkeit.

 Das Blatt `Sheet2` ist das aktive Blatt der Quelldatei[sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Speichern Sie alle Arbeitsblätter unter PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** zeigt sichtbare Blätter in einer Arbeitsmappe an und**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** gibt alle Blätter an, einschließlich sichtbarer Blätter und ausgeblendeter/unsichtbarer Blätter in einer Arbeitsmappe. Wenn Sie alle Blätter als PDF exportieren möchten, können Sie einfach bestehen**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** Zu**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** Möglichkeit.

 Die Quelldatei[sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit verstecktem Blatt `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Speichern Sie die angegebenen Arbeitsblätter unter PDF**
 Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter als PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattindizes an übergeben**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** Möglichkeit.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
