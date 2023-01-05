---
title: Resampling von Bildern für Excel in PDF-Konvertierung
type: docs
weight: 250
url: /de/java/resample-images-for-excel-to-pdf-conversion/
description: Dieser Artikel demonstriert das Reduzieren der Bildgröße beim Konvertieren von Excel-Dateien in PDF
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

Beim Arbeiten mit großen Microsoft Excel-Dateien mit vielen Bildern müssen Sie eventuell hinzugefügte Bilder komprimieren, um die Größe der PDF Ausgabedatei zu reduzieren und die Konvertierungsleistung insgesamt zu verbessern. Aspose.Cells unterstützt das Resampling hinzugefügter Bilder, um die Ausgabedateigröße PDF zu reduzieren und die Leistung zu verbessern.

{{% /alert %}}

## **Resampling von Bildern für Excel in PDF-Konvertierung**

Bitte sehen Sie sich den folgenden Beispielcode an, der beschreibt, wie die Aufgabe mit Aspose.Cells API ausgeführt wird. Das Beispiel konvertiert eine Microsoft-Excel-Datei in eine PDF-Datei, während die Bilder in der Datei komprimiert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 Verwendung der[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) Option minimiert die Größe der Ausgabe PDF, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte in PDF wiedergegeben werden.

{{% /alert %}}
