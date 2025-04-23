---
title: إزالة مقطع التصفح باستخدام C++
linktitle: إزالة قالب التصفية
type: docs
weight: 30
url: /ar/cpp/removing-slicer/
description: تعلم كيفية إزالة مقاطع التصفح في ملفات Excel برمجياً باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تريد إزالة مقطع تصفح في Microsoft Excel، فقط حدده واضغط على زر *حذف*. بالمثل، إذا كنت تريد إزالته باستخدام واجهة برمجة التطبيقات Aspose.Cells برمجياً، يرجى استخدام الطريقة [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/). ستقوم بذلك بإزالة مقطع التصفح من ورقة العمل.

## **إزالة قالب التصفية**

الكود العينة التالي يحمل [ملف إكسل عينة](67338478.xlsx) الذي يحتوي على قالب تصفية موجود. يدخل إلى قوالب التصفية ثم يقوم بإزالتها. وأخيراً، يحفظ الدفتر ك [ملف إكسل الناتج](67338477.xlsx). اللقطة الشاشة التالية توضح قالب التصفية الذي سيتم إزالته بعد تنفيذ الكود العينة.

![todo:image_alt_text](removing-slicer_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
