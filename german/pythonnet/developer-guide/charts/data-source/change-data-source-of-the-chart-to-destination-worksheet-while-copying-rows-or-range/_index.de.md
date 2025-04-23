---
title: Ändern Sie die Datenquelle des Diagramms in das Zieltabellenblatt beim Kopieren von Zeilen oder Bereich
description: Erfahren Sie, wie Sie die Datenquelle eines Diagramms zu einem Ziel Arbeitsblatt ändern, während Sie Zeilen oder einen Bereich in Aspose.Cells für Python via .NET kopieren. Unser Leitfaden zeigt, wie Sie den Datenbereich des Diagramms aktualisieren und auf das Ziel Arbeitsblatt verlinken, um sicherzustellen, dass die kopierten Zeilen oder der Bereich im Diagramm korrekt widergespiegelt werden.
keywords: Aspose.Cells für Python via .NET, Diagrammerstellung, Datenquelle, Ziel Arbeitsblatt, Zeilen, Bereich, kopieren, aktualisieren, Datenbereich, Verknüpfung.
type: docs
weight: 440
url: /de/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Zeilen oder einen Bereich kopieren, der Diagramme enthält, und in ein neues Arbeitsblatt einfügen, ändert sich die Datenquelle des Diagramms nicht. Wenn beispielsweise die Datenquelle des Diagramms =Sheet1!$A$1:$B$4 ist, dann bleibt die Datenquelle nach dem Kopieren von Zeilen oder Bereich in ein neues Arbeitsblatt gleich, d.h. =Sheet1!$A$1:$B$4. Es bezieht sich immer noch auf das alte Arbeitsblatt, d.h. Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Wenn Sie jedoch möchten, dass sie sich auf das neue Zielarbeitsblatt bezieht, verwenden Sie die [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet)-Eigenschaft und setzen Sie sie auf **true** bei Aufruf der [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows)-Methode. Jetzt, wenn Ihr Zielarbeitsblatt DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 in =DestSheet!$A$1:$B$4.

## **Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen**

Der folgende Beispielcode erläutert die Verwendung der [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet)-Eigenschaft beim Kopieren von Zeilen oder Bereich mit Diagrammen in ein neues Arbeitsblatt. Der Code verwendet die [Beispieldatei Excel](5113699.xlsx) und generiert die [Ausgabedatei Excel](5113697.xlsx).

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
