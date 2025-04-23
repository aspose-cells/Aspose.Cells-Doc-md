---
title: Hur och Var man använder enumeratorer med C++
linktitle: Iterera data
type: docs
weight: 55
url: /sv/cpp/how-and-where-to-use-enumerators/
description: Lär dig hur och var man använder enumeratorer via API et Aspose.Cells for C++.
keywords: Hur man använder Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---

{{% alert color="primary" %}}

 En enumerator är ett objekt som ger möjlighet att traversera en behållare eller kollektion. Enumerators kan användas för att läsa data i kollektionen, men de kan inte ändra den underliggande kollektionen, medan IEnumerable är ett gränssnitt som definierar en metod GetEnumerator som returnerar ett IEnumerator-objekt, vilket i sin tur tillåter endast läsaccess till en kollektion.

Aspose.Cells API:er tillhandahåller ett gäng enumeratörer, denna artikel diskuterar huvudsakligen de tre typerna som listas nedan.

1. Cells Enumerator
1. Rows Enumerator
1. Kolumnenummer

{{% /alert %}}

## **Hur man använder Enumerators**

### **Cellers Enumerator**

Det finns olika sätt att komma åt Celler Enumerator, och man kan använda någon av dessa metoder baserat på programkraven. Här är metoderna som returnerar cellerna Enumerator.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

Alla ovan nämnda metoder returnerar enumeratorn som tillåter att traversera samlingen av celler som har initierats.

{{% alert color="primary" %}}

När man traverserar cellerna ska samlingen inte modifieras (operationer som kommer att orsaka en ny cell att instansieras eller befintlig cell att ta bort). Annars kanske inte Enumeratorn kan traversera alla celler korrekt (vissa element kan traverseras upprepade gånger eller hoppas över).

{{% /alert %}}

Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för en Cells-samling.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Radenummerator**

Enumsator för rader kan nås medan du använder [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/) metoden. Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Kolumner Hämtning**

 Kolumner kan nås medan du använder [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/) metoden. Följande kodexempel visar implementeringen av Get-metoden för [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Var man ska använda Enumerators**

För att diskutera fördelarna med att använda enumerators, låt oss ta ett exempel i realtid.

**Scenario**

 Ett applikationskrav är att traversera alla celler i en given [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) för att läsa deras värden. Det kan finnas flera sätt att implementera detta mål. Några demonstreras nedan.

### **Användning av Display Range**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **Användning av MaxDataRow & MaxDataColumn**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Som du kan observera använder båda ovan nämnda tillvägagångssätten mer eller mindre liknande logik, det vill säga; loopa över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av flera skäl som diskuteras nedan.

1. API:er som [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) & [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor kan användningen av dessa API:er försena prestandan.
1. I de flesta fall är inte alla celler i en given omfattning instansierade. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att bara kontrollera de initierade cellerna.
1. Åtkomst av en cell i en loop som Celler rad, kolumn kommer att orsaka att alla cellobjekt i ett område instansieras, vilket så småningom kan orsaka OutOfMemoryException.

## **Slutsats**

Baserat på ovan nämnda fakta är följande möjliga scenarier där enumerators bör användas.

1. Endast läsåtkomst av cellsamlingen krävs, dvs. kravet är att endast inspektera cellerna.
1. Ett stort antal celler ska traverseras.
1. Endast initialiserade celler/rader/kolumner ska traverseras.
