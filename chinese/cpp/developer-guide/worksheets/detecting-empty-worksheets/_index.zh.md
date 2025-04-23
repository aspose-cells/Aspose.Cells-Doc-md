---
title: 使用C++检测空白工作表
linktitle: 检测空工作表
type: docs
weight: 410
url: /zh/cpp/detecting-empty-worksheets/
description: 本文展示了如何使用Aspose.Cells的C++ API编程检测Excel工作簿中的空白工作表。
keywords: 检测空白工作表 C++，查找空白Excel工作表 C++
---

## **检查已填充的单元格**

工作表可以包含一个或多个已填充值的单元格，这些值可以是文本、数字、日期/时间、公式或基于公式的值。在这种情况下，容易判断工作表是否为空。我们只需要检查[**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)或[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)属性。如果这些属性返回零或正数，代表有一个或多个单元格已被填写；如果任何一个返回-1，表示没有任何单元格被填充。

{{% alert color="primary" %}}

 行和列的集合是从零开始索引的，因此位于第0行第0列的单元格即为A1单元格。

{{% /alert %}}

## **检测空初始化单元格**

 所有具有值的单元格都会被自动初始化。然而，可能存在只应用格式的空单元格。在这种情况下，[**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)或[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)属性会返回-1，表示没有任何已填充的值。但由于单元格格式导致的已初始化单元格无法通过此方法检测。如要检查工作表是否存在空的已初始化单元格，建议对从[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合获取的枚举器使用`MoveNext`方法。如果`MoveNext`返回true，说明工作表中存在一个或多个已初始化的单元格。

## **检查形状**

某个工作表可能没有任何已填充的单元格，但它可能包含形状和对象，如控件、图表、图片等。若要检查工作表中是否存在任何形状，可以检查[**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/)属性。任何正值都表示工作表中存在形状。

## **编程示例**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
