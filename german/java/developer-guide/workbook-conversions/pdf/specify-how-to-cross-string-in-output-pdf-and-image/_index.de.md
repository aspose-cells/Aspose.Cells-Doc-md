---
title: Geben Sie an, wie die Zeichenfolge in Ausgabe PDF und Bild gekreuzt werden soll
type: docs
weight: 110
url: /de/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Mögliche Nutzungsszenarien**

Wenn eine Zelle Text oder eine Zeichenfolge enthält, aber größer als die Breite der Zelle ist, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in PDF/Image speichern, können Sie diesen Überlauf kontrollieren, indem Sie den Kreuztyp mit angeben[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)Aufzählung. Es hat die folgenden Werte

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Darstellung wie MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, kreuzt sich die Zeichenfolge oder sie wird abgeschnitten.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren von PDF/Image an

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Zeigen Sie den gesamten Text an, indem Sie andere Zellen kreuzen, und überschreiben Sie den Text von gekreuzten Zellen

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Die Zeichenfolge wird nur innerhalb der Zellenbreite angezeigt.

## **Geben Sie an, wie die Zeichenfolge in der Ausgabe PDF/Image mit TextCrossType gekreuzt werden soll**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im Format PDF/Image, indem er different[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Die Excel-Beispieldatei und die Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
