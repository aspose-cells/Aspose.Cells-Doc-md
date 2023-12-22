---
title: Neuabtastung hinzugefügter Bilder – Konvertierung von Excel in PDF
type: docs
weight: 150
url: /de/python-net/resample-added-images-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie hinzugefügte Bilder beim Konvertieren von Excel in PDF mit Aspose.Cells for Python via .NET API neu berechnen.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

Wenn Sie mit großen Microsoft Excel-Dateien mit vielen Bildern arbeiten, müssen Sie möglicherweise hinzugefügte Bilder komprimieren, um die Größe der Ausgabedatei zu reduzieren und die Konvertierungsleistung insgesamt zu verbessern. Aspose.Cells for Python via .NET unterstützt das Resampling hinzugefügter Bilder, um die Größe der Ausgabedatei zu reduzieren und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte sehen Sie sich den folgenden Beispielcode an, der beschreibt, wie die Aufgabe mit Aspose.Cells for Python via .NET API ausgeführt wird. Das Beispiel konvertiert eine Excel-Datei Microsoft in eine Datei PDF und komprimiert dabei die Bilder in der Datei.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 Mit dem[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)Diese Option minimiert die Größe der Ausgabe PDF, kann jedoch die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
