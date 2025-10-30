---
title: Datastyrning med Golang via C++
linktitle: Data Sortering
type: docs
weight: 130
url: /sv/go-cpp/sort-data-of-excel/
description: Lär dig hur man sorterar data med hjälp av API Aspose.Cells for C++.
keywords: Sortera data i stigande eller fallande ordning, Sortera data baserat på bakgrundsfärg
---

{{% alert color="primary" %}}

Databasering är en av Microsoft Excels många användbara funktioner. Det låter användare ordna data för att göra det lättare att skanna. Aspose.Cells låter utvecklare sortera arbetsbladsdata i alfabetisk eller numerisk ordning, vilket fungerar på samma sätt som Microsoft Excel gör för att sortera data.

{{% /alert %}}

## **Sortering av data i Microsoft Excel**

För att sortera data i Microsoft Excel:

1. Välj **Data** från **Sortera**-menyn. Sorteringsdialogen visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp data där data visas i kolumner.

## **Sortera data med Aspose.Cells**

Aspose.Cells tillhandahåller klassen [**DataSorter**](https://reference.aspose.com/cells/go-cpp/datasorter/) som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och ange sorteringsordning för nyckeln.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) accepterar följande parametrar:

- [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), cellerna för det underliggande arbetsbladet.
- [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel använder mallfilen "Bok1.xls" skapad i Microsoft Excel. Efter att koden har utförts sorteras data på lämpligt sätt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting.go" >}}
{{% alert color="primary" %}}

Om du vill sortera *FrånVänsterTillHöger*, använd attributet [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Sortera data med bakgrundsfärg**

Excel erbjuder funktioner för att sortera data baserat på bakgrundsfärg. Samma funktion tillhandahålls med Aspose.Cells med användning av DataSorter där [**SortOnType**](https://reference.aspose.com/cells/go-cpp/sortontype/).CellColor kan användas i [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) för att sortera data baserat på bakgrundsfärg. Alla celler som innehåller specificerad färg i [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), funktion placeras överst eller nederst enligt SortOrder-inställningen och ordningen för resten av cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting-1.go" >}}
## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/cpp/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/cpp/specifying-sort-warning-while-sorting-data/)
