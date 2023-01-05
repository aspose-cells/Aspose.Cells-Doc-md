---
title: Resampling hinzugefügter Bilder – Konvertierung von Excel in PDF
type: docs
weight: 150
url: /de/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Beim Arbeiten mit großen Microsoft Excel-Dateien mit vielen Bildern müssen Sie eventuell hinzugefügte Bilder komprimieren, um die Größe der PDF Ausgabedatei zu reduzieren und die Konvertierungsleistung insgesamt zu verbessern. Aspose.Cells unterstützt das Resampling hinzugefügter Bilder, um die Ausgabedateigröße PDF zu reduzieren und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte sehen Sie sich den folgenden Beispielcode an, der beschreibt, wie die Aufgabe mit Aspose.Cells API ausgeführt wird. Das Beispiel konvertiert eine Microsoft-Excel-Datei in eine PDF-Datei, während die Bilder in der Datei komprimiert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

 Unter Verwendung der[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)Option minimiert die Größe der Ausgabe PDF, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte in PDF wiedergegeben werden.

{{% /alert %}}
