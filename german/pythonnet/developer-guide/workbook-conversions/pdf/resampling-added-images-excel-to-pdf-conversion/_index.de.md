---
title: Erneut hinzugefügte Bilder neu sampeln  Excel zu PDF Konvertierung
type: docs
weight: 150
url: /de/python-net/resample-added-images-excel-to-pdf-conversion/
description: Lernen Sie, wie Sie beim Konvertieren von Excel in PDF mit Aspose.Cells für Python via .NET API hinzugefügte Bilder neu abtasten.
keywords: Python Neuabtasten hinzugefügter Bilder beim Konvertieren von Excel in PDF
---

{{% alert color="primary" %}}

Beim Arbeiten mit großen Microsoft Excel-Dateien mit vielen Bildern müssen möglicherweise die hinzugefügten Bilder komprimiert werden, um die Größe der Ausgabedatei zu reduzieren und die gesamte Konverterleistung zu verbessern. Aspose.Cells für Python via .NET unterstützt das Neuabtasten hinzugefügter Bilder, um die Größe der Ausgabedatei zu reduzieren und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte beachten Sie den folgenden Beispielcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells für Python via .NET API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

Die Verwendung der Option [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) minimiert die Größe des Ausgabepdfs, kann jedoch die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
