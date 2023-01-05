---
title: Passen Sie die Komprimierungsstufe der Arbeitsmappe an
type: docs
weight: 130
url: /de/java/adjust-workbook-compression-level/
---
## **Passen Sie die Komprimierungsstufe der Arbeitsmappe an**

Entwickler können die Komprimierungsstufe der Arbeitsmappe anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen gegenüber der Verarbeitungszeit priorisieren oder umgekehrt. Aspose.Cells bietet**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**Enumeration, mit der Sie die Komprimierungsstufe der Arbeitsmappe festlegen können. Das**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** Enumeration stellt die folgenden Elemente bereit.

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: Die schnellste, aber am wenigsten effektive Komprimierung.
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: Etwas langsamer, aber besser als Stufe 1.
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**Etwas langsamer, aber besser als Stufe 2.
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: Etwas langsamer, aber besser als Stufe 3.
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: Etwas langsamer als Stufe 4, aber mit besserer Komprimierung.
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: Eine gute Balance zwischen Geschwindigkeit und Kompressionseffizienz.
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: Ziemlich gute Komprimierung!
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Bessere Komprimierung als Level7!
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**Die „beste“ Komprimierung, wobei am besten die größte Verringerung der Größe des Eingangsdatenstroms bedeutet. Dies ist auch die langsamste Komprimierung.

Das folgende Code-Snippet demonstriert die Verwendung von**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** Aufzählung und vergleicht die Konvertierungszeit für**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** , und**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. Sie können auch die Größen der generierten Dateien vergleichen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
