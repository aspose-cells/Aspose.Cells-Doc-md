---
title: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 110
url: /de/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder eine Zeichenfolge enthält, die breiter ist als die Zellbreite, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte leer oder null ist. Beim Speichern Ihrer Excel-Datei in PDF/Bild können Sie diese Überlauf durch Angabe des Kreuztyps mithilfe der [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)-Aufzählung steuern. Diese hat folgende Werte

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Anzeige wie in MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle leer ist, wird die Zeichenfolge überlaufen oder abgeschnitten.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Anzeige der Zeichenfolge wie beim Exportieren von PDF/Bild aus MS Excel

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Anzeige des gesamten Textes durch Überlaufen anderer Zellen und Überschreiben des Textes in überlaufenen Zellen

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Anzeige nur der Zeichenfolge innerhalb der Zellbreite.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) angegeben werden. Die Beispiel-Excel-Datei und die Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
