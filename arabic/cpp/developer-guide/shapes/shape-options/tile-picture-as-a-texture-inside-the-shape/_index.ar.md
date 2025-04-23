---
title: تكرار الصورة كملمس داخل الشكل باستخدام C++
linktitle: صورة البلاط كقشرة داخل الشكل
type: docs
weight: 1700
url: /ar/cpp/tile-picture-as-a-texture-inside-the-shape/
description: تعلم كيفية تكرار صورة كملمس داخل شكل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما تكون الصورة صغيرة ولا تغطي السطح بأكمله للشكل دون فقدان جودتها ، فإن لديك خيار تبطينها. يملأ التبطين سطح الشكل بصورة صغيرة عن طريق تكرارها كما لو أنها بلاط.

## **صورة البلاط كقشرة داخل الشكل**

يمكنك ملء سطح الشكل ببعض الصورة وتبطينها باستخدام الخاصية [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) وضبطها على ** صحيح **. يرجى الرجوع إلى الشيفرة المرجعية التالية ، [ملف Excel المرجعي](46465050.xlsx) وكذلك لقطة الشاشة كمرجع.

## **لقطة شاشة**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **الكود المثالي**

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
