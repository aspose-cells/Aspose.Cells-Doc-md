---
title: シェイプの調整値をC++で変更
linktitle: シェイプの調整値の変更
type: docs
weight: 2000
url: /ja/cpp/change-adjustment-values-of-the-shape/
description: Aspose.CellsとC++を使用してExcelで図形調整値を変更
---

{{% alert color="primary" %}}

Aspose.Cells は、シェイプの調整ポイントを変更するための [**Shape.Geometry.GetShapeAdjustValues**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/geometry/getshapeadjustvalues/) プロパティを提供します。Microsoft Excel の UI では、調整は黄色のダイヤモンドノードとして表示されます。例:

- 角丸四角形は、円弧を変更するための調整があります
- 三角形は、ポイントの位置を変更するための調整があります
- 台形は、上部の幅を変更するための調整があります
- 矢印には、頭部と末尾の形状を変更するための2つの調整があります

この記事では、異なるシェイプの調整値を変更するための [**Shape.Geometry.GetShapeAdjustValues**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/geometry/getshapeadjustvalues/) プロパティの使用方法について説明します。

{{% /alert %}}

## **調整値の変更**

以下のコードサンプルは、シェイプの調整値を変更する方法を示しています。

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

## **ExcelでRoundedRectangularCalloutの先端点を設定または変更する方法**

以下のコード例は、Excelでラウンド長方形のコールアウトの先端点位置を設定または変更する方法を示しています。

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
