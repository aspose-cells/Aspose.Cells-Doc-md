---
title: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs
weight: 190
url: /ar/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **سيناريوهات الاستخدام المحتملة**
يسمح Microsoft Excel بتطبيق *تصفية* متقدمة على بيانات ورق العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق مرشح متقدم مع Microsoft Excel عبر أمره *بيانات> متقدم* كما هو موضح في هذه اللقطة الشاشية.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

يسمح Aspose.Cells أيضًا بتطبيق المرشح المتقدم باستخدام الطريقة [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)). تمامًا مثل Microsoft Excel، يقبل التعامل مع المعلمات التالية.

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
تطبيق تصفية متقدمة على [ملف إكسل عينة](48496702.xlsx) وإنشاء [ملف الإكسل الناتج](48496705.xlsx)، الشاشة تظهر كلا الملفين للمقارنة. كما يمكنك رؤية داخل الصورة، البيانات تم تصفيتها داخل ملف الإكسل الناتج بحسب معايير معقدة.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
