---
title: Gib an, wie man Zeilen in HTML Ausgabe mit HtmlCrossType überspringt, mit Golang via C++
linktitle: Geben Sie HtmlCrossType im Ausgabe HTML an
type: docs
weight: 140
url: /de/go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Lernen Sie, wie Sie den Textüberlauf in HTML Ausgaben mit Aspose.Cells for C++ und HtmlCrossType kontrollieren.
---

## **Mögliche Verwendungsszenarien**

 Wenn eine Zelle Text oder einen String enthält, der größer ist als die Breite der Zelle, läuft der Text über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Beim Speichern Ihrer Excel-Datei als HTML können Sie diesen Überlauf steuern, indem Sie den Quertyp mit [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) festlegen. Er hat folgende Werte:

- **HtmlCrossType.Default**: Zeigen Sie es wie MS Excel an, abhängig von der nächsten Zelle. Wenn die nächste Zelle leer ist, wird der String durchgestrichen oder abgeschnitten.

- **HtmlCrossType.MSExport**: Zeigen Sie den String wie MS Excel, der HTML exportiert.

- **HtmlCrossType.Cross**: Zeigen Sie den HTML-Durchkreuzungsstring an. Die Leistung bei der Erstellung großer HTML-Dateien ist mehr als zehnmal schneller als das Setzen des Werts auf Standard oder FitToCell.

- **HtmlCrossType.FitToCell**: Nur innerhalb der Breite der Zelle anzeigen.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740732.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) angegeben werden. Bitte laden Sie die [Ausgabedateien HTML](51740734.zip) herunter, die mit diesem Code generiert wurden. Die Beispiel-Excel-Datei enthält das Bild mit rotem Rahmen, wie in diesem Screenshot gezeigt, der die Wirkung der [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/)-Werte auf das Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}
