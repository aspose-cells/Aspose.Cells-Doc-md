---
title: Excel in PDF konvertieren
type: docs
weight: 50
url: /de/python-java/convert-excel-to-pdf/
description: Wie man Excel mit Python in PDF konvertiert. Dieser Artikel zeigt, wie man Excel Dateien mit Python und der benutzerfreundlichen Aspose.Cells for Python via Java API in PDF umwandelt.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Excel in PDF konvertieren**

PDF-Dokumente werden weitläufig als Standardformat zum Austausch von Dokumenten zwischen Organisationen, Regierungsbehörden und Einzelpersonen verwendet. Softwareentwickler werden häufig gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien einfach in PDF-Dokumente umzuwandeln. Die Aspose.Cells for Python via Java-API bietet die Möglichkeit, Excel-Dateien in PDF-Dokumente (einschließlich PDF/A) zu konvertieren. Aspose.Cells konvertiert Tabellenkalkulationen mit einer hohen Genauigkeit und Treuehaftigkeit in PDF.

### **Direkte Konvertierung**

Um eine Excel-Datei direkt als PDF zu speichern, können Sie die [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))-Methode verwenden und [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) als zweiten Parameter übergeben.

Der folgende Code-Schnipsel demonstriert die Verwendung der Methode [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) und der Methode [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) zur Konvertierung von Excel in das PDF-Format.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Erweiterte Konvertierung**

Um mehr Kontrolle über die Konvertierung in PDF zu haben, bietet die API die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) an. Die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) kann verwendet werden, um verschiedene Attribute für die Konvertierung festzulegen. Die Einstellung verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) gibt Ihnen Kontrolle über die Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für die resultierende PDF-Datei. Die wichtigste Eigenschaft ist [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance), die es Ihnen ermöglicht, die Excel-Dateien in PDF/A-konforme PDF-Dateien zu speichern.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, rufen Sie die Methode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) kurz vor dem Rendern der Tabelle in PDF auf. Dies stellt sicher, dass die von den Formeln abhängigen Werte neu berechnet werden und die richtigen Werte im PDF dargestellt werden.

{{% /alert %}}
