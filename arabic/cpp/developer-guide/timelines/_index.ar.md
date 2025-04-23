---
title: إدراج Timeline باستخدام C++
linktitle: الجداول الزمنية
type: docs
weight: 170
url: /ar/cpp/create-timeline/
description: تعلم كيفية إنشاء مخطط زمني باستخدام Aspose.Cells باستخدام C++.
---

## **سيناريوهات الاستخدام المحتملة**

بدلاً من ضبط المرشحات لعرض التواريخ، يمكنك استخدام مخطط جدول محوري——خيار مرشح ديناميكي يتيح لك تصفية بسهولة حسب التاريخ/الوقت، والتكبير على الفترة التي تريدها باستخدام عنصر تحكم شريط التمرير. يسمح لك Microsoft Excel بإنشاء مخطط زمني عبر اختيار جدول محوري ثم النقر على *إدراج > مخطط زمني*. كما يتيح Aspose.Cells إنشاء مخطط زمني باستخدام [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/) الطريقة.

## **إنشاء الجدول الزمني لجدول البيفوت**

يرجى الاطلاع على رمز العينة التالي. يقوم بتحميل [ملف إكسل عيني](input.xlsx) الذي يحتوي على الجدول الدينامي. ثم ينشئ الجدول الزمني بناءً على أول حقل قاعدة لجدول البيفوت. وأخيرًا، يحفظ المصنف بتنسيق [XLSX](output.xlsx). تُظهر اللقطة الشاشية التالية الجدول الزمني الذي تم إنشاؤه بواسطة Aspose.Cells في ملف الإكسيل الناتج.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
