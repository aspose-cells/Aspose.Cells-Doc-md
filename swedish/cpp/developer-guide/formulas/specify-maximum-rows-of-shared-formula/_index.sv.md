---
title: Ange maximala rader för delad formel med C++
linktitle: Ange maximala rader för delad formel
type: docs
weight: 40
url: /sv/cpp/specify-maximum-rows-of-shared-formula/
description: Lär dig hur du specificerar maximala rader för delad formel i Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Standardmaximalt antal rader för delad formel är 64. Det kan vara vilken siffra som helst, t.ex. 1000. Prestandan för den delade formeln påverkas av antalet rader. Därför tillhandahåller Aspose.Cells egenskapen [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) som kan användas för att specificera det maximala antalet rader för delad formel. Den delade formeln delas upp i flera delade formler om det totala antalet rader är större än detta, precis som visas i följande skärmdump.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Ange maximala rader för delad formel**

Följande exempelkod förklarar användningen av egenskapen [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). Den sätter max antal rader för den delade formeln till 5 och lägger till den delade formeln i cell D1 för 100 rader och sparar till [utdata Excel-fil](61767856.xlsx). Om du extraherar innehållet i Excel-filen och granskar *sheet1.xml* kan du se att den delade formeln delas efter varje 5:e rad, som markerats i ovanstående skärmdump.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
