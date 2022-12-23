---
title: Ändern Sie die Datenquelle des Diagramms in das Zielarbeitsblatt, während Sie Zeilen oder einen Bereich kopieren
type: docs
weight: 850
url: /de/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Mögliche Nutzungsszenarien**
Wenn Sie Zeilen oder Bereiche, die Diagramme enthalten, in ein neues Arbeitsblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Wenn beispielsweise die Datenquelle des Diagramms =Sheet1!$A$1:$B$4 ist, bleibt die Datenquelle nach dem Kopieren von Zeilen oder Bereichen in ein neues Arbeitsblatt unverändert, dh =Sheet1!$A$1:$B$4. Es bezieht sich immer noch auf das alte Arbeitsblatt, dh Sheet1. Dies ist auch das Microsoft Excel-Verhalten. Wenn Sie jedoch möchten, dass es sich auf ein neues Zielarbeitsblatt bezieht, verwenden Sie bitte die Eigenschaft CopyOptions.ReferToDestinationSheet und setzen Sie sie beim Aufrufen der Methode Cells.CopyRows() auf „true“. Wenn Ihr Zielarbeitsblatt jetzt DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 zu =DestSheet!$A$1:$B$4.
## **Ändern Sie die Datenquelle des Diagramms in das Zielarbeitsblatt, während Sie Zeilen oder einen Bereich kopieren**
 Der folgende Beispielcode erläutert die Verwendung der Eigenschaft CopyOptions.ReferToDestinationSheet beim Kopieren von Zeilen oder Bereichen, die Diagramme enthalten, in ein neues Arbeitsblatt. Der Code verwendet die[Excel-Beispieldatei](5472284.xlsx) und generiert die[Excel-Datei ausgeben](5472283.xlsx) . Der Screenshot zeigt, dass die Datenquelle des Diagramms in[Excel-Datei ausgeben](5472283.xlsx) bezieht sich jetzt auf DestSheet statt auf Sheet1.

![todo: Bild_alt_Text](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






