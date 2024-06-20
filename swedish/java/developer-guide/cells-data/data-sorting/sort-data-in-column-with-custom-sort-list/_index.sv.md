---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 210
url: /sv/java/sort-data-in-column-with-custom-sort-list/
---

## **Möjliga användningsscenario**

Du kan sortera data i kolumnen med hjälp av en anpassad lista. Det kan göras med [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) metoden. Men denna metod fungerar endast om objekten i den anpassade listan inte har kommatecken inuti dem. Om de har kommatecken som "USA, US", "China, CN" osv., måste du använda [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) metoden. Här är det sista parametern inte en sträng utan en array av strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Följande provkod förklarar användningen av [DataSorter.AddKey(int key, SortOrder order, String[] customList)] metoden för att sortera data med anpassad sorteringslista. Se den [prov Excel-filen](50528359.xlsx) som används i denna kod och [utdata Excel-filen](50528358.xlsx) genererad av den. Följande skärmdump visar effekten av koden på prov Excel-filen vid körning.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
