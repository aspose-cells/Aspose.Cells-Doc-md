---
title: Bilder für die Umwandlung von Excel in PDF neu anordnen
type: docs
weight: 250
url: /de/java/resample-images-for-excel-to-pdf-conversion/
description: Dieser Artikel zeigt, wie Bilddateien beim Konvertieren von Excel Dateien in PDF verkleinert werden.
keywords: Excel zu PDF, Bilder beim Konvertieren von Excel zu PDF erneut anordnen, Bilder beim Konvertieren von Excel zu PDF komprimieren, Bildgrößen beim Konvertieren von Excel zu PDF reduzieren, Excel in PDF mit kleinerer Größe konvertieren, Excel in PDF mit Bildneuanordnung konvertieren, Excel in PDF mit Bildkompression konvertieren, Bilder beim Konvertieren von Excel zu PDF in Java komprimieren
---

{{% alert color="primary" %}}

Wenn Sie mit großen Microsoft Excel-Dateien arbeiten, die viele Bilder enthalten, müssen Sie möglicherweise die hinzugefügten Bilder komprimieren, um die Größe der Ausgabedatei zu verringern und die allgemeine Konvertierungsleistung zu verbessern. Aspose.Cells unterstützt das Neuabtasten hinzugefügter Bilder, um die Größe der Ausgabedatei zu reduzieren und die Leistung zu verbessern.

{{% /alert %}}

## **Bilder für die Umwandlung von Excel in PDF neu anordnen**

Bitte beachten Sie den folgenden Beispiellcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells-API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

Die Verwendung der [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample-int-int-)-Option minimiert die Größe der Ausgabe-PDF, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
