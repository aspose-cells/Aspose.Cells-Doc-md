---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/python-net/sort-data-in-column-with-custom-sort-list/
description: Lär dig hur du sorterar data i kolumn med en anpassad lista genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python Sortera data i kolumn med anpassad sorteringslista, Python Sortera data med anpassad lista.
---

## **Möjliga användningsscenario**

Du kan sortera data i kolumn med en anpassad lista. Detta kan göras med hjälp av [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)-metoden. Dock fungerar denna metod endast om objekten i den anpassade listan inte har kommatecken inuti dem. Om de har kommatecken som "USA,US", "Kina,CN" osv., måste du använda [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)-metoden. Här är det sista parametern inte en sträng utan en matris av strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Den följande exemplarkoden förklarar hur man använder [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)-metoden för att sortera data med anpassad sorteringslista. Se den [exempelfil för Excel](50528327.xlsx) som används i denna kod och [utdatafil för Excel](50528328.xlsx) som genereras av den. Följande skärmdump visar effekten av koden på exemplet för Excel vid körning.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
