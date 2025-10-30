---
title: XLS Datei mit Bildern oder Diagrammen mit Golang via C++ in PDF umwandeln
linktitle: Konvertierung von XLS Datei mit Bildern oder Diagrammen in PDF
type: docs
weight: 50
url: /de/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: XLS Dateien mit Bildern oder Diagrammen in PDF Dokumente umwandeln mit Aspose.Cells unter Golang via C++.
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien, die Bilder und Diagramme enthalten, in PDF-Dokumente. Aspose.Cells for C++ kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren: Für die Konvertierung ist kein Aspose.PDF für C++ erforderlich. Der Vorgang kann im Speicher durchgeführt werden, da er nicht von temporären oder Zwischen-XML-Dateien abhängt. Das bedeutet, dass große Excel-Dateien, z. B. solche mit Bildern, Diagrammen und anderen Zeichenobjekten, schnell und effizient konvertiert werden können.

{{% /alert %}} 
## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) kurz vor der Umwandlung in PDF aufzurufen. Dadurch wird sichergestellt, dass Formelbehaftete Werte neu berechnet werden und die korrekten Werte im PDF angezeigt werden.

{{% /alert %}}
