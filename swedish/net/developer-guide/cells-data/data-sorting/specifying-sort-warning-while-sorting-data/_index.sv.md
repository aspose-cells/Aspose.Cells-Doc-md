---
title: Specificera sorteringsvarning vid sortering av data
type: docs
weight: 140
url: /sv/net/specifying-sort-warning-while-sorting-data/
description: Lär dig hur man specificerar sorteringsvarning vid sortering av data med hjälp av API et Aspose.Cells for .NET.
keywords: Lägg till sorteringsvarning vid sortering av data, ställ in sorteringsvarning vid sortering av data, välj sorteringsvarning vid sortering av data.
---

## **Möjliga användningsscenario**

Överväg denna textdata dvs. {11, 111, 22}. Denna textdata sorteras eftersom, i termer av text, kommer 111 före 22. Men om du vill sortera denna data inte som text utan som nummer, kommer det att bli {11, 22, 111} eftersom 111 numeriskt kommer efter 22. Aspose.Cells tillhandahåller {0} egenskapen för att hantera detta problem. Ställ in denna egenskap **true** och din textdata kommer att sorteras som numerisk data. Följande skärmdump visar sorteringsvarningen som visas av Microsoft Excel när textdata som ser ut som numerisk data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Exempelkod**

Den följande exemplarkoden illustrerar användningen av [**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)-egenskapen enligt tidigare förklaring. Kontrollera dess [exempelfil för Excel](43352075.xlsx) och [utdatafil för Excel](43352076.xlsx) för mer hjälp.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
