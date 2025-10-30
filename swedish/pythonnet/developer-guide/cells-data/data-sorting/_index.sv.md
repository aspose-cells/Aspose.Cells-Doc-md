---
title: Data Sortering
type: docs
weight: 130
url: /sv/python-net/sort-data-of-excel/
description: Lär dig hur man sorterar data genom att använda Aspose.Cells for för Python via .NET API.
keywords: Python Excel Library, Python Sortera data i stigande eller fallande ordning, Python Sortera data baserat på bakgrundsfärg.
---

{{% alert color="primary" %}}

Datahantering är en av Microsoft Excels många användbara funktioner. Det låter användare ordna data för att göra det lättare att skanna igenom. Aspose.Cells för Python via .NET låter utvecklare sortera kalkylbladsdata alfabetiskt eller numeriskt vilket fungerar på samma sätt som Microsoft Excel gör för att sortera data.

{{% /alert %}}

## **Sortering av data i Microsoft Excel**

För att sortera data i Microsoft Excel:

1. Välj **Data** från **Sortera**-menyn. Sorteringsdialogen visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp data där data visas i kolumner.

## **Sortera data med Aspose.Cells för Python Excel-biblioteket**

Aspose.Cells för Python via .NET tillhandahåller klassen [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och ange nyckelns sorteringsordning.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) accepterar följande parametrar:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), cellerna för det underliggande arbetsbladet.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel använder mallfilen "Bok1.xls" skapad i Microsoft Excel. Efter att koden har utförts sorteras data på lämpligt sätt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

Om du vill sortera *FrånVänsterTillHöger*, använd attributet [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/).

{{% /alert %}}

### **Sortera data med bakgrundsfärg med hjälp av Aspose.Cells för Python Excel-biblioteket**

Excel erbjuder funktioner för att sortera data baserat på bakgrundsfärg. Samma funktion tillhandahålls med hjälp av Aspose.Cells för Python via .NET med hjälp av DataSorter där [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor kan användas i [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) för att sortera data baserat på bakgrundsfärg. Alla celler som innehåller specificerad färg i [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) funktionen placeras överst eller underst enligt inställningen för SortOrder och ordningen för resten av cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/python-net/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
