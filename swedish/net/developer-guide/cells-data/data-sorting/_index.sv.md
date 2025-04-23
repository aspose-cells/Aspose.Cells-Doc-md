---
title: Data Sortering
type: docs
weight: 130
url: /sv/net/sort-data-of-excel/
description: Lär dig hur man sorteras data genom att använda Aspose.Cells for .NET API.
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

Aspose.Cells tillhandahåller klassen [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter) som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och ange sorteringsordning för nyckeln.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) accepterar följande parametrar:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), cellerna för det underliggande arbetsbladet.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel använder mallfilen "Bok1.xls" skapad i Microsoft Excel. Efter att koden har utförts sorteras data på lämpligt sätt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

Om du vill sortera *FrånVänsterTillHöger*, använd attributet [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright).

{{% /alert %}}

### **Sortera data med bakgrundsfärg**

Excel erbjuder funktioner för att sortera data baserat på bakgrundsfärg. Samma funktion tillhandahålls med Aspose.Cells med användning av DataSorter där [**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor kan användas i [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) för att sortera data baserat på bakgrundsfärg. Alla celler som innehåller specificerad färg i [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), funktion placeras överst eller nederst enligt SortOrder-inställningen och ordningen för resten av cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/net/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="csharp" >}}
