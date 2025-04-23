---
title: Text in Spalten konvertieren mithilfe von Aspose.Cells
type: docs
weight: 70
url: /de/java/convert-text-to-columns-using-aspose-cells/
---

## **Mögliche Verwendungsszenarien**
Sie können Ihren Text mit Microsoft Excel in Spalten umwandeln. Diese Funktion ist im Abschnitt *Datenwerkzeuge* unter dem Reiter *Daten* verfügbar. Um den Inhalt einer Spalte in mehrere Spalten aufzuteilen, sollte die Daten einen bestimmten Trennzeichen enthalten, z.B. ein Komma (oder ein anderes Zeichen), anhand dessen Microsoft Excel den Zelleninhalt in mehrere Zellen aufteilt. Aspose.Cells bietet diese Funktion ebenfalls über die Methode [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) an.
## **Text in Spalten konvertieren mit Aspose.Cells**
Der folgende Beispielcode erklärt die Verwendung der [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) Methode. Der Code fügt zunächst einige Personennamen in Spalte A des ersten Arbeitsblatts ein. Vorname und Nachname sind durch ein Leerzeichen getrennt. Anschließend wendet er die [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) Methode auf Spalte A an und speichert sie als Ausgabedatei. Wenn Sie die [Ausgabedatei](25395230.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A und die Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
