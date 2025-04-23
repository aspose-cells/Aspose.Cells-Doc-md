--- 
title: Как проверить замороженное состояние без Excel с C++ 
linktitle: Замороженное состояние 
type: docs 
weight: 190 
url: /ru/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: В этой статье вы узнаете, как программно проверить замороженное состояние листа Excel, используя C++ с API Aspose.Cells. 
--- 

## **Введение** 

В этой статье мы научимся, как программно проверять замороженное состояние листа Excel. Мы можем легко определить, заморожен ли лист или разделен в MS Excel. Но есть ли способ определить это программно на C++? Мы можем сделать это с помощью Aspose.Cells for C++. 

## **Заморожены ли оконные рамы** 
С помощью Aspose.Cells for C++ мы можем проверить, заблокировано ли окно и сколько строк и столбцов заблокировано. 

Пожалуйста, используйте свойство [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/), чтобы проверить состояние оконных панелей и получить заблокированные строки и столбцы с помощью метода [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/). 
1. Создайте рабочую книгу для открытия файла. 
2. Проверьте, заморожен ли лист. 
3. Получить заблокированные строки и столбцы. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

