---
title: 使用C++更改形状的调整值
linktitle: 更改形状的调整值
type: docs
weight: 2000
url: /zh/cpp/change-adjustment-values-of-the-shape/
description: 使用Aspose.Cells和C++修改Excel中的形状调整值。
---

{{% alert color="primary" %}}

Aspose.Cells 提供 [**Shape.Geometry.GetShapeAdjustValues**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/geometry/getshapeadjustvalues/) 属性以更改形状的调整点。在微软Excel用户界面中，调整显示为黄色菱形节点。例如：

- 圆角矩形有一个调整来改变拱形
- 三角形有一个调整来改变顶点的位置
- 梯形具有一个调整以更改顶部的宽度
- 箭头有两个调整，可改变箭头头部和尾部的形状

本文将解释如何使用 [**Shape.Geometry.GetShapeAdjustValues**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/geometry/getshapeadjustvalues/) 属性来更改不同形状的调整值。

{{% /alert %}}

## ** 更改调整值**

以下代码示例显示如何更改形状的调整值。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object from source excel file
    U16String inputFilePath = srcDir + u"source.xlsx";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first three shapes of the worksheet
    Shape shape1 = worksheet.GetShapes().Get(0);
    Shape shape2 = worksheet.GetShapes().Get(1);
    Shape shape3 = worksheet.GetShapes().Get(2);

    // Change the adjustment values of the shapes
    shape1.GetGeometry().GetShapeAdjustValues().Get(0).SetValue(0.5);
    shape2.GetGeometry().GetShapeAdjustValues().Get(0).SetValue(0.8);
    shape3.GetGeometry().GetShapeAdjustValues().Get(0).SetValue(0.5);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **在Excel中设置或更改圆角矩形文本框的尖端点**

以下示例演示如何在Excel中设置或更改圆角矩形文本框的尖端点位置。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for saving the workbook
    U16String filePath(u"");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a RoundedRectangularCallout to the worksheet
    Shape polygonShape = sheet.GetShapes().AddAutoShape(AutoShapeType::RoundedRectangularCallout, 0, 0, 0, 0, 0, 0);

    polygonShape.SetY(200); // Shape Top properties
    polygonShape.SetX(500); // Shape Left properties
    polygonShape.SetWidth(200); // Shape Width
    polygonShape.SetHeight(100); // Shape Height

    ShapeGuideCollection shapeGuides = polygonShape.GetGeometry().GetShapeAdjustValues();
    shapeGuides.Add(u"adj1", 1.02167); // The distance between the tip point and the center point
    shapeGuides.Add(u"adj2", -0.295);  // The distance between the tip point and the center point
    shapeGuides.Add(u"adj3", 0.16667); // Usually the default value

    // Save the workbook
    workbook.Save(filePath + u"res.xlsx", SaveFormat::Xlsx);

    // Read a new workbook
    workbook = Workbook(filePath + u"res.xlsx");
    sheet = workbook.GetWorksheets().Get(0);

    // Get a RoundedRectangularCallout from the worksheet
    polygonShape = sheet.GetShapes().Get(0);
    shapeGuides = polygonShape.GetGeometry().GetShapeAdjustValues();
    shapeGuides.Get(0).SetValue(0.7); // Modify the first shape guide value

    // Save the workbook again
    workbook.Save(filePath + u"res-resave.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
