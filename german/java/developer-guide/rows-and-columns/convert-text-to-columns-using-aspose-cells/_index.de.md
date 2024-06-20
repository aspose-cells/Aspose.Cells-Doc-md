---
title: Text in Spalten konvertieren mithilfe von Aspose.Cells
type: docs
weight: 70
url: /de/java/convert-text-to-columns-using-aspose-cells/
---

## **Mögliche Verwendungsszenarien**
Sie können Ihren Text mit Microsoft Excel in Spalten konvertieren. Diese Funktion ist unter dem Register *Daten* -> *Daten Tools* verfügbar. Um den Inhalt einer Spalte in mehrere Spalten aufzuteilen, sollte die Daten einen bestimmten Trennzeichen enthalten, wie z.B. ein Komma (oder ein anderes Zeichen), anhand dessen Microsoft Excel den Inhalt einer Zelle in mehrere Zellen aufteilt. Aspose.Cells bietet auch diese Funktion über die Methode [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)).
## **Text in Spalten konvertieren mit Aspose.Cells**
Der folgende Beispielcode erläutert die Verwendung der Methode [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)). Der Code fügt zunächst einige Personennamen in Spalte A des ersten Arbeitsblatts hinzu. Der Vor- und Nachname ist durch ein Leerzeichen getrennt. Dann wendet er die Methode [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) auf Spalte A an und speichert sie als Ausgabedatei. Wenn Sie die [Ausgabedatei](25395230.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A und die Nachnamen in Spalte B sind, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
