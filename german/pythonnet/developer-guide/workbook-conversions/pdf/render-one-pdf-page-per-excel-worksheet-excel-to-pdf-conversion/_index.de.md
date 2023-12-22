---
title: Rendern Sie eine PDF-Seite pro Excel-Arbeitsblatt – Konvertierung von Excel in PDF
type: docs
weight: 100
url: /de/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie eine PDF-Seite pro Excel-Arbeitsblatt rendern und dabei Excel in PDF mit Aspose.Cells for Python via .NET API konvertieren.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

Wenn Sie mit großen Microsoft-Excel-Dateien arbeiten (z. B. einer Arbeitsmappe mit vielen Blättern mit jeweils 50 Spalten und 300 oder mehr Datenzeilen), möchten Sie möglicherweise, dass in der PDF-Ausgabe eine Seite pro Arbeitsblatt angezeigt wird, unabhängig von der Größe des Arbeitsblatts . Dies würde bedeuten, dass jede Seite wahrscheinlich eine völlig andere Seitengröße hat. Dies kann durch die Verwendung von Aspose.Cells for Python via .NET API erreicht werden.

{{% /alert %}} 

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Wenn die[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)Wenn die Option auf *true** gesetzt ist, wird der gesamte Blattinhalt auf einer PDF-Seite gerendert.

{{% /alert %}} {{% alert color="primary" %}} 

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) Methode direkt vor dem Rendern der Tabelle in PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte in PDF gerendert werden.

{{% /alert %}}
