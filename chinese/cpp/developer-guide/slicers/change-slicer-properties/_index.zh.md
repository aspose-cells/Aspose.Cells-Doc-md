---
title: 用C++更改切片器属性
linktitle: 更改切片器属性
type: docs
weight: 70
url: /zh/cpp/change-slicer-properties/
description: 使用Aspose.Cells和C++更改单个Excel文件中切片器的属性。
---

## **可能的使用场景**

也许会出现您希望更改切片器的属性的情况，比如位置或行高等。Aspose.Cells为您提供了更新这些属性的选项。

## **更改切片器属性**

请查看以下示例代码。它加载包含表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器，并更改其属性，如行高、宽度、是否可打印、标题等。将工作簿另存为[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
