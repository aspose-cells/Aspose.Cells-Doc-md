---
title: تطبيق عامل التصفية المتقدم لـ Microsoft Excel لعرض السجلات التي تفي بالمعايير المعقدة
type: docs
weight: 190
url: /ar/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **سيناريوهات الاستخدام الممكنة**
 Microsoft يسمح لك Excel بالتقديم*تصفية متقدم* في بيانات ورقة العمل لعرض السجلات التي تفي بالمعايير المعقدة. يمكنك تطبيق مرشح متقدم مع Microsoft Excel من خلال*البيانات> متقدم*الأمر كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

يسمح لك Aspose.Cells أيضًا بتطبيق المرشح المتقدم باستخدام[Worksheet.advancedFilter ()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) طريقة. تمامًا مثل Microsoft Excel ، فإنه يقبل المعلمات التالية.

**isFilter**

يشير إلى ما إذا كانت تصفية القائمة في مكانها.

**قائمة**

نطاق القائمة.

**وتتراوح المعايير**

نطاق المعايير.

**نسخ الى**

النطاق الذي يتم فيه نسخ البيانات.

**فريد التسجيل فقط**

عرض أو نسخ الصفوف الفريدة فقط.
## **تطبيق عامل التصفية المتقدم لـ Microsoft Excel لعرض السجلات التي تفي بالمعايير المعقدة**
يطبق نموذج التعليمات البرمجية التالي عامل التصفية المتقدم على ملف[نموذج لملف Excel](48496702.xlsx) ويولد ال[إخراج ملف Excel](48496705.xlsx). تظهر لقطة الشاشة كلا الملفين للمقارنة. كما ترى داخل لقطة الشاشة ، تمت تصفية البيانات داخل ملف Excel الناتج وفقًا لمعايير معقدة.

![ما يجب القيام به: image_بديل_نص](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
