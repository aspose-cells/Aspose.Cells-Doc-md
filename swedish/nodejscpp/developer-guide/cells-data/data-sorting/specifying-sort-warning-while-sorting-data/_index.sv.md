---
title: Specificera sorteringsvarning vid sortering av data
type: docs
weight: 140
url: /sv/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: Lär dig hur man specificerar varningsmeddelande för sortering när man sorterar data med API Aspose.Cells for Node.js via C++.
keywords: Lägg till sorteringsvarning vid sortering av data, ställ in sorteringsvarning vid sortering av data, välj sorteringsvarning vid sortering av data.
---

## **Möjliga användningsscenario**

Tänk på denna textbaserade data dvs. {11, 111, 22}. Denna data sorteras eftersom, i termer av text, kommer 111 före 22. Men om du vill sortera denna data som siffror, blir den {11, 22, 111} eftersom numeriskt kommer 111 efter 22. API Aspose.Cells for Node.js via C++ tillhandahåller egenskapen {0} för att hantera detta problem. Ställ in egenskapen **true** och din textdata kommer att sorteras som numerisk data. Skärmbilden visar varningsmeddelandet som Microsoft Excel visar när textbaserad data som ser ut som numerisk data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Exempelkod**

Den följande exemplarkoden illustrerar användningen av [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-)-egenskapen enligt tidigare förklaring. Kontrollera dess [exempelfil för Excel](43352075.xlsx) och [utdatafil för Excel](43352076.xlsx) för mer hjälp.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

