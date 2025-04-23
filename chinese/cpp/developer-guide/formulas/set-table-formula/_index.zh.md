---
title: 在表格或列表对象中自动传播公式，以便在输入新行数据时自动更新，使用 C++
linktitle: 设置Table公式
type: docs
weight: 260
url: /zh/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: 学习如何在表格或列表对象中自动传播公式，当输入新数据时，使用 Aspose.Cells for C++。
---

## **可能的使用场景**
有时候，你希望在输入新数据时，表格或列表对象中的公式自动传播到新行。这是 Microsoft Excel 的默认行为。要用 Aspose.Cells 实现相同的功能，可以使用 [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/) 方法。

## **在输入新数据时自动传播表或列表对象中的公式**
以下示例代码以此方式创建了一个表格或列表对象，使得在第 B 列中的公式会在输入新数据时自动传播到新行。请查看此代码生成的 [输出 Excel 文件](5115469.xlsx)。如果在 A3 单元格中输入任何数字，你会看到 B2 单元格中的公式会自动传播到 B3。

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
