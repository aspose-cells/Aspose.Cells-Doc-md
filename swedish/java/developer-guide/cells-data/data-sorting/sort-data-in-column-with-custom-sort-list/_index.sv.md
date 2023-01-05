---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 210
url: /sv/java/sort-data-in-column-with-custom-sort-list/
---
## **Möjliga användningsscenarier**

Du kan sortera data i kolumnen med hjälp av en anpassad lista. Detta kan göras med hjälp av[DataSorter.AddKey(int nyckel, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) metod. Den här metoden fungerar dock bara om objekten i den anpassade listan inte har kommatecken. Om de har kommatecken som "USA, USA", "Kina, CN" etc. måste du använda[DataSorter.AddKey(int nyckel, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) metod. Här är den sista parametern inte String utan en Array of Strings.

## **Sortera data i kolumn med anpassad sorteringslista**

Följande exempelkod förklarar hur man använder metoden DataSorter.AddKey(int-nyckel, SortOrder order, String[]customList) för att sortera data med anpassad sorteringslista. Vänligen se[exempel på Excel-fil](50528359.xlsx)används i denna kod och[utdata Excel-fil](50528358.xlsx)genereras av det. Följande skärmdump visar effekten av koden på exemplet på Excel-filen vid exekvering.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
