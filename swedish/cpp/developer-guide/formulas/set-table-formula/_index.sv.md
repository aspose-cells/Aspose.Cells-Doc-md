---
title: Sprid formel i tabell eller listobjekt automatiskt när data matas in i nya rader med C++
linktitle: Ställer in tabellformel
type: docs
weight: 260
url: /sv/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Lär dig hur du sprider formler automatiskt i tabeller eller listobjekt när du matar in ny data med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
 Ibland vill du att en formel i din tabell eller listobjekt automatiskt ska spridas till nya rader när du matar in ny data. Detta är standardbeteendet i Microsoft Excel. För att uppnå samma funktionalitet med Aspose.Cells, använd metoden [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/).

## **Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader**
Följande exempel på kod skapar en tabell eller listobjekt så att formeln i kolumn B automatiskt sprids till nya rader när du matar in ny data. Kontrollera den [utdataexcel-fil](5115469.xlsx) som genereras med denna kod. Om du skriver in ett tal i cell A3, kommer du att se att formeln i cell B2 automatiskt sprids till cell B3.

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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
