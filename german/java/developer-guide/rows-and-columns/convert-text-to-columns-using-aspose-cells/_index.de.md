---
title: Konvertieren Sie Text in Spalten mit Aspose.Cells
type: docs
weight: 70
url: /de/java/convert-text-to-columns-using-aspose-cells/
---
## **Mögliche Nutzungsszenarien**
Sie können Ihren Text mit Microsoft Excel in Spalten umwandeln. Diese Funktion ist ab verfügbar*Datenwerkzeuge* unter dem*Daten* Tab. Um den Inhalt einer Spalte auf mehrere Spalten aufzuteilen, sollten die Daten ein bestimmtes Trennzeichen wie ein Komma (oder ein beliebiges anderes Zeichen) enthalten, auf dessen Grundlage Microsoft Excel den Inhalt einer Zelle auf mehrere Zellen aufteilt. Aspose.Cells bietet diese Funktion auch über[TextZuSpalten](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) Methode.
## **Konvertieren Sie Text in Spalten mit Aspose.Cells**
Der folgende Beispielcode erläutert die Verwendung der[TextZuSpalten](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) Methode. Der Code fügt zunächst einige Personennamen in Spalte A des ersten Arbeitsblatts hinzu. Vor- und Nachname werden durch Leerzeichen getrennt. Dann gilt die[TextZuSpalten](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) )-Methode in Spalte A und speichert sie als Ausgabe-Excel-Datei. Wenn Sie die öffnen[Excel-Datei ausgeben](25395230.xlsx), werden Sie sehen, dass sich Vornamen in Spalte A befinden, während Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](convert-text-to-columns-using-aspose-cells_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
