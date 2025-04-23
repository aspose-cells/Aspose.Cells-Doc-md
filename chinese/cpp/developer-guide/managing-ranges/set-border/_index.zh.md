---
title: 用C++设置范围边框
type: docs
weight: 600
url: /zh/cpp/set-range-border/
description: 学习如何在Aspose.Cells中用C++设置范围边框。
---

## **可能的使用场景**
当你想为范围设置边框时，不需要逐个设置每个单元格。你可以直接在范围上设置边框。Aspose.Cells提供了此功能。本文提供了使用Aspose.Cells设置范围边框的示例代码。

## **在Excel中设置范围边框**
要在Excel中设置范围的边框，可以按照以下步骤进行：
1. 选择要应用边框的单元格范围。
2. 在功能区“主页”选项卡中，找到“字体”组。
3. 在“字体”组内，单击“边框”下拉按钮。
<br>
<img src="border.png" />
4. 从下拉菜单中选择要应用的边框类型。您可以选择预设的边框样式或自定义您自己的边框。
5. 选择所需的边框样式后，边框将应用于所选的单元格范围。

## **使用Aspose.Cells设置范围边框**
此示例演示如何：

1. 创建一个工作簿。
2. 在第一个工作表的单元格中添加数据。
3. 创建一个[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range)。
4. 设置范围的内部边框。
5. 设置范围的外部边框。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
