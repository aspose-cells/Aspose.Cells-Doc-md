---
title: Ange sorteringsvarning vid sortering av data
type: docs
weight: 140
url: /sv/net/specifying-sort-warning-while-sorting-data/
description: Lär dig hur du anger sorteringsvarning när du sorterar data genom att använda Aspose.Cells for .NET API.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **Möjliga användningsscenarier**

Tänk på denna textinformation, dvs. {11, 111, 22}. Denna textdata sorteras eftersom, i termer av text, 111 kommer före 22. Men om du vill sortera denna data inte som text utan som siffror, kommer det att bli {11, 22, 111} eftersom numeriskt 111 kommer efter 22 Aspose.Cells tillhandahåller[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)egendom för att hantera denna fråga. Vänligen ange denna egenskap**Sann**och din textdata kommer att sorteras som numerisk data. Följande skärmdump visar sorteringsvarningen som visas av Microsoft Excel när textdata som ser ut som numerisk data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **Exempelkod**

 Följande exempelkod illustrerar användningen av[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) egendom som förklarats tidigare. Vänligen kontrollera den[exempel på Excel-fil](43352075.xlsx) och[utdata Excel-fil](43352076.xlsx) för mer hjälp.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
