---
title: Excel in Markdown konvertieren
type: docs
weight: 30
url: /de/python-java/convert-excel-to-markdown/
---

## **Excel in Markdown konvertieren**
Aspose.Cells for Python via Java unterstützt die Konvertierung von Excel-Dateien in das Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, geben Sie [SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN) als den zweiten Parameter der [Workbook.Save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) Methode an. Sie können auch die [MarkdownSaveOptions](https://reference.aspose.com/cells/python/asposecells.api/MarkdownSaveOptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export von Arbeitsblättern in Markdown festzulegen.

Das folgende Codebeispiel veranschaulicht, wie das aktive Arbeitsblatt in Markdown exportiert wird, indem das Enumerationsmitglied [SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN) verwendet wird. Bitte beachten Sie die durch den Code generierte [Ausgabemarke-Datei](Book1.txt) als Referenz.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToMarkdownFiles.py" >}}
