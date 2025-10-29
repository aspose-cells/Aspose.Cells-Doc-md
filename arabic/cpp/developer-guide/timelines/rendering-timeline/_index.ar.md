---
title: تصيير الجدول الزمني باستخدام C++
type: docs
weight: 40
url: /ar/cpp/rendering-timeline/
description: إدارة الجداول الزمنية لملفات Excel باستخدام Aspose.Cells مع C++.
keywords: تحويل الجدول الزمني بدون Office 2013، Office 2016، Office 2019 وOffice 365
---

## **سيناريوهات الاستخدام المحتملة**
تدعم Aspose.Cells تقديم شكل الجدول الزمني دون استخدام Office 2013 أو Office 2016 أو Office 2019 أو Office 365. إذا قمت بتحويل ورقة العمل الخاصة بك إلى صورة أو حفظ سجل العمل الخاص بك إلى تنسيقات PDF أو HTML ، فسترى أن الجداول الزمنية تتم عرضها بشكل صحيح.

## **تقديم الجدول الزمني**
يقوم الكود العيني التالي بتحميل ملف Excel عيّني يحتوي على جدول زمني موجود. احصل على كائن الشكل وفقًا لاسم الجدول الزمني ، ثم قم بتقديمه إلى صورة من خلال طريقة Shape.ToImage(). الصورة الناتجة هي الصورة الناتجة التي تظهر الجدول الزمني المقدم. كما يمكنك أن ترى ، تم عرض الجدول الزمني بشكل صحيح ويبدو نفسه كما في ملف Excel العيني.

![todo:image_alt_text](out.png)
### **الكود المثالي**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
