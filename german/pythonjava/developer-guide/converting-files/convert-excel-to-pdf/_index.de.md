---
title: Konvertieren Sie Excel in PDF
type: docs
weight: 50
url: /de/python-java/convert-excel-to-pdf/
description: Wie man Excel mit Python in PDF konvertiert.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Konvertieren Sie Excel in PDF**

PDF-Dokumente werden häufig als Standardformat für den Austausch von Dokumenten zwischen Organisationen, Regierungssektoren und Einzelpersonen verwendet. Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft-Excel-Dateien einfach in PDF-Dokumente umzuwandeln. Aspose.Cells for Python via Java API bietet die Möglichkeit, Excel-Dateien in PDF-Dokumente (einschließlich PDF/A) zu konvertieren. Aspose.Cell konvertiert Tabellenkalkulationen mit einem hohen Maß an Genauigkeit und Wiedergabetreue in PDF.

### **Direkte Konvertierung**

Um eine Excel-Datei direkt unter PDF zu speichern, können Sie die verwenden[**Arbeitsmappe.speichern**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) Methode und Pass[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) als zweiter Parameter.

Das folgende Code-Snippet demonstriert die Verwendung von[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)und die[**Arbeitsmappe.speichern**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))-Methode zum Konvertieren von Excel in das PDF-Format.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Erweiterte Konvertierung**

Um mehr Kontrolle über die Umwandlung in PDF zu haben, bietet die API die[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)Klasse. Das[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)-Klasse können verschiedene Attribute für die Konvertierung gesetzt werden. Festlegen verschiedener Eigenschaften der[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)-Klasse gibt Ihnen die Kontrolle über die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die resultierende PDF-Datei. Die bemerkenswerteste Eigenschaft ist die[**Beachtung**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)Damit können Sie die Excel-Dateien in PDF/A-kompatible PDF-Dateien speichern.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 Wenn Ihre Tabelle Formeln enthält, rufen Sie die auf[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula())-Methode direkt vor dem Rendern der Tabelle in PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte in PDF gerendert werden.

{{% /alert %}}
