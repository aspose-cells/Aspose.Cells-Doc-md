---
title: Ändern Sie die Datenquelle des Diagramms in das Zieltabellenblatt beim Kopieren von Zeilen oder Bereich
type: docs
weight: 850
url: /de/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie Zeilen oder einen Bereich, die Diagramme enthalten, auf ein neues Tabellenblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Wenn beispielsweise die Datenquelle des Diagramms =Sheet1!$A$1:$B$4 lautet, bleibt nach dem Kopieren von Zeilen oder einem Bereich auf das neue Tabellenblatt die Datenquelle gleich, d.h. es bezieht sich immer noch auf das alte Tabellenblatt Sheet1. Dies ist auch das Verhalten von Microsoft Excel. Wenn Sie jedoch möchten, dass es sich auf das neue Zieltabellenblatt bezieht, verwenden Sie bitte die Eigenschaft CopyOptions.ReferToDestinationSheet und setzen Sie diese beim Aufruf der Cells.CopyRows() Methode auf true. Wenn Ihr Zieltabellenblatt beispielsweise DestSheet lautet, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 in =DestSheet!$A$1:$B$4.
## **Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen**
Der folgende Beispielcode erläutert die Verwendung der Eigenschaft CopyOptions.ReferToDestinationSheet beim Kopieren von Zeilen oder Bereichen mit Diagramm auf ein neues Tabellenblatt. Der Code verwendet die [Beispiel-Excel-Datei](5472284.xlsx) und generiert die [Ausgabe-Excel-Datei](5472283.xlsx). Der Screenshot zeigt, dass die Datenquelle des Diagramms in der [Ausgabe-Excel-Datei](5472283.xlsx) jetzt auf DestSheet anstatt auf Sheet1 verweist.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






