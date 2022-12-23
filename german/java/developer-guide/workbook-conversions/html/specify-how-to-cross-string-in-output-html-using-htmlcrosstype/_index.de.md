---
title: Geben Sie an, wie die Zeichenfolge in Ausgabe HTML mit HtmlCrossType gekreuzt werden soll
type: docs
weight: 140
url: /de/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Mögliche Nutzungsszenarien**

Wenn die Zelle Text oder eine Zeichenfolge enthält, aber größer als die Breite der Zelle ist, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie diesen Überlauf kontrollieren, indem Sie den Kreuztyp mit angeben[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Aufzählung. Es hat die folgenden Werte

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Anzeige wie MS Excel, die von der nächsten Zelle abhängt. Wenn die nächste Zelle null ist, kreuzt sich die Zeichenfolge oder sie wird abgeschnitten.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren von HTML an.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : Zeigen Sie HTML Querzeichenfolge an, die Leistung beim Erstellen großer HTML-Dateien ist mehr als zehnmal schneller als beim Festlegen des Werts auf[**URSPRÜNGLICH**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) oder[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Zeigen Sie HTML Querzeichenfolge an und blenden Sie die rechte Zeichenfolge aus, wenn sich die Texte überschneiden.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL)Die Zeichenfolge wird nur innerhalb der Breite der Zelle angezeigt.

## **Geben Sie an, wie die Zeichenfolge in Ausgabe HTML mit HtmlCrossType gekreuzt werden soll**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](51740747.xlsx)und speichert es im Format HTML, indem Sie different angeben[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Bitte laden Sie die herunter[Ausgang HTML](51740745.zip) Dateien, die mit diesem Code generiert wurden. Die Beispiel-Excel-Datei enthält das rot umrandete Bild, wie in diesem Screenshot gezeigt, der die Wirkung von zeigt[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Werte am Ausgang HTML.

![todo: Bild_alt_Text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
