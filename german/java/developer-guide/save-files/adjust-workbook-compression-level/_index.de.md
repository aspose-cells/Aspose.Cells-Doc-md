---
title: Einstellen des Arbeitsmappenkompressionsniveaus
type: docs
weight: 130
url: /de/java/adjust-workbook-compression-level/
---

## **Anpassen des Arbeitsmappe-Komprimierungsgrads**

Entwickler können den Kompressionsgrad der Arbeitsmappe anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen über die Verarbeitungszeit oder umgekehrt priorisieren. Aspose.Cells bietet die [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)-Enumeration, die Sie verwenden können, um den Kompressionsgrad der Arbeitsmappe festzulegen. Die [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)-Enumeration bietet die folgenden Elemente.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1): Die schnellste, aber am wenigsten effektive Kompression.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2): Etwas langsamer, aber besser als Level 1.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3): Etwas langsamer, aber besser als Level 2.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4): Etwas langsamer, aber besser als Level 3.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5): Etwas langsamer als Level 4, aber mit besserer Kompression.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6): Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionswirkungsgrad.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7): Ziemlich gute Kompression!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8): Bessere Kompression als Level7!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9): Die "beste" Kompression, wobei best bedeutet, dass die Größe des Eingabedatenstroms am stärksten reduziert wird. Dies ist auch die langsamste Kompression.

Der folgende Codeausschnitt zeigt die Verwendung der [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)-Enumeration und vergleicht die Konvertierungszeit für [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6) und [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9). Sie können auch die Größen der generierten Dateien vergleichen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
