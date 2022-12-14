---
title: Geben Sie an, wie Zeichenfolgen in Ausgabe-PDF und -Bild gekreuzt werden sollen
type: docs
weight: 20
url: /de/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Geben Sie an, wie Zeichenfolgen in Ausgabe-PDF und -Bild gekreuzt werden sollen**
 Wenn eine Zelle Text oder eine Zeichenfolge enthält, die größer als die Breite der Zelle ist, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in PDF/Image speichern, können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mit angeben[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) Aufzählung. Es hat die folgenden Werte

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Darstellung wie MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, kreuzt sich die Zeichenfolge oder sie wird abgeschnitten.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Zeigt die Zeichenfolge ähnlich wie MS Excel beim Exportieren von PDF/Bildern an
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE): Zeigen Sie den gesamten Text an, indem Sie andere Zellen kreuzen, und überschreiben Sie den Text von gekreuzten Zellen
- [TextCrossType.STRICT_IN_ZELLE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL)Die Zeichenfolge wird nur innerhalb der Breite der Zelle angezeigt.

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF/Image-Format, indem ein anderer TextCrossType angegeben wird. Die Excel-Beispieldatei und die Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
