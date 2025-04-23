---
title: إنشاء صور DataBars للتنسيق الشرطي باستخدام C++
linktitle: إنشاء بيانات شكل معايرة شريطية للصور
description: Aspose.Cells هو مكتبة C++ للتعامل مع ملفات جداول البيانات. يدعم إنشاء أشرطة بيانات وصور ذات تنسيق شرطي، مما يتيح للمستخدمين تخصيص عرض الجدول استنادًا إلى قيمة الخلايا. ستقدم هذه المقالة طريقة استخدام مكتبة Aspose.Cells لإنشاء أشرطة بيانات وصور ذات تنسيق شرطي.
keywords: Aspose.Cells، التنسيق الشرطي، شرائط بيانات، صور، جداول بيانات
type: docs
weight: 40
url: /ar/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

أحيانًا ، تحتاج إلى إنشاء صور شرائط البيانات التنسيقية الشرطية. يمكنك استخدام طريقة Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) لإنشاء هذه الصور. توضح هذه المقالة كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

ينتج رمز العينة التالي صورة DataBar للخلية C1. أولاً، يقوم بالوصول إلى كائن شرط التنسيق للخلية، ومن ذلك الكائن، يصل إلى [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) ويستخدم طريقة [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) لإنشاء صورة الخلية. أخيرًا، يحفظ الصورة على القرص.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
