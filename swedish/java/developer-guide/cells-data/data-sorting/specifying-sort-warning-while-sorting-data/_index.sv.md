---
title: Ange sorteringsvarning vid sortering av data
type: docs
weight: 100
url: /sv/java/specifying-sort-warning-while-sorting-data/
---
## **Möjliga användningsscenarier**
 Tänk på denna textinformation, dvs. {11, 111, 22}. Den här textdatan sorteras så här eftersom 111 kommer före 22 när det gäller text. Men om du vill sortera denna data inte som text utan som siffror kommer det att bli {11, 22, 111} eftersom numeriskt 111 kommer efter 22. Aspose.Cells tillhandahåller[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) egendom för att hantera denna fråga. Vänligen ange denna egenskap**Sann**och din textdata kommer att sorteras som numerisk data. Följande skärmdump visar sorteringsvarningen som visas av Microsoft Excel när textdata som ser ut som numerisk data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Exempelkod**
 Följande exempelkod illustrerar användningen av[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)egendom som förklarats tidigare. Vänligen kontrollera den[exempel på Excel-fil](43352077.xlsx) och[utdata Excel-fil](43352078.xlsx) för mer hjälp.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
