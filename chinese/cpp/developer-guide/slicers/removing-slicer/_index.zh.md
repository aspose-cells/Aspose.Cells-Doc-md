---
title: 用C++移除切片器
linktitle: 移除切片器
type: docs
weight: 30
url: /zh/cpp/removing-slicer/
description: 学习如何用程序在Excel文件中移除切片器，使用Aspose.Cells for C++。
---

## **可能的使用场景**

如果想在Microsoft Excel中移除切片器，只需选择它并按*Delete*按钮。同样，要用Aspose.Cells API程序化移除，可以使用[**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/)方法。这将从工作表中删除切片器。

## **移除切片器**

以下示例代码加载了包含现有切片器的[sample Excel file](67338478.xlsx)。它访问切片器，然后将其移除，最后将工作簿保存为[output Excel file](67338477.xlsx)。以下截图展示了在执行示例代码后将要移除的切片器。

![todo:image_alt_text](removing-slicer_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
