---
title: عرض ورقة العمل على سياق رسومي باستخدام C++
linktitle: تقديم ورقة العمل إلى السياق الرسومي
type: docs
weight: 300
url: /ar/cpp/render-worksheet-to-graphic-context/
description: تعلم كيفية عرض ورقة عمل على سياق رسومي باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكن الآن لـ Aspose.Cells عرض ورقة عمل على سياق رسومي. يمكن أن يكون السياق الرسومي أي شيء مثل ملف صورة، شاشة، أو طابعة، وما إلى ذلك. يرجى استخدام أحد الطريقتين التاليتين لعرض ورقة العمل على سياق رسومي.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

يوضح الكود التالي كيفية استخدام Aspose.Cells لعرض ورقة عمل على سياق رسومي. عند تنفيذ الكود، سيقوم بطباعة ورقة العمل بالكامل وملء المساحة الفارغة بالبلاو بلون أزرق في السياق الرسومي وحفظ الصورة كملف **OutputImage_out_.png**. يمكنك استخدام أي ملف إكسل للمصدر لتجربة هذا الكود. يرجى أيضًا قراءة التعليقات داخل الكود لفهم أفضل.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
