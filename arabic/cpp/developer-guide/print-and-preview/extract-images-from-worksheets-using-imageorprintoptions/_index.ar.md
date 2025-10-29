---
title: استخراج الصور من أوراق العمل باستخدام ImageOrPrintOptions مع C++
linktitle: استخراج الصور من ورق العمل
type: docs
weight: 140
url: /ar/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: تعلم كيفية استخراج الصور من أوراق عمل Excel وحفظها على محرك أقراص محلي باستخدام رقم النموذج Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

يمكن لمستخدمي Microsoft Excel إضافة صور إلى جداول البيانات. باستخدام Aspose.Cells ، من الممكن قراءة الصور من ملفات Microsoft Excel وحفظها على محرك أقراص محلي. يوضح هذا المقال كيفية القيام بذلك.

{{% /alert %}} 

يوضح الكود العيني أدناه كيفية استخراج الصور من ملف Excel وحفظها.

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

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
