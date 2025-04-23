---
title: 用C++渲染切片器
type: docs
weight: 40
url: /zh/cpp/rendering-slicer/
description: 使用Aspose.Cells和C++渲染Excel文件中的切片器。
---

## **可能的使用场景**
Aspose.Cells支持对切片器形状进行渲染。如果将工作表转换为图像，或者将工作簿保存为PDF或HTML格式，您会看到切片器被正确地渲染。
## **呈现切片器**
以下示例代码加载包含现有切片器的[示例Excel文件](67338479.xlsx)，通过设置仅覆盖切片器的打印区域将工作表转换为图片。以下图片为[输出图片](67338480.png)，展示渲染的切片器。可以看到，切片器已正确渲染，与示例Excel文件中一样。

![todo:image_alt_text](rendering-slicer_1)
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
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
