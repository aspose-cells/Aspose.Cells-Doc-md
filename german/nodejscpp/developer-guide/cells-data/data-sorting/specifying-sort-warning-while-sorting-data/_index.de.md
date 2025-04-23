---
title: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 140
url: /de/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: Erfahren Sie, wie Sie beim Sortieren von Daten die Warnung bei der Sortierung mithilfe der API Aspose.Cells for Node.js via C++ angeben.
keywords: Sortierwarnung hinzufügen beim Sortieren von Daten, Sortierwarnung beim Sortieren von Daten festlegen, Sortierwarnung beim Sortieren von Daten auswählen.
---

## **Mögliche Verwendungsszenarien**

Bitte beachten Sie diese Textdaten, d.h. {11, 111, 22}. Diese Textdaten werden sortiert, weil 111 vor 22 kommt, wenn man nach Text sortiert. Möchten Sie diese Daten jedoch nicht als Text, sondern als Zahlen sortieren, lautet die Reihenfolge {11, 22, 111}, da numerisch 111 nach 22 kommt. Die API Aspose.Cells for Node.js via C++ stellt die Eigenschaft {0} bereit, um dieses Problem zu lösen. Stellen Sie diese Eigenschaft auf **true**, und Ihre Textdaten werden wie numerische Daten sortiert. Das folgende Bildschirmfoto zeigt die Sortierwarnung, die Microsoft Excel anzeigt, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

Der folgende Beispielscode veranschaulicht die Verwendung der [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-)-Eigenschaft wie zuvor erläutert. Bitte überprüfen Sie die [Beispieldatei Excel](43352075.xlsx) und die [Ausgabedatei Excel](43352076.xlsx) für mehr Hilfe.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

