---
title: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs
weight: 280
url: /ar/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: تعلم كيفية تطبيق عامل تصفية متقدم من Microsoft Excel لعرض السجلات التي تلبي معايير معقدة باستخدام API Aspose.Cells for .NET.
keywords: تطبيق عامل تصفية متقدم، تعيين عامل تصفية متقدم، إضافة عامل تصفية متقدم، إنشاء عامل تصفية متقدم، كيفية إضافة عامل تصفية متقدم إلى نطاق 
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Microsoft Excel بتطبيق *تصفية* متقدمة على بيانات ورق العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق مرشح متقدم مع Microsoft Excel عبر أمره *بيانات> متقدم* كما هو موضح في هذه اللقطة الشاشية.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

تسمح Aspose.Cells أيضًا لك بتطبيق العامل تصفية المتقدم باستخدام الطريقة [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter). تمامًا مثل Microsoft Excel، يقبل البارامترات التالية.

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

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
