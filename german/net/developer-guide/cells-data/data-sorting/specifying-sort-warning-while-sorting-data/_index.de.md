---
title: Angeben einer Sortierwarnung beim Sortieren von Daten
type: docs
weight: 140
url: /de/net/specifying-sort-warning-while-sorting-data/
---
## **Mögliche Nutzungsszenarien**

Bitte beachten Sie diese Textdaten, dh {11, 111, 22}. Diese Textdaten werden sortiert, weil 111 in Bezug auf Text vor 22 kommt. Wenn Sie diese Daten jedoch nicht als Text, sondern als Zahlen sortieren möchten, werden sie zu {11, 22, 111}, da 111 numerisch nach 22 kommt Aspose.Cells bietet[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)Eigenschaft, mit diesem Problem umzugehen. Bitte legen Sie diese Eigenschaft fest**Stimmt**und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt die Sortierwarnung, die von Microsoft Excel angezeigt wird, wenn Textdaten sortiert werden, die wie numerische Daten aussehen.

![todo: Bild_alt_Text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

 Der folgende Beispielcode veranschaulicht die Verwendung von[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)Eigenschaft, wie zuvor erklärt. Bitte überprüfen Sie es[Beispiel-Excel-Datei](43352075.xlsx) und[Excel-Datei ausgeben](43352076.xlsx) für weitere Hilfe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
