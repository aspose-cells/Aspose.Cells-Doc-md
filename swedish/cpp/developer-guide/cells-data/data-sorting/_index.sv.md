---
title: Datasortering med C++
linktitle: Data Sortering
type: docs
weight: 130
url: /sv/cpp/sort-data-of-excel/
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

Aspose.Cells tillhandahåller klassen [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/) som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och ange sorteringsordning för nyckeln.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) accepterar följande parametrar:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), cellerna för det underliggande arbetsbladet.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel använder mallfilen "Bok1.xls" skapad i Microsoft Excel. Efter att koden har utförts sorteras data på lämpligt sätt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Om du vill sortera *FrånVänsterTillHöger*, använd attributet [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Sortera data med bakgrundsfärg**

Excel erbjuder funktioner för att sortera data baserat på bakgrundsfärg. Samma funktion tillhandahålls med Aspose.Cells med användning av DataSorter där [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor kan användas i [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) för att sortera data baserat på bakgrundsfärg. Alla celler som innehåller specificerad färg i [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), funktion placeras överst eller nederst enligt SortOrder-inställningen och ordningen för resten av cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/cpp/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/cpp/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="cpp" >}}
