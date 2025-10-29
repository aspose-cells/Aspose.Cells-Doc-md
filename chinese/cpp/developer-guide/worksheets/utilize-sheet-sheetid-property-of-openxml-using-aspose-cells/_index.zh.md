---
title: 使用C++利用OpenXml的Sheet.SheetId属性
linktitle: 利用OpenXml的Sheet.SheetId属性
type: docs
weight: 200
url: /zh/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: 本文演示如何使用C++的Excel操作API或库，编程实现OpenXml的Sheet.SheetId属性的使用。
keywords: openxml的Sheet id属性的C++实现，excel工作表的sheet id C++
---

## **可能的使用场景**

Sheet.SheetId属性位于DocumentFormat.OpenXml.Spreadsheet命名空间内，是OpenXml的一部分。您可以在*workbook.xml*文件中看到此属性及其值，如下屏幕截图所示。Aspose.Cells提供了[**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/)属性作为等价属性。

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性**

以下示例代码加载了[示例Excel文件](51740716.xlsx)，读取其表格或标签ID，然后将其分配为新的标签ID并保存为[输出Excel文件](51740717.xlsx)。还请参见下方给出的代码的控制台输出作为参考。

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **控制台输出**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
