---
title: تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel باستخدام C++
linktitle: تحميل صورة ويب من عنوان URL إلى ورقة عمل إكسل
type: docs
weight: 30
url: /ar/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: تعلم كيفية تحويل صورة من URL إلى صورة مدمجة في Excel باستخدام C++ و API Aspose.Cells for C++.
keywords: عرض الصورة من URL في Excel، URL الصورة في Excel، عرض صورة في Excel من URL، إدراج صورة من URL في Excel، تحويل URL إلى صورة في Excel، صورة من URL في Excel، تحميل صورة من URL في Excel، C++، Excel
---

## تحميل صورة من عنوان URL إلى ورقة عمل إكسل

يوفر API Aspose.Cells for C++ طريقة مباشرة لتحميل الصور من URLs إلى أوراق عمل Excel. تشرح هذه المقالة كيفية تنزيل بيانات الصورة إلى تدفق ذاكرة وإدراجها في ورقة العمل باستخدام Aspose.Cells. تصبح الصورة مدمجة في ملف Excel ولا تتطلب عمليات تحميل خارجية عند الفتح.

## كود عينة

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

للحالات التي تتطلب صورًا محدثة دائمًا من URL، استخدم الطريقة الموضحة في [إدراج صورة مربوطة من عنوان ويب](/cells/ar/cpp/insert-a-linked-picture-from-web-address/). يقوم هذا الأسلوب بتحميل الصورة من URL في كل مرة يتم فيها فتح ورقة العمل.

{{% /alert %}}
