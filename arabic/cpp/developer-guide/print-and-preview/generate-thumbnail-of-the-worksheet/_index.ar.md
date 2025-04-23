---
title: إنشاء صورة مصغرة لورقة العمل باستخدام C++
linktitle: إنشاء صورة مصغرة لورقة العمل
type: docs
weight: 110
url: /ar/cpp/generate-thumbnail-of-the-worksheet/
description: إنشاء صور مصغرة لورقة العمل كصور باستخدام رقم النموذج Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

يمكن أن يكون من المفيد إنشاء صور مصغرة من ورقة العمل. الصورة المصغرة هي صورة صغيرة يمكن لصقها في مستند Word أو عرض تقديمي بوربوينت لإعطاء معاينة لمحتوى ورقة العمل. يمكن إضافتها إلى صفحة الويب مع رابط لتنزيل الوثيقة الأصلية ولها العديد من الاستخدامات الأخرى.

{{% /alert %}} 

يسمح رقم النموذج Aspose.Cells for C++ بإخراج أوراق العمل إلى ملفات صور، مما يجعل إنشاء الصور المصغرة بسيطًا. يُظهر الكود التالي كيفية إخراج أوراق العمل إلى ملفات صور باستخدام C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
