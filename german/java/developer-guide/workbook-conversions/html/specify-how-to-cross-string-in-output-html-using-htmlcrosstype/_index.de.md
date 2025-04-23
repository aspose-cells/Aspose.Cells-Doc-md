---
title: Geben Sie an, wie Zeichenkette in der Ausgabe HTML mit HtmlCrossType geschnitten werden soll
type: docs
weight: 140
url: /de/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Mögliche Verwendungsszenarien**

Wenn die Zelle Text oder eine Zeichenkette enthält, die jedoch breiter ist als die Breite der Zelle, dann wird die Zeichenfolge überlaufen, wenn die nächste Zelle in der nächsten Spalte leer oder null ist. Beim Speichern Ihrer Excel-Datei in HTML können Sie diese Überlaufkontrolle angeben, indem Sie den Kreuztyp mit der [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)-Aufzählung angeben. Es hat die folgenden Werte

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Anzeige wie in MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, wird die Zeichenkette überquert oder es wird abgeschnitten.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS-EXPORT): Anzeige der Zeichenfolge wie bei MS Excel-Exportierung in HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): Zeigen Sie HTML-Cross-String an, die Leistung bei der Erstellung großer HTML-Dateien ist mehr als zehnmal schneller als beim Wert [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) oder [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL) einstellen.

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT): Zeigen Sie HTML-Cross-String an und verbergen Sie den rechten String, wenn sich die Texte überlappen.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL): Zeigen Sie nur den String innerhalb der Breite der Zelle an.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740747.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) angegeben werden. Laden Sie bitte die generierten [Ausgabe-HTML-Dateien](51740745.zip) mit diesem Code herunter. Die Beispiel-Excel-Datei enthält das mit roter Farbe umrandete Bild, wie in diesem Screenshot gezeigt, der die Wirkung der [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)-Werte auf das Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
{{< app/cells/assistant language="java" >}}
