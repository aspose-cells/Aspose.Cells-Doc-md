--- 
title: 如何在没有Excel的情况下用C++检测冻结状态 
linktitle: 冻结状态 
type: docs 
weight: 190 
url: /zh/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: 在本文中，您将学习如何使用C++的Aspose.Cells API以编程方式检测Excel工作表的冻结状态。 
--- 

## **介绍** 

在本文中，我们将学习如何以编程方式检查Excel工作表的冻结状态。我们可以轻松判断工作表是否被冻结或拆分，但是否有办法用C++判断？我们可以使用Aspose.Cells for C++来实现。 

## **窗格是否冻结** 
使用Aspose.Cells for C++，可以检查窗口是否被冻结以及锁定了多少行和列。 

请使用[**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/)属性检查窗口面板的状态，并使用[**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/)方法获取锁定的行和列。 
1.构建工作簿以打开文件。 
2.检查工作表是否被冻结。 
3. 获取锁定的行和列。 

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

