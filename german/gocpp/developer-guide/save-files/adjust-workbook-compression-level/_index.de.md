---
title: Arbeitsbuch Komprimierungsstufe mit Golang über C++ anpassen
linktitle: Arbeitsmappen Komprimierungsgrad anpassen
type: docs
weight: 180
url: /de/go-cpp/adjust-workbook-compression-level/
description: Lernen Sie, wie Sie den Komprimierungsgrad einer Arbeitsmappe mit Aspose.Cells for C++ anpassen, um Dateigröße und Verarbeitungszeit zu optimieren.
---

## **Arbeitsmappenkompressionsniveau anpassen**

Entwickler können den Komprimierungsgrad der Arbeitsmappe anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen höher priorisieren als die Verarbeitungszeit oder umgekehrt. Aspose.Cells stellt die [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) Enumeration bereit, die zur Festlegung des Komprimierungsgrads der Arbeitsmappe verwendet werden kann. Die [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) Enumeration bietet die folgenden Elemente.

- Level1: Die schnellste, aber am wenigsten effektive Kompression.
- Level2: Etwas langsamer, aber besser als Level 1.
- Stufe3: Etwas langsamer, aber besser als Stufe 2.
- Stufe4: Etwas langsamer, aber besser als Stufe 3.
- Stufe5: Etwas langsamer als Stufe 4, aber mit besserer Kompression.
- Stufe6: Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionseffizienz.
- Stufe7: Ziemlich gute Kompression!
- Stufe8: Bessere Kompression als Stufe7!
- Stufe9: Die "beste" Kompression, wobei beste die größte Reduzierung der Größe des Eingabedatenstroms bedeutet. Dies ist auch die langsamste Kompression.

Der folgende Codeausschnitt zeigt die Verwendung der [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) Enumeration und vergleicht die Konvertierungszeit für Level1, Level6 und Level9. Sie können auch die Größen der generierten Dateien vergleichen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}
