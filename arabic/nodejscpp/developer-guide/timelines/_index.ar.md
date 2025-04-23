---
title: إدراج الجدول الزمني
linktitle: الجداول الزمنية
type: docs
weight: 170
url: /ar/nodejs-cpp/create-timeline/
description: تعلم كيفية إنشاء جدول زمني باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

بدلاً من تعديل الفلاتر لعرض التواريخ، يمكنك استخدام جدول زمني ضمن PivotTable——خيار تصفية ديناميكي يتيح لك تصفية بسهولة حسب التاريخ/الوقت، والتكبير على الفترة التي تريدها باستخدام عنصر التحكم sli. يتيح لك Microsoft Excel إنشاء جدول زمني عن طريق اختيار جدول محوري ثم النقر على *إدراج > جدول زمني*. Aspose.Cells for Node.js via C++ يتيح أيضًا إنشاء جدول زمني باستخدام طريقة [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **إنشاء الجدول الزمني لجدول البيفوت**

يرجى الاطلاع على الكود التجريبي التالي. يقوم بتحميل ملف إكسل النموذجي الذي يحتوي على الجدول المحوري. ثم ينشئ الجدول الزمني بناءً على أول حقل جدول محوري أساسي. وأخيرًا، يحفظ المصنف بتنسيق [XLSX المخرجة](output.xlsx). تظهر لقطة الشاشة التالية الجدول الزمني الذي أنشأه Aspose.Cells for Node.js via C++ في ملف إكسل الناتج.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

