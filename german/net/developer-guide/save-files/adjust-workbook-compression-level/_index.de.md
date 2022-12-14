---
title: Passen Sie die Komprimierungsstufe der Arbeitsmappe an
type: docs
weight: 180
url: /de/net/adjust-workbook-compression-level/
---
## **Passen Sie die Komprimierungsstufe der Arbeitsmappe an**

Entwickler können die Komprimierungsstufe der Arbeitsmappe anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen gegenüber der Verarbeitungszeit priorisieren oder umgekehrt. Aspose.Cells bietet**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** Enumeration, mit der Sie die Komprimierungsstufe der Arbeitsmappe festlegen können. Das**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** Enumeration stellt die folgenden Elemente bereit.

- Level1: Die schnellste, aber am wenigsten effektive Komprimierung.
- Level2: Etwas langsamer, aber besser als Level 1.
- Level3: Etwas langsamer, aber besser als Level 2.
- Level4: Etwas langsamer, aber besser als Level 3.
- Level5: Etwas langsamer als Level 4, aber mit besserer Komprimierung.
- Level6: Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionseffizienz.
- Level7: Ziemlich gute Komprimierung!
- Level8: Bessere Komprimierung als Level7!
- Level9: Die „beste“ Komprimierung, wobei „best“ die größte Verringerung der Größe des Eingangsdatenstroms bedeutet. Dies ist auch die langsamste Komprimierung.

 Das folgende Code-Snippet demonstriert die Verwendung von**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**Enumeration und vergleicht die Konvertierungszeit für Level1, Level6 und Level9. Sie können auch die Größen der generierten Dateien vergleichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
