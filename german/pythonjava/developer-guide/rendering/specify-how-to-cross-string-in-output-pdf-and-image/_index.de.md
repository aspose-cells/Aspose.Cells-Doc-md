---
title: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 20
url: /de/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Angeben, wie Zeilenumbruch im Ausgabe-PDF und Bild erfolgen soll**
Wenn eine Zelle Text oder einen String enthält, der breiter ist als die Zelle selbst, dann wird der Text überlaufen, wenn die benachbarte Zelle in der nächsten Spalte leer ist. Beim Speichern Ihrer Excel-Datei als PDF/Bild können Sie diesen Überlauf kontrollieren, indem Sie den Übergangstyp mit der Aufzählung [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) festlegen. Diese Aufzählung hat die folgenden Werte:

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Wie in MS Excel angezeigt, abhängig von der nächsten Zelle. Wenn die nächste Zelle leer ist, wird der Text überlaufen oder er wird abgeschnitten.
- [TextCrossType.CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : Zeigt den Text ähnlich dem Export von MS Excel in PDF/Bild
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : Zeigt den gesamten Text, wobei er andere Zellen überquert und den Text der überquerten Zellen überschreibt
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : Zeigt nur den Text innerhalb der Breite der Zelle an.

Der folgende Beispielcode lädt die Muster-Excel-Datei und speichert sie im PDF-/Bildformat, indem verschiedene TextCrossType festgelegt werden. Die Muster-Excel-Datei und Ausgabedateien können unter den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
