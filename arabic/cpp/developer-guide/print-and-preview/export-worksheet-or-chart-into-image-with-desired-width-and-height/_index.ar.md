---
title: تصدير ورقة العمل أو المخطط إلى صورة مع عرض وارتفاع مرغوبين باستخدام C++
linktitle: تصدير ورقة العمل أو الرسم البياني إلى صورة بالعرض والارتفاع المطلوبين
type: docs
weight: 290
url: /ar/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: استخدام Aspose.Cells لتصدير ورقة العمل أو المخطط إلى صورة باستخدام العرض والارتفاع المطلوبين في C++.
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لتصدير ورقة العمل أو الرسم البياني الخاص بك إلى صورة بالعرض والارتفاع المطلوبين. يوفر الأسلوب [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) لتعيين العرض والارتفاع المطلوبين للصورة المصدرة. يتم تحديد العرض والارتفاع بوحدة البكسل.

{{% /alert %}}

الكود التالي يقوم بتصدير ورقة العمل إلى صورة بحجم 400x400.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleWorksheetToImageDesiredSize.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetDesiredSize(400, 400, false);

    // Render sheet into image
    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outputDir + u"outputWorksheetToImageDesiredSize.png");

    std::cout << "Worksheet rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
