---
title: 用C++查找工作表是否为对话框工作表
linktitle: 查找工作表是否为对话框工作表
type: docs
weight: 90
url: /zh/cpp/find-if-the-worksheet-is-dialog-sheet/
description: 对话框工作表是早期格式的工作表。本文提供了使用C++ API判断Excel工作表是否为对话框工作表的说明和示例代码。
keywords: 使用C++查找Excel工作表对话框类型，工作表对话框C++
---

## **可能的使用场景**

对话工作表是一种包含对话框的工作表的旧格式。这样的工作表可能是由Microsoft Excel的旧版本（如2003）插入的，就像这张截图中所显示的一样。它也可以在较新版本的Microsoft Excel（如2016）中使用VBA插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

 可以使用Aspose.Cells的[**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/)属性判断工作表是否为对话框工作表。如果返回枚举值[**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/)，则表示该工作表为对话框工作表。

## **查找工作表是否为对话框工作表**

 以下示例代码加载包含对话框工作表的示例Excel文件(64716820.xlsx)，检查[**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/)属性并与[**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/)比较，然后输出结果信息。详见下方控制台输出。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **控制台输出**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
