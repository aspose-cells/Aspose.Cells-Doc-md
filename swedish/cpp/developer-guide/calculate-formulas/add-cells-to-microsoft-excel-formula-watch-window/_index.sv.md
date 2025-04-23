---
title: Lägg till celler i Microsoft Excels Formelbevakningsfönster med C++
linktitle: Lägg till celler till formelvaktfönster
description: Lär dig hur du använder Aspose.Cells for C++ för att lägga till celler i formelbevakningsfönstret i Excel. Ladda eller skapa en Excel fil, manipulera celler, ställ in formler och spara den modifierade filen.
keywords: Aspose.Cells, Excel, Formel bevakningsfönster, Cell, Lägg till, C++
type: docs
weight: 60
url: /sv/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Möjliga användningsscenario**

Microsoft Excel bevakningsfönster är ett användbart verktyg för bekvämt att övervaka cellvärden och deras formler i ett fönster. Du kan öppna *Bevakningsfönster* i Microsoft Excel genom att klicka på *Formler > Bevakningsfönster*. Det har knappen *Lägg till bevakning* som kan användas för att lägga till celler för inspektion. På liknande sätt kan du använda [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/)-metoden för att lägga till celler i *Bevakningsfönstret* med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande exempelkod sätter formeln för cellerna C1 och E1 och lägger till båda i Bevaka fönstret. Den sparar sedan arbetsboken som en [utgångs Excel-fil](67338481.xlsx). Om du öppnar utgångs Excel-filen och tittar i *Bevakningsfönstret*, kommer du att se båda cellerna som visas i denna skärmdump.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
