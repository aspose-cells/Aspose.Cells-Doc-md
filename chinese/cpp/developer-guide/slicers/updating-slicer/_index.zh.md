---
title: 用C++更新切片器
linktitle: 更新切片器
type: docs
weight: 50
url: /zh/cpp/updating-slicer/
description: 本文介绍如何通过更新切片器来更新关联的透视表，使用Aspose.Cells for C++ API。
keywords: Aspose.Cells C++更新切片器，如何在C++中更改切片器、调整切片器、选择或取消选择切片器项。
---

## **可能的使用场景**

如果你想在Microsoft Excel中更新切片器，选择或取消选择其项目，它将相应地更新切片器表或透视表。请使用[**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/)选择或取消选择切片器项，然后调用[**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/)方法更新切片器表或透视表。

## **如何更新数据透视切片器**

以下示例代码加载包含现有数据透视切片器的[示例 Excel 文件](67338475.xlsx)，取消选择数据透视切片器的第 2 和第 3 个项目，并刷新数据透视切片器，然后将工作簿保存为[输出 Excel 文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。如屏幕截图所示，使用选定项目刷新数据透视切片器也已相应地刷新了数据透视表。

![todo:image_alt_text](updating-slicer_1.png)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
