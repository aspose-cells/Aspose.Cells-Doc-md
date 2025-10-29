---
title: تطبيق فلتر متقدم في مايكروسوفت إكسل لعرض السجلات التي تلبي معايير معقدة باستخدام جولانج عبر C++
linktitle: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs
weight: 280
url: /ar/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: تعلم كيفية تطبيق التصفية المتقدمة لMicrosoft Excel لعرض السجلات التي تلبي معايير معقدة باستخدام API رقم Aspose.Cells for C++.
keywords: تطبيق عامل تصفية متقدم، تعيين عامل تصفية متقدم، إضافة عامل تصفية متقدم، إنشاء عامل تصفية متقدم، كيفية إضافة عامل تصفية متقدم إلى نطاق
---

## **سيناريوهات الاستخدام المحتملة**

يسمح لك Microsoft Excel بتطبيق *التصفية المتقدمة* على بيانات ورقة العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق التصفية المتقدمة باستخدام أمر *البيانات > متقدمة* كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

كما يسمح Aspose.Cells بتطبيق التصفية المتقدمة باستخدام طريقة [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/). تمامًا مثل Microsoft Excel، يقبل المعلمات التالية.

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

الكود النموذجي التالي يطبق التصفية المتقدمة على ملف Excel [ملف Excel النموذجي](48496692.xlsx) ويولد ملف [ملف إخراج Excel](48496691.xlsx). تُظهر لقطة الشاشة كلا الملفين للمقارنة. كما ترى في لقطة الشاشة، تم تصفية البيانات داخل ملف الإخراج وفقًا لمعايير معقدة.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
