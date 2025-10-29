---
title: إدراج الجدول الزمني مع Golang عبر C++
linktitle: الجداول الزمنية
type: docs
weight: 170
url: /ar/go-cpp/create-timeline/
description: تعلم كيفية إنشاء مخطط زمني باستخدام Aspose.Cells باستخدام C++.
---

## **سيناريوهات الاستخدام المحتملة**

بدلاً من ضبط المرشحات لعرض التواريخ، يمكنك استخدام مخطط جدول محوري——خيار مرشح ديناميكي يتيح لك تصفية بسهولة حسب التاريخ/الوقت، والتكبير على الفترة التي تريدها باستخدام عنصر تحكم شريط التمرير. يسمح لك Microsoft Excel بإنشاء مخطط زمني عبر اختيار جدول محوري ثم النقر على *إدراج > مخطط زمني*. كما يتيح Aspose.Cells إنشاء مخطط زمني باستخدام [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/) الطريقة.

## **إنشاء الجدول الزمني لجدول البيفوت**

يرجى الاطلاع على رمز العينة التالي. يقوم بتحميل [ملف إكسل عيني](input.xlsx) الذي يحتوي على الجدول الدينامي. ثم ينشئ الجدول الزمني بناءً على أول حقل قاعدة لجدول البيفوت. وأخيرًا، يحفظ المصنف بتنسيق [XLSX](output.xlsx). تُظهر اللقطة الشاشية التالية الجدول الزمني الذي تم إنشاؤه بواسطة Aspose.Cells في ملف الإكسيل الناتج.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
