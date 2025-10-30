---
title: Specificera sorteringsvarning vid sortering av data
type: docs
weight: 140
url: /sv/python-net/specifying-sort-warning-while-sorting-data/
description: Lär dig hur du specificerar sorteringsvarning vid sortering av data genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Lägg till sorteringsvarning vid sortering av data med Python, Ange sorteringsvarning vid sortering av data med Python, Välj sorteringsvarning vid sortering av data med Python.
---

## **Möjliga användningsscenario**

Överväg detta textdata, dvs. {11, 111, 22}. Detta textdata ordnas eftersom, i termer av text, kommer 111 före 22. Men om du vill sortera dessa data inte som text utan som nummer, blir det {11, 22, 111} eftersom numeriskt kommer 111 efter 22. Aspose.Cells for Python via .NET tillhandahåller egenskapen {0} för att hantera detta problem. Ställ in denna egenskap på **true** och ditt textdata kommer att sorteras som numeriskt data. Följande skärmdump visar sorteringsvarningen som visas av Microsoft Excel när textdata som ser ut som numeriska data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Exempelkod**

Den följande exemplarkoden illustrerar användningen av [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/)-egenskapen enligt tidigare förklaring. Kontrollera dess [exempelfil för Excel](43352075.xlsx) och [utdatafil för Excel](43352076.xlsx) för mer hjälp.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
{{< app/cells/assistant language="python-net" >}}
