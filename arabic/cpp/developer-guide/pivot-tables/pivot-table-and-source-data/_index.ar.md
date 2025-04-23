---
title: جدول Pivot والبيانات المصدرية باستخدام C++
linktitle: جدول محوري وبيانات المصدر
type: docs
weight: 30
url: /ar/cpp/pivot-table-and-source-data/
description: تعلم كيفية تغيير مصدر البيانات للجدول المحوري ديناميكيًا باستخدام Aspose.Cells مع C++.
---

## **بيانات المصدر للجدول المحوري**

هناك أوقات عندما ترغب في إنشاء تقارير Microsoft Excel باستخدام جداول محورية تأخذ البيانات من مصادر بيانات مختلفة (مثل قاعدة بيانات) غير معروفة في وقت التصميم. يوفر هذا المقال نهجًا لتغيير بيانات مصدر الجدول المحوري بشكل ديناميكي.

### **تغيير مصدر بيانات الجدول المحوري**

1. إنشاء قالب مصمم جديد.
   1. إنشاء ملف قالب مصمم جديد كما في لقطة الشاشة أدناه.
   1. ثم تعريف نطاق مسمى، **DataSource**، الذي يشير إلى هذا النطاق من الخلايا.

      **إنشاء قالب مصمم وتعريف نطاق مسمى، DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. إنشاء جدول محوري بناءً على هذا النطاق المسمى.
   1. في Microsoft Excel ، اختر ** البيانات **، ثم ** جدول البيانات المحوري ** و ** تقرير PivotChart **.
   1. إنشاء جدول محوري استنادًا إلى المجموعة المسماة التي تم إنشاؤها في الخطوة الأولى.

      ** إنشاء جدول محوري استنادًا إلى المجموعة المسماة ، مصدر البيانات ** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. اسحب الحقل المقابل إلى صف جدول البيانات المحوري والعمود ، ثم قم بإنشاء جدول البيانات المحوري الناتج كما في اللقطة أدناه.

   ** إنشاء جدول محوري استنادًا إلى حقل مقابل ** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. انقر بزر الماوس الأيمن على الجدول المحوري وحدد **خيارات الجدول**.
   1. تحقق من ** التحديث عند الفتح ** في إعدادات ** خيارات البيانات **.

      ** ضبط خيارات جدول البيانات المحوري ** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


الآن ، يمكنك حفظ هذا الملف باسم ملف القالب الخاص بالمصمم.

1. ملء البيانات الجديدة وتغيير بيانات مصدر جدول البيانات المحوري.
   1. بمجرد إنشاء قالب المصمم ، استخدم الكود التالي لتغيير بيانات مصدر جدول البيانات المحوري.

تنفيذ الكود المثالي أدناه يغير بيانات مصدر الجدول المحوري.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
