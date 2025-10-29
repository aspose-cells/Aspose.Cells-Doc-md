---
title: Автоматическая передача формул в таблицах или списках при вводе данных в новые строки с помощью C++
linktitle: Устанавливает формулу таблицы
type: docs
weight: 260
url: /ru/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Узнайте, как автоматически распространять формулы в таблицах или списках при вводе новых данных, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Иногда при вводе новых данных вам нужно, чтобы формула в вашей таблице или списке автоматически распространилась на новые строки. Это поведение по умолчанию в Microsoft Excel. Чтобы добиться этого в Aspose.Cells, используйте метод [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/).

## **Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки**
Следующий пример кода создает таблицу или списковый объект таким образом, что формула в столбце B автоматически распространяется на новые строки при вводе новых данных. Проверьте [созданный экспортированный файл Excel](5115469.xlsx). Если вы введете любое число в ячейку A3, вы увидите, что формула в ячейке B2 автоматически распространяется на ячейку B3.

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
