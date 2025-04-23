---
title: Ändern Sie die Datenquelle des Diagramms in das Zieltabellenblatt beim Kopieren von Zeilen oder Bereich
description: Erfahren Sie, wie Sie die Datenquelle eines Diagramms in ein Zielarbeitsblatt ändern, während Sie Zeilen oder einen Bereich in Aspose.Cells for .NET kopieren. Unser Leitfaden zeigt Ihnen, wie Sie den Datenbereich des Diagramms aktualisieren und mit dem Zielarbeitsblatt verknüpfen, um sicherzustellen, dass die kopierten Zeilen oder der Bereich im Diagramm genau wiedergegeben werden.
keywords: Aspose.Cells for .NET, Diagrammerstellung, Datenquelle, Zielarbeitsblatt, Zeilen, Bereich, kopieren, aktualisieren, Datenbereich, Verknüpfung.
type: docs
weight: 440
url: /de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Zeilen oder einen Bereich kopieren, der Diagramme enthält, und in ein neues Arbeitsblatt einfügen, ändert sich die Datenquelle des Diagramms nicht. Wenn beispielsweise die Datenquelle des Diagramms =Sheet1!$A$1:$B$4 ist, dann bleibt die Datenquelle nach dem Kopieren von Zeilen oder Bereich in ein neues Arbeitsblatt gleich, d.h. =Sheet1!$A$1:$B$4. Es bezieht sich immer noch auf das alte Arbeitsblatt, d.h. Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Wenn Sie jedoch möchten, dass sie sich auf das neue Zielarbeitsblatt bezieht, verwenden Sie die [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)-Eigenschaft und setzen Sie sie auf **true** bei Aufruf der [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)-Methode. Jetzt, wenn Ihr Zielarbeitsblatt DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 in =DestSheet!$A$1:$B$4.

## **Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen**

Der folgende Beispielcode erläutert die Verwendung der [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)-Eigenschaft beim Kopieren von Zeilen oder Bereich mit Diagrammen in ein neues Arbeitsblatt. Der Code verwendet die [Beispieldatei Excel](5113699.xlsx) und generiert die [Ausgabedatei Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
