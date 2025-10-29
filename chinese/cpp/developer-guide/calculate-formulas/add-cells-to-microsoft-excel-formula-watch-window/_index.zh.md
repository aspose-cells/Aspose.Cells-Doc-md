---
title: 用C++向Microsoft Excel公式监视窗口添加单元格
linktitle: 向公式监视窗口添加单元格
description: 学习如何使用Aspose.Cells for C++在Excel中向公式监视窗口添加单元格。加载或创建一个Excel文件，操作单元格，设置公式，然后保存修改后的文件。
keywords: Aspose.Cells、Excel、公式监视窗口、单元格、添加、C++
type: docs
weight: 60
url: /zh/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel的监视窗口是一个方便监控单元格值及其公式的工具。你可以在Microsoft Excel中点击“公式 > 监视窗口”打开*监视窗口*。它有“添加监视”按钮，可以用来添加单元格进行检查。同样，也可以使用[**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/)方法通过Aspose.Cells API将单元格添加到*监视窗口*。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了C1和E1单元格的公式并将它们添加到监视窗口。然后将工作簿保存为[输出Excel文件](67338481.xlsx)。如果你打开输出Excel文件并查看*监视窗口*，会看到两个单元格，如截图所示。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
