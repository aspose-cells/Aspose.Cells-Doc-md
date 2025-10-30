---
title: Şeklin Ayar Değerlerini Değiştirme C++ ile
linktitle: Şekil Ayar Değerlerini Değiştir
type: docs
weight: 2000
url: /tr/cpp/change-adjustment-values-of-the-shape/
description: Aspose.Cells ile Excel de şekil ayar değerlerini değiştirme.
---

{{% alert color="primary" %}}

Aspose.Cells, şekillerin ayar noktalarını değiştirmek için [**Shape.Geometry.GetShapeAdjustValues**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/geometry/getshapeadjustvalues/) özelliğini sağlar. Microsoft Excel arayüzünde, ayarlamalar sarı elmas düğme noktaları olarak görüntülenir. Örneğin:

- Yuvarlatılmış Dikdörtgenin yay değiştirmek için ayarlaması vardır
- Üçgenin nokta konumunu değiştirmek için bir ayarlaması vardır
- Trapezoid, üst genişliği değiştirmek için bir ayarlamaya sahiptir
- Oklar, baş ve kuyruk şeklini değiştirmek için iki ayarlamaya sahiptir

Bu makale, farklı şekillerin ayar değerini değiştirmek için [**Shape.Geometry.GetShapeAdjustValues**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/geometry/getshapeadjustvalues/) özelliğinin kullanımını açıklayacaktır.

{{% /alert %}}

## **Ayar Değerlerini Değiştir**

Aşağıdaki kod örneği, şeklin ayar değerlerini nasıl değiştireceğinizi göstermektedir.

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

## **Excel'de RoundedRectangularCallout ipucu noktasını nasıl ayarlar veya değiştirirsiniz**

Aşağıdaki kod örneği, Excel'de yuvarlak dikdörtgen çağrı noktasını ayarlama veya değiştirme nasıl yapılacağını gösterir.

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
