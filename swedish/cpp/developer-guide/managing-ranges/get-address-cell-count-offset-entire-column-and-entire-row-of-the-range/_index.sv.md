---
title: Hämta adress, cellantal, offset, hela kolumnen och hela raden i intervallet med C++
linktitle: Hämta adress, cellantal, offset, hela kolumnen och hela raden i intervallet
type: docs
weight: 330
url: /sv/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Lär dig hur man får adress, cellantal, offset, hela kolumnen och hela raden för ett intervall med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller `Range`-objektet, som har olika hjälpfunktioner som underlättar arbetet med Excel-intervall. Denna artikel illustrerar användningen av följande metoder eller egenskaper för `Range`-objektet:

- **Adress**

  Hämtar intervalladressen.

- **Cellräkning**

  Hämtar det totala cellantalet i intervallet.

- **Offset**

  Hämtar ett intervall med offset.

- **Hela kolumnen**

  Hämtar ett `Range`-objekt som representerar hela kolumnen (eller kolumnerna) som innehåller det angivna intervallet.

- **Hela raden**

  Hämtar ett `Range`-objekt som representerar hela raden (eller rader) som innehåller det angivna intervallet.

## **Hämta adress, cellantal, offset, hela kolumnen och hela raden i intervallet**
Följande exempel kod förklarar användningen av de ovan nämnda metoderna och egenskaperna. Vänligen se konsolutmatningen av koden nedan som referens.

## **Exempelkod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
