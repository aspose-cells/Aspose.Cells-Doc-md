---
title: إضافة نص فن الكلمة مع أنماط مدمجة باستخدام C++
linktitle: إضافة نص فني بأنماط مضمنة
type: docs
weight: 270
url: /ar/cpp/add-word-art-text-with-built-in-styles/
description: تعلم كيفية إضافة نص فن الكلمات باستخدام الأنماط المدمجة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك إضافة نص فن الكلمات باستخدام Aspose.Cells. يرجى استخدام [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) لهذا الغرض.

## **إضافة نص Word Art بأنماط مدمجة**
يقوم الكود النموذجي التالي بإضافة نصوص فنية بأنماط مدمجة مختلفة. يُرجى التحقق من [ملف الإكسل الناتج](5115470.xlsx) الذي تم إنشاؤه بهذا الكود. هكذا يبدو [ملف الإكسل الناتج](5115470.xlsx) في Microsoft Excel.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
