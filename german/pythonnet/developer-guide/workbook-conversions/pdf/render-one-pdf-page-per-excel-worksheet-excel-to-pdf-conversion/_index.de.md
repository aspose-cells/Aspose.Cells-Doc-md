---
title: Ein PDF Seite pro Excel Arbeitsblatt rendern  Konvertierung von Excel in PDF
type: docs
weight: 100
url: /de/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie eine PDF Seite pro Excel Arbeitsblatt rendern, während Sie Excel zu PDF mit Aspose.Cells für Python via .NET API konvertieren.
keywords: Python Render Eine PDF Seite Pro Excel Arbeitsblatt beim Speichern in PDF, Eine PDF Seite Pro Excel Arbeitsblatt beim Speichern von Excel in PDF mit Python, Python zeigt eine Seite pro Arbeitsblatt beim Konvertieren von Excel in PDF
---

{{% alert color="primary" %}} 

Wenn Sie mit großen Microsoft Excel-Dateien arbeiten (zum Beispiel mit einer Arbeitsmappe, die viele Blätter mit jeweils 50 Spalten und 300 oder mehr Zeilen Daten enthält), möchten Sie möglicherweise, dass die PDF-Ausgabe unabhängig von der Größe des Arbeitsblatts eine Seite pro Arbeitsblatt anzeigt. Dies bedeutet, dass jede Seite wahrscheinlich eine radikal andere Seitengröße aufweist. Dies kann mit der Aspose.Cells for Python via .NET API erreicht werden.

{{% /alert %}} 

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

Wenn die Option [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) auf **true** gesetzt ist, wird der gesamte Blattinhalt auf eine PDF-Seite gerendert.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Ihre Tabellenkalkulation Formeln enthält, ist es am besten, die Methode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) unmittelbar vor dem Rendern der Tabellenkalkulation in PDF aufzurufen. Dadurch wird sichergestellt, dass die von den Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
