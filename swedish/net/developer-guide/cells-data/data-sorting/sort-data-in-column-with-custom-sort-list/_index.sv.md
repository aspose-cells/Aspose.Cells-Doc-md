---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/net/sort-data-in-column-with-custom-sort-list/
description: Lär dig hur man sorterar data i kolumnen med en anpassad lista med hjälp av API et Aspose.Cells for .NET.
keywords: Sortera Data i Kolumn med Anpassad Sorteringslista, Sortera data med anpassad lista.
---

## **Möjliga användningsscenario**

Du kan sortera data i kolumnen med en anpassad lista. Detta kan göras med hjälp av [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2) metoden. Dock fungerar denna metod bara om objekten i den anpassade listan inte har kommatecken i sig. Om de har kommatecken som "USA,US", "China,CN" osv., måste du använda [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) metoden. Här är det sista parametern inte en Sträng utan en Array av Strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Följande exempelkod förklarar hur man använder [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) metoden för att sortera data med anpassad sorteringslista. Se [exempel på Excel-fil](50528327.xlsx) som används i denna kod och [utdata Excel-fil](50528328.xlsx) som genereras av den. Nedanstående skärmdump visar effekten av koden på exempel-Excel-filen vid körningen.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
