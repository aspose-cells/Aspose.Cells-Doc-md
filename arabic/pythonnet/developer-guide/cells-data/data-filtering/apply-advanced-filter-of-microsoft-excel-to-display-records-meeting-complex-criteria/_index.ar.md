---
title: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs
weight: 280
url: /ar/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: تعلم كيفية تطبيق تصفية متقدمة لمايكروسوفت إكسل لعرض السجلات التي تلتقي بالمعايير المعقدة باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Excel الخاصة بـ Python، تطبيق تصفية متقدمة باستخدام Python، تعيين تصفية متقدمة بواسطة Python، إضافة تصفية متقدمة بواسطة Python، إنشاء تصفية متقدمة بواسطة Python، كيفية إضافة تصفية متقدمة إلى نطاق باستخدام Python.
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Microsoft Excel بتطبيق *تصفية* متقدمة على بيانات ورق العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق مرشح متقدم مع Microsoft Excel عبر أمره *بيانات> متقدم* كما هو موضح في هذه اللقطة الشاشية.

![todo:image_alt_text](1.png)

تسمح Aspose.Cells for Python via .NET أيضًا لك بتطبيق التصفية المتقدمة باستخدام الطريقة [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool). تمامًا مثل Microsoft Excel، فإنه يقبل المعلمات التالية.

**isFilter**

يشير ما إذا كان يتم تصفية القائمة في المكان.

**listRange**

نطاق القائمة.

**criteriaRange**

نطاق المعيار.

**copyTo**

نطاق نسخ البيانات إليه.

**uniqueRecordOnly**

عرض أو نسخ الصفوف الفريدة فقط.

## **تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة**

الكود العيني التالي يطبق عامل التصفية المتقدم على [ملف إكسل عيني](48496692.xlsx) ويولد [ملف إكسل الناتج](48496691.xlsx). يظهر لقطات الشاشة كلا الملفين للمقارنة. كما يمكن رؤية داخل صورة الشاشة أن البيانات تم تصفيتها داخل ملف إكسل الناتج وفقًا لمعايير معقدة.

![todo:image_alt_text](2.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
