---
title: العمل مع شكل أو رسم ثلاثي الأبعاد بتنسيق الثلاثي الأبعاد (ThreeDFormat) مع C++
linktitle: العمل مع ثلاثة الأبعاد من الشكل أو الرسم البياني
type: docs
weight: 250
url: /ar/cpp/working-with-the-threedformat-of-shape-or-chart/
description: تعرّف على كيفية التلاعب بتنسيق ثلاثي الأبعاد للأشكال أو الرسوم باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**
توفّر Aspose.Cells خاصية [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) مع فصل [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) للعمل على تنسيق ثلاثي الأبعاد للأشكال أو الرسوم. يحتوي فصل [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) على خصائص مختلفة يمكن تعيينها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

## **العمل مع ثلاثة الأبعاد من الشكل أو الرسم البياني**
الكود النموذجي التالي يحمّل ملف إكسل المصدر ويمتلك الشكل الأول في ورقة العمل الأولى. ثم يضبط الخصائص الفرعية لخاصية [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) ويحفظ المصنف في ملف إكسل الناتج.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
