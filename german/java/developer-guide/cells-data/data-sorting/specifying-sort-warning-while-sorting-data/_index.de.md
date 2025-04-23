---
title: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 100
url: /de/java/specifying-sort-warning-while-sorting-data/
---

## **Mögliche Verwendungsszenarien**
Bitte beachten Sie diese textuellen Daten, d.h. {11, 111, 22}. Diese textuellen Daten werden so sortiert, weil in Texten 111 vor 22 kommt. Wenn Sie jedoch diese Daten nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, denn numerisch kommt 111 nach 22. Aspose.Cells bietet die Eigenschaft [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) zur Bewältigung dieses Problems an. Bitte setzen Sie diese Eigenschaft auf **true** und Ihre textuellen Daten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung, die von Microsoft Excel angezeigt wird, wenn textuelle Daten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Beispielcode**
Der folgende Beispielscode veranschaulicht die Verwendung der Eigenschaft [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) wie zuvor erklärt. Bitte überprüfen Sie die [Beispiel-Excel-Datei](43352077.xlsx) und die [Ausgabe-Excel-Datei](43352078.xlsx) für weitere Hilfe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
{{< app/cells/assistant language="java" >}}
