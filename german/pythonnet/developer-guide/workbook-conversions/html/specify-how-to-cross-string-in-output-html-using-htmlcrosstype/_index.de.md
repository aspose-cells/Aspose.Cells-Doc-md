---
title: Geben Sie an, wie Zeichenkette in der Ausgabe HTML mit HtmlCrossType geschnitten werden soll
type: docs
weight: 140
url: /de/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Mögliche Verwendungsszenarien**

Wenn in einer Zelle Text oder eine Zeichenfolge enthalten ist, die jedoch breiter ist als die Breite der Zelle, dann läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte leer oder null ist. Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie dieses Überlaufen steuern, indem Sie den Überlauftyp mithilfe der [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)-Enumerationswert angeben. Es hat die folgenden Werte

- **HtmlCrossType.DEFAULT**: Anzeige wie MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, wird der String gekreuzt oder abgeschnitten.

- **HtmlCrossType.MS_EXPORT**: Anzeige des Strings wie beim HTML-Export in MS Excel.

- **HtmlCrossType.CROSS**: Anzeige des HTML-Kreuzstrings, die Erstellung großer HTML-Dateien ist mehr als zehnmal schneller als bei Default oder FitToCell.

- **HtmlCrossType.CROSS_HIDE_RIGHT**: Anzeige des HTML-Kreuzstrings und Ausblenden des rechten Strings, wenn die Texte sich überlappen.

- **HtmlCrossType.FIT_TO_CELL**: Nur Anzeige des Strings innerhalb der Breite der Zelle.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740732.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) spezifiziert werden. Bitte laden Sie die mit diesem Code generierten [Ausgabe-HTMLs](51740734.zip) herunter. Die Beispiel-Excel-Datei enthält das Bild mit rotem Rahmen, wie in diesem Screenshot gezeigt, der den Effekt der [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)-Werte auf die Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
