---
title: Einstellen des Arbeitsmappenkompressionsniveaus
type: docs
weight: 180
url: /de/python-net/adjust-workbook-compression-level/
---

## **Arbeitsmappenkompressionsniveau anpassen**

Entwickler können den Kompressionsgrad des Arbeitsbuchs beim Arbeiten mit größeren Arbeitsbüchern anpassen. Entwickler können kleinere Dateigrößen gegenüber der Verarbeitungszeit priorisieren oder umgekehrt. Aspose.Cells für Python via .NET bietet die Enumeration [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype), mit der Sie den Kompressionsgrad festlegen können. Die Enumeration [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) bietet die folgenden Mitglieder.

- Level1: Die schnellste, aber am wenigsten effektive Kompression.
- Level2: Etwas langsamer, aber besser als Level 1.
- Stufe3: Etwas langsamer, aber besser als Stufe 2.
- Stufe4: Etwas langsamer, aber besser als Stufe 3.
- Stufe5: Etwas langsamer als Stufe 4, aber mit besserer Kompression.
- Stufe6: Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionseffizienz.
- Stufe7: Ziemlich gute Kompression!
- Stufe8: Bessere Kompression als Stufe7!
- Stufe9: Die "beste" Kompression, wobei beste die größte Reduzierung der Größe des Eingabedatenstroms bedeutet. Dies ist auch die langsamste Kompression.

Der folgende Codeausschnitt zeigt die Verwendung der [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) Enumeration und vergleicht die Konvertierungszeit für Level1, Level6 und Level9. Sie können auch die Größen der generierten Dateien vergleichen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

