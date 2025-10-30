---
title: Infoga eller ta bort rader i ett Excel ark med C++
linktitle: Infoga eller ta bort rader
type: docs
weight: 20
url: /sv/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Denna artikel ger C++ koden för att infoga och ta bort rader i ett Excel ark.
keywords: c++ infoga eller ta bort rader i Excel ark, c++ infoga eller ta bort rader i Excel, c++ infoga rader i Excel, c++ ta bort rader i Excel, infoga eller ta bort rader i Excel ark med c++, infoga eller ta bort rader i Excel med c++, infoga rader i Excel med c++, ta bort rader i Excel med c++
---

{{% alert color="primary" %}}

När du skapar ett nytt arbetsblad eller arbetar med ett befintligt arbetsblad kan du behöva lägga till extra rader eller kolumner för att rymma data. Ibland kan du behöva ta bort rader eller kolumner från specificerade positioner i arbetsbladet.

{{% /alert %}}

Aspose.Cells erbjuder två metoder för att infoga och ta bort rader:  [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) och [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Dessa metoder är optimerade för prestanda och utför jobbet mycket snabbt.

För att infoga eller ta bort ett antal rader rekommenderar vi alltid att du använder  [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) och [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) metoderna istället för att använda  [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) eller [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) metoderna i en slinga.

Aspose.Cells fungerar på samma sätt som Microsoft Excel gör. När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt och till höger. När rader eller kolumner tas bort skiftas innehållet i arbetsbladet uppåt eller till vänster. Alla referenser i andra arbetsblad och celler uppdateras när rader läggs till eller tas bort.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
