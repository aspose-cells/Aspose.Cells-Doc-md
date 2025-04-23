---
title: Specificera sorteringsvarning vid sortering av data
type: docs
weight: 100
url: /sv/java/specifying-sort-warning-while-sorting-data/
---

## **Möjliga användningsscenario**
Vänligen beakta denna textdata dvs. {11, 111, 22}. Denna textdata sorteras så här eftersom i text 111 kommer före 22. Men om du vill sortera dessa data inte som text utan som nummer, kommer det att bli {11, 22, 111} eftersom numeriskt kommer 111 efter 22. Aspose.Cells tillhandahåller [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) egenskapen för att hantera detta problem. Vänligen sätt denna egenskap **true** och din textdata kommer att sorteras som numeriska data. Följande skärmdump visar sorteringsvarningen som visas av Microsoft Excel när textdata som ser ut som numeriska data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Exempelkod**
Följande provkod illustrerar användningen av [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) egenskapen som förklarats tidigare. Vänligen kontrollera dess [prov Excel-fil](43352077.xlsx) och [utdata Excel-fil](43352078.xlsx) för mer hjälp.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
{{< app/cells/assistant language="java" >}}
