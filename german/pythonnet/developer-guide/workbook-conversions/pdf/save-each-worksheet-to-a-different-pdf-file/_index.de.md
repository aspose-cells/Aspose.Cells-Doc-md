---
title: Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei
type: docs
weight: 130
url: /de/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Erfahren Sie, wie Sie jedes Arbeitsblatt mit Aspose.Cells for Python via .NET API in einer anderen PDF-Datei speichern.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for Python via .NET kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren, und Sie müssen Aspose.PDF for .NET nicht für die Konvertierung verwenden. Für die Konvertierung ist es nicht erforderlich, dass die Software temporäre Dateien erstellt oder verwendet, da der gesamte Vorgang im Speicher durchgeführt werden kann.

{{% /alert %}} 
##  **Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei**
 Wenn Sie jedes Arbeitsblatt in Ihrer Excel-Vorlagedatei speichern müssen, um verschiedene PDF-Dateien zu generieren, können Sie dies problemlos erreichen. Sie können versuchen, einen Blattindex auf festzulegen**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** Option nacheinander zum Rendern auf PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
