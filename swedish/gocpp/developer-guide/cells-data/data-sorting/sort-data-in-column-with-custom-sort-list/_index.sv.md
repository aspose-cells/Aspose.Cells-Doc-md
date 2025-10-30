---
title: Sortera data i kolumn med anpassad sorteringslista med Golang via C++
linktitle: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Lär dig hur du sorterar data i en kolumn med en anpassad lista med API et Aspose.Cells for C++.
keywords: Sortera Data i Kolumn med Anpassad Sorteringslista, Sortera data med anpassad lista.
---

## **Möjliga användningsscenario**

Du kan sortera data i en kolumn med en anpassad lista. Detta kan göras med [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/)-metoden. Men, denna metod fungerar endast om objekten i den anpassade listan inte innehåller kommatecken. Om de har kommatecken som "USA,US", "China,CN" etc., måste du använda [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/)-metoden. Här är det sista parametern inte en String, utan en array av strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Följande exempel på kod förklarar hur man använder [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/)-metoden för att sortera data med en anpassad sorteringslista. Se [exempel-Excel fil](50528327.xlsx) som används i denna kod och [utdata Excel-fil](50528328.xlsx) som genereras av den. Följande skärmbild visar effekten av koden på exempel-Excel-filen vid körning.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
