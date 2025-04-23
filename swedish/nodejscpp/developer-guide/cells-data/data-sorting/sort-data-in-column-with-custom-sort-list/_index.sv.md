---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Lär dig hur man sorterar data i en kolumn med en anpassad lista med hjälp av API Aspose.Cells for Node.js via C++.
keywords: Sortera Data i Kolumn med Anpassad Sorteringslista, Sortera data med anpassad lista.
---

## **Möjliga användningsscenario**

Du kan sortera data i en kolumn med en anpassad lista. Detta kan göras med metoden [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-). Dock fungerar denna metod endast om objekten i den anpassade listan inte har komma inuti dem. Om de har komma, som "USA,US", "China,CN" etc., måste du använda [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) metod. Här är den sista parametern inte en Sträng utan en Array av Strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Följande exempel demonstrerar hur man använder [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) metod för att sortera data med en anpassad sorteringslista. Se exempel-Excel-filen och den genererade utdata Excel-filen. Skärmbilden visar effekten av koden på exempel-Excel-filen vid körning.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

