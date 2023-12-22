---
title: Ändern Sie beim Kopieren von Zeilen oder Bereichen die Datenquelle des Diagramms in das Zielarbeitsblatt
description: Erfahren Sie unter Aspose.Cells for .NET, wie Sie beim Kopieren von Zeilen oder einem Bereich die Datenquelle eines Diagramms in ein Zielarbeitsblatt ändern. Unser Leitfaden zeigt Ihnen, wie Sie den Datenbereich des Diagramms aktualisieren und mit dem Zielarbeitsblatt verknüpfen, um sicherzustellen, dass die kopierten Zeilen bzw Bereich werden im Diagramm genau wiedergegeben.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Mögliche Nutzungsszenarien**

Wenn Sie Zeilen oder Bereiche, die Diagramme enthalten, in ein neues Arbeitsblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Wenn die Datenquelle des Diagramms beispielsweise =Sheet1!$A$1:$B$4 ist, bleibt die Datenquelle nach dem Kopieren von Zeilen oder Bereichen in ein neues Arbeitsblatt dieselbe, d. h. =Sheet1!$A$1:$B$4. Es bezieht sich immer noch auf das alte Arbeitsblatt, also Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Wenn Sie jedoch möchten, dass es auf das neue Zielarbeitsblatt verweist, verwenden Sie bitte das[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)Eigenschaft und setzen Sie sie auf**WAHR** beim Anrufen[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)Methode. Wenn Ihr Zielarbeitsblatt nun DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 in =DestSheet!$A$1:$B$4.

##  **Ändern Sie beim Kopieren von Zeilen oder Bereichen die Datenquelle des Diagramms in das Zielarbeitsblatt**

Der folgende Beispielcode erläutert die Verwendung von[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) -Eigenschaft beim Kopieren von Zeilen oder Bereichen, die Diagramme enthalten, in ein neues Arbeitsblatt. Der Code verwendet die[Beispiel-Excel-Datei](5113699.xlsx) und erzeugt die[Excel-Datei ausgeben](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
