---
title: Hinzufügen von neu abgetasteten Bildern  Excel in PDF Konvertierung
type: docs
weight: 150
url: /de/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Bei der Arbeit mit großen Microsoft Excel-Dateien mit vielen Bildern müssen Sie möglicherweise Bilder komprimieren, die hinzugefügt wurden, um die Größe der Ausgabepdf-Datei zu reduzieren und die Gesamtwandlungsleistung zu verbessern. Aspose.Cells unterstützt das Neuabtasten von hinzugefügten Bildern, um die Größe der Ausgabepdf-Datei zu reduzieren und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte beachten Sie den folgenden Beispiellcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells-API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

Die Verwendung der Option [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) minimiert die Größe des Ausgabepdfs, kann jedoch die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
