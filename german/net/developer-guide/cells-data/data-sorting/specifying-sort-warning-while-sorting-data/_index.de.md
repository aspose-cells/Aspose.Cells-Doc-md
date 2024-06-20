---
title: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 140
url: /de/net/specifying-sort-warning-while-sorting-data/
description: Erfahren Sie, wie Sie beim Sortieren von Daten unter Verwendung der Aspose.Cells for .NET API eine Sortierwarnung angeben.
keywords: Sortierwarnung hinzufügen beim Sortieren von Daten, Sortierwarnung beim Sortieren von Daten festlegen, Sortierwarnung beim Sortieren von Daten auswählen.
---

## **Mögliche Verwendungsszenarien**

Bitte beachten Sie diese Textdaten, d.h. {11, 111, 22}. Diese Textdaten werden sortiert, weil hinsichtlich des Textes 111 vor 22 kommt. Wenn Sie jedoch diese Daten nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, da numerisch 111 nach 22 kommt. Aspose.Cells bietet die {0}-Eigenschaft, um dieses Problem zu beheben. Bitte setzen Sie diese Eigenschaft auf **true** und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung, die von Microsoft Excel angezeigt wird, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

Der folgende Beispielscode veranschaulicht die Verwendung der [**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)-Eigenschaft wie zuvor erläutert. Bitte überprüfen Sie die [Beispieldatei Excel](43352075.xlsx) und die [Ausgabedatei Excel](43352076.xlsx) für mehr Hilfe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
