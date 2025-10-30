---
title: Warnung vor Sortieren von Daten bei Sortierung mit Golang via C++ angeben
linktitle: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 140
url: /de/go-cpp/specifying-sort-warning-while-sorting-data/
description: Erfahren Sie, wie Sie beim Sortieren von Daten mithilfe der API Aspose.Cells for C++ Warnungen bei der Sortierung angeben.
keywords: Sortierwarnung hinzufügen beim Sortieren von Daten, Sortierwarnung beim Sortieren von Daten festlegen, Sortierwarnung beim Sortieren von Daten auswählen.
---

## **Mögliche Verwendungsszenarien**

Bitte beachten Sie diese Textdaten, d.h. {11, 111, 22}. Diese Textdaten werden sortiert, weil hinsichtlich des Textes 111 vor 22 kommt. Wenn Sie jedoch diese Daten nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, da numerisch 111 nach 22 kommt. Aspose.Cells bietet die {0}-Eigenschaft, um dieses Problem zu beheben. Bitte setzen Sie diese Eigenschaft auf **true** und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung, die von Microsoft Excel angezeigt wird, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

Der folgende Beispielscode veranschaulicht die Verwendung der [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortasnumber/)-Eigenschaft wie zuvor erläutert. Bitte überprüfen Sie die [Beispieldatei Excel](43352075.xlsx) und die [Ausgabedatei Excel](43352076.xlsx) für mehr Hilfe.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSortWarningWhileSortingData.go" >}}
