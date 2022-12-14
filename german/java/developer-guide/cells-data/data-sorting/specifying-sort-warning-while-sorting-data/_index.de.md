---
title: Angeben einer Sortierwarnung beim Sortieren von Daten
type: docs
weight: 100
url: /de/java/specifying-sort-warning-while-sorting-data/
---
## **Mögliche Nutzungsszenarien**
 Bitte beachten Sie diese Textdaten, dh {11, 111, 22}. Diese Textdaten werden so sortiert, weil 111 in Bezug auf Text vor 22 steht. Wenn Sie diese Daten jedoch nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, weil 111 numerisch danach kommt 22. Aspose.Cells bietet[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) Eigenschaft, mit diesem Problem umzugehen. Bitte legen Sie diese Eigenschaft fest**Stimmt**und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung, die von Microsoft Excel angezeigt wird, wenn Textdaten sortiert werden, die wie numerische Daten aussehen.

![todo: Bild_alt_Text](specifying-sort-warning-while-sorting-data_1.png)
## **Beispielcode**
 Der folgende Beispielcode veranschaulicht die Verwendung von[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)Eigenschaft, wie zuvor erklärt. Bitte überprüfen Sie es[Beispiel-Excel-Datei](43352077.xlsx) und[Excel-Datei ausgeben](43352078.xlsx) für weitere Hilfe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
