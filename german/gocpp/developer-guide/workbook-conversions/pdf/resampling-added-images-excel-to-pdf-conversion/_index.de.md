---
title: Resampling Hinzugefügter Bilder  Excel in PDF Konvertierung mit Golang via C++
linktitle: Hinzufügen von neu abgetasteten Bildern  Excel in PDF Konvertierung
type: docs
weight: 150
url: /de/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Lernen Sie, wie Sie hinzugefügte Bilder neu abtasten, um die PDF Größe mit Aspose.Cells in Golang via C++ zu reduzieren.
---

{{% alert color="primary" %}}

Bei der Arbeit mit großen Microsoft Excel-Dateien mit vielen Bildern müssen Sie möglicherweise Bilder komprimieren, die hinzugefügt wurden, um die Größe der Ausgabepdf-Datei zu reduzieren und die Gesamtwandlungsleistung zu verbessern. Aspose.Cells unterstützt das Neuabtasten von hinzugefügten Bildern, um die Größe der Ausgabepdf-Datei zu reduzieren und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte beachten Sie den folgenden Beispiellcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells-API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Die Verwendung der [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/)-Option minimiert die Größe der Ausgabe-PDF, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} 

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}

