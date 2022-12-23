---
title: Ändern Sie die Datenquelle des Diagramms in das Zielarbeitsblatt, während Sie Zeilen oder einen Bereich kopieren
type: docs
weight: 440
url: /de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie Zeilen oder Bereiche, die Diagramme enthalten, in ein neues Arbeitsblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Wenn beispielsweise die Datenquelle des Diagramms =Sheet1!$A$1:$B$4 ist, bleibt die Datenquelle nach dem Kopieren von Zeilen oder Bereichen in ein neues Arbeitsblatt unverändert, dh =Sheet1!$A$1:$B$4. Es bezieht sich immer noch auf das alte Arbeitsblatt, dh Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Wenn Sie jedoch möchten, dass es sich auf das neue Zielarbeitsblatt bezieht, verwenden Sie bitte die[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)Eigenschaft und setzen Sie es auf**wahr** beim Anrufen der[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)Methode. Wenn Ihr Zielarbeitsblatt jetzt DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 zu =DestSheet!$A$1:$B$4.

## **Ändern Sie die Datenquelle des Diagramms in das Zielarbeitsblatt, während Sie Zeilen oder einen Bereich kopieren**

 Der folgende Beispielcode erläutert die Verwendung von[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) -Eigenschaft beim Kopieren von Zeilen oder Bereichen, die Diagramme enthalten, in ein neues Arbeitsblatt. Der Code verwendet die[Excel-Beispieldatei](5113699.xlsx) und generiert die[Excel-Datei ausgeben](5113697.xlsx).

![todo: Bild_alt_Text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
