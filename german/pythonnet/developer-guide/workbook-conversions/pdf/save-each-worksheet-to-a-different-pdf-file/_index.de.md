---
title: Jede Arbeitsblatt in eine separate PDF Datei speichern
type: docs
weight: 130
url: /de/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Lernen Sie, wie Sie mit der Aspose.Cells für Python via .NET API jede Arbeitsmappe in eine separate PDF Datei speichern.
keywords: Python Jede Arbeitsmappe in eine separate PDF Datei speichern
---

{{% alert color="primary" %}} 

Aspose.Cells für Python via .NET unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells für Python via .NET kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren, und Sie müssen Aspose.PDF für die Konvertierung nicht verwenden. Der Vorgang erfordert keine temporären Dateien, da der gesamte Prozess im Speicher durchgeführt werden kann.

{{% /alert %}} 
## **Jedes Arbeitsblatt in eine separate PDF-Datei speichern**
Wenn Sie jedes Arbeitsblatt in Ihrer Vorlagen-Excel-Datei speichern möchten, um verschiedene PDF-Dateien zu generieren, können Sie dies einfach erreichen. Sie können versuchen, eine Blattindexierungsoption auf [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) festzulegen, um es einzeln in PDF zu rendern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
