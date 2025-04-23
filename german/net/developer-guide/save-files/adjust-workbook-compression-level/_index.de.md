---
title: Einstellen des Arbeitsmappenkompressionsniveaus
type: docs
weight: 180
url: /de/net/adjust-workbook-compression-level/
---

## **Arbeitsmappenkompressionsniveau anpassen**

Entwickler können den Komprimierungsgrad der Arbeitsmappe anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen höher priorisieren als die Verarbeitungszeit oder umgekehrt. Aspose.Cells stellt die [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) Enumeration bereit, die zur Festlegung des Komprimierungsgrads der Arbeitsmappe verwendet werden kann. Die [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) Enumeration bietet die folgenden Elemente.

- Level1: Die schnellste, aber am wenigsten effektive Kompression.
- Level2: Etwas langsamer, aber besser als Level 1.
- Stufe3: Etwas langsamer, aber besser als Stufe 2.
- Stufe4: Etwas langsamer, aber besser als Stufe 3.
- Stufe5: Etwas langsamer als Stufe 4, aber mit besserer Kompression.
- Stufe6: Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionseffizienz.
- Stufe7: Ziemlich gute Kompression!
- Stufe8: Bessere Kompression als Stufe7!
- Stufe9: Die "beste" Kompression, wobei beste die größte Reduzierung der Größe des Eingabedatenstroms bedeutet. Dies ist auch die langsamste Kompression.

Der folgende Codeausschnitt zeigt die Verwendung der [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) Enumeration und vergleicht die Konvertierungszeit für Level1, Level6 und Level9. Sie können auch die Größen der generierten Dateien vergleichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
