--- 
title: How to check Frozen State without Excel with C++ 
linktitle: Frozen State 
type: docs 
weight: 190 
url: /cpp/how-to-check-frozen-state-of-excel-worksheet 
description: In this article, you will learn how to check the frozen state of an Excel worksheet programmatically using C++ with the Aspose.Cells API. 
--- 

## **Introduction** 

In this article, we will learn how to check the frozen state of an Excel worksheet programmatically. We can simply find whether the worksheet is frozen or split in MS Excel. But is there a way to find whether it is frozen or split with C++? We can do it with Aspose.Cells for C++. 

## **Are Window Panes Frozen** 
With Aspose.Cells for C++, we can check whether the window is frozen and how many rows and columns are locked. 

Please use the [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) property to check the state of window panes and get locked rows and columns with the [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/) method. 
1. Construct Workbook to open the file. 
2. Check whether the worksheet is frozen. 
3. Get the locked rows and columns. 

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
 