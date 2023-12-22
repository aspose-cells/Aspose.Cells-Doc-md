---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/net/sort-data-in-column-with-custom-sort-list/
description: Lär dig hur du sorterar data i kolumnen med hjälp av en anpassad lista genom att använda Aspose.Cells for .NET API.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Möjliga användningsscenarier**

 Du kan sortera data i kolumnen med hjälp av en anpassad lista. Detta kan göras med hjälp av[**DataSorter.AddKey(int nyckel, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)metod. Den här metoden fungerar dock bara om objekten i den anpassade listan inte har kommatecken. Om de har kommatecken som "USA,US", "China,CN" etc., måste du använda [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://referens. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) metod. Här är den sista parametern inte String utan en Array of Strings.

##  **Sortera data i kolumn med anpassad sorteringslista**

Följande exempelkod förklarar hur du använder [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) metod för att sortera data med anpassad sorteringslista. Vänligen se[exempel på Excel-fil](50528327.xlsx) används i denna kod och[utdata Excel-fil](50528328.xlsx) genereras av det. Följande skärmdump visar effekten av koden på exemplet på Excel-filen vid exekvering.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
