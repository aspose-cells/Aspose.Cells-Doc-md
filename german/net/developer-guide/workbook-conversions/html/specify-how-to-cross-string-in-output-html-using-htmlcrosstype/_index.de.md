---
title: Geben Sie an, wie Zeichenkette in der Ausgabe HTML mit HtmlCrossType geschnitten werden soll
type: docs
weight: 140
url: /de/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Mögliche Verwendungsszenarien**

Wenn in einer Zelle Text oder eine Zeichenfolge enthalten ist, die jedoch breiter ist als die Breite der Zelle, dann läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte leer oder null ist. Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie dieses Überlaufen steuern, indem Sie den Überlauftyp mithilfe der [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)-Enumerationswert angeben. Es hat die folgenden Werte

- **HtmlCrossType.Default**: Zeigen Sie es wie MS Excel an, abhängig von der nächsten Zelle. Wenn die nächste Zelle leer ist, wird der String durchgestrichen oder abgeschnitten.

- **HtmlCrossType.MSExport**: Zeigen Sie den String wie MS Excel, der HTML exportiert.

- **HtmlCrossType.Cross**: Zeigen Sie den HTML-Durchkreuzungsstring an. Die Leistung bei der Erstellung großer HTML-Dateien ist mehr als zehnmal schneller als das Setzen des Werts auf Standard oder FitToCell.

- **HtmlCrossType.FitToCell**: Zeigen Sie nur den String innerhalb der Zellenbreite an.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740732.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) spezifiziert werden. Bitte laden Sie die mit diesem Code generierten [Ausgabe-HTMLs](51740734.zip) herunter. Die Beispiel-Excel-Datei enthält das Bild mit rotem Rahmen, wie in diesem Screenshot gezeigt, der den Effekt der [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)-Werte auf die Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
