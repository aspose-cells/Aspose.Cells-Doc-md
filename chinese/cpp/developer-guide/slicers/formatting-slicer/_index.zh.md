---
title: 用C++格式化切片器
linktitle: 格式化切片器
type: docs
weight: 20
url: /zh/cpp/formatting-slicer/
description: 使用Aspose.Cells和C++格式化Microsoft Excel中的切片器。
---

## **可能的使用场景**

你可以通过设置其列数或样式等来格式化Excel中的切片器。Aspose.Cells还允许你使用[**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/)和[**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/)属性实现此操作。

## **格式化切片器**

请查看以下代码示例；它加载包含切片器的[示例Excel文件](67338473.xlsx)，访问切片器并设置其列数和样式类型，然后另存为[输出Excel文件](67338474.xlsx)。截图展示了执行示例代码后，切片器的样子。

![todo:image_alt_text](formatting-slicer_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
