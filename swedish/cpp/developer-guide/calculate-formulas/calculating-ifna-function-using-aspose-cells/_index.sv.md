---
title: Beräkning av IFNA funktionen med Aspose.Cells och C++
linktitle: Beräkning av IFNA funktionen
description: Hur man beräknar IFNA funktioner med Aspose.Cells biblioteket med C++. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoderna som tillhandahålls av Aspose.Cells för att beräkna IFNA funktionen och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, IFNA funktioner, beräkningar, C++
type: docs
weight: 40
url: /sv/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder beräkningen av IFNA Excel-funktionen. IFNA-funktionen returnerar det värde du specificerar om formeln returnerar felvärdet #N/A; annars returneras resultatet av formeln.

{{% /alert %}} 

## **Beräkning av IFNA-funktionen med Aspose.Cells**
Följande kodexempel illustrerar beräkningen av IFNA-funktionen med Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
