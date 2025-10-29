---
title: 使用C++控制工作表标签栏的方法
linktitle: 如何控制选项卡工具栏
type: docs
weight: 600
url: /zh/cpp/how-to-control-sheet-tab-bar/
description: 学习如何通过Aspose.Cells for C++ API控制工作表标签栏。
keywords: 如何控制选项卡工具栏，操作选项卡工具栏，设置选项卡工具栏，控制选项卡工具栏。 
---

## **可能的使用场景**
当需要调整Excel工作表标签栏的显示时，你需要知道如何控制标签栏，例如隐藏或显示标签栏、改变标签栏宽度、指定第一个可见标签等。Aspose.Cells支持这些功能。Aspose.Cells提供以下属性和方法帮助你实现目标。

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## ** 使用Aspose.Cells for C++控制工作表标签栏的方法**
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 显示工作表标签并设置标签栏的宽度。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

结果文件预览：
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="cpp" >}}
