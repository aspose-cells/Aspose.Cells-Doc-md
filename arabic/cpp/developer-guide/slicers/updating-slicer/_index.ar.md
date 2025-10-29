---
title: تحديث مقطع التصفح باستخدام C++
linktitle: تحديث المقسم
type: docs
weight: 50
url: /ar/cpp/updating-slicer/
description: توضح هذه المقالة كيفية تحديث جداول Pivot المرتبطة عن طريق تحديث مقاطع التصفح باستخدام API Aspose.Cells for C++.
keywords: تحديث مقطع التصفح في Aspose.Cells باستخدام C++، كيفية تغيير مقطع التصفح، كيفية ضبط مقطع التصفح في C++، كيفية اختيار أو إلغاء اختيار عناصر المقطع.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تريد تحديث مقطع التصفح في Microsoft Excel، حدد أو إلغاء تحديد عناصره، ثم سيتم تحديث جدول المقطع أو جدول Pivot وفقًا لذلك. يرجى استخدام [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/) لتحديد أو إلغاء تحديد عناصر المقطع باستخدام Aspose.Cells ثم استدعاء طريقة [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) لتحديث جدول المقطع أو جدول Pivot.

## **كيفية تحديث العارض**

يحمل الكود العيني التالي الملف اكسل العيني الذي يحتوي على عارض موجود. يلغي تحديد العناصر الثانية والثالثة من العارض ويحدث العارض. ثم يحفظ الدفتر كملف أكسل بإسم ملف الأكسل العيني الناتج. تظهر الصورة العينية التالية تأثير الكود العيني على ملف الأكسل العيني العيني. كما ترون في الصورة العينية، تم تحديث العارض بالعناصر المحددة وكذلك تم تحديث الجدول المحوري وفقًا لذلك.

![todo:image_alt_text](updating-slicer_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
