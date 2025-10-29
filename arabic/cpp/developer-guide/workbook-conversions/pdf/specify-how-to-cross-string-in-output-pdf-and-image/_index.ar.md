---
title: تحديد كيفية عبور النص في ملف PDF والصورة الناتجة باستخدام C++
linktitle: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 120
url: /ar/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: تعلم كيفية التحكم في تجاوز النص في مخرجات PDF والصورة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما تحتوي الخلية على نص أو سلسلة أكبر من عرض الخلية، يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة أو null. عند حفظ ملف Excel الخاص بك إلى PDF أو صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). القيم التالية هي:

- **TextCrossType.Default**: عرض النص مثل MS Excel ويعتمد على الخلية التالية. إذا كانت الخلية التالية null، سيتجاوز النص أو سيتم اقتطاعه.

- **TextCrossType.CrossKeep**: عرض النص مثل تصدير MS Excel إلى PDF/صور.

- **TextCrossType.CrossOverride**: عرض كل النص عن طريق عبور خلايا أخرى وتجاوز نص الخلايا المعترضة.

- **TextCrossType.StrictInCell**: عرض السلسلة فقط ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يعرض الرمز النموذجي التالي تحميل ملف Excel النموذجي وحفظه إلى تنسيق PDF/صور عن طريق تحديد قيم مختلفة [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### مثال على الكود

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
