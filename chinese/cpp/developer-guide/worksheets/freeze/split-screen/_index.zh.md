---
title: 用 C++ 在 Excel 工作表中分屏
linktitle: 分割屏幕
type: docs
weight: 190
url: /zh/cpp/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将学习如何通过编程方式使用 C++ 将工作表分成两部分或四部分，以在不同的窗格中显示特定的行和/或列。
keywords: 冻结顶部行，冻结顶部行。
---

## **介绍**

在本文中，我们将学习如何通过分屏将工作表分成两部分或四部分，以显示特定的行和/或列。在处理大型数据集时，我们需要同时查看同一工作表中的几个区域以便比较不同的数据子集。分屏功能可以满足您的需求。

## **如何在Excel中分割屏幕**
要将工作表分割成两个或四个部分，请按照以下操作：

1. 选择要分割的行/列/单元格之前的位置。
2. 在“查看”选项卡上，在“窗口”组中，单击“拆分”按钮。

**![拆分屏幕](Split-Screen.png)**

## **在列上垂直拆分工作表**

要在电子表格的两个区域垂直分隔，选择要在其右侧出现分隔的列，并在Excel中单击“拆分”按钮。

使用 Aspose.Cells for C++ 轻松编程垂直分割工作表中的列，只需在顶部行中选择一个单元格作为活动单元格，然后
使用 [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) 方法进行拆分。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **在行上水平拆分工作表**
要在Excel中水平分隔您的Excel窗口，请选择要在其下方发生分隔的行。

使用 Aspose.Cells for C++ 轻松编程水平分割工作表中的行，只需在左侧列中选择一个单元格作为活动单元格，然后
使用 [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) 方法进行拆分。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **将工作表分成四部分**
要同时查看同一工作表的四个不同部分，请在Excel中垂直和水平拆分屏幕。

使用 Aspose.Cells for C++ 轻松编程垂直分割工作表中的列，只需选择一个不在第一行和第一列的单元格作为活动单元格，然后
使用 [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) 方法进行拆分。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **如何移除拆分**
要移除工作表的拆分，只需再次单击“拆分”按钮。

Aspose.Cells for C++ 提供了一种 [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) 方法来移除分割设置。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
