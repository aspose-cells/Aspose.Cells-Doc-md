--- 
title: Hur man kontrollerar fryst tillstånd utan Excel med C++ 
linktitle: Fruset tillstånd 
type: docs 
weight: 190 
url: /sv/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: I denna artikel kommer du att lära dig hur du programmässigt kan kontrollera det frysta tillståndet för ett Excel ark med C++ och Aspose.Cells API. 
--- 

## **Introduktion** 

I denna artikel kommer vi att lära oss hur man kontrollerar det frusna tillståndet för ett Excel-ark programmatiskt. Vi kan enkelt ta reda på om arket är fruset eller delat i MS Excel. Men finns det ett sätt att ta reda på om det är fruset eller delat med C++? Vi kan göra det med Aspose.Cells for C++. 

## **Är fönsterfönster frysta** 
Med Aspose.Cells for C++ kan vi kontrollera om fönstret är fruset och hur många rader och kolumner som är låsta. 

Använd [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) egenskapen för att kontrollera fönsterpanar och få låsta rader och kolumner med [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/) metoden. 
1. Konstruera Arbetsbok för att öppna filen. 
2. Kontrollera om arbetsbladet är fruset. 
3. Hämta de låsta raderna och kolumnerna. 

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

{{< app/cells/assistant language="cpp" >}}
