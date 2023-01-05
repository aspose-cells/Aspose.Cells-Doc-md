---
title: قراءة وكتابة جدول الاستعلام الخاص بورقة العمل
type: docs
weight: 560
url: /ar/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 يوفر Aspose.Cells[Worksheet.getQueryTables ()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) المجموعة التي تعيد[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . للحصول على ملف[الاستعلام](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) ، استخدم ال[QueryTableCollection.get ()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) وتمرير فهرس QueryTable. ال[الاستعلام](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) تحتوي الفئة على الخاصيتين التاليتين لضبط جدول الاستعلام.

- [QueryTable.getAdjustColumnWidth ()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting ()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

كلاهما قيم منطقية. يمكنك عرضها في Microsoft Excel عبر البيانات> الاتصالات> الخصائص.

{{% /alert %}} 
## **قراءة وكتابة جدول الاستعلام الخاص بورقة العمل**
 يقرأ نموذج التعليمات البرمجية التالي الأول[الاستعلام](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) من ورقة العمل الأولى ثم طباعة ملف[الاستعلام](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) الخصائص. ثم يقوم بتعيين ملف[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) إلى**حقيقي**.

تُظهر لقطة الشاشة التالية ملف[ملف اكسل المصدر](5472578.xlsx) المستخدمة في الكود وخصائصه تظهر كلا من[الاستعلام](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)القيم.

![ما يجب القيام به: image_بديل_نص](reading-and-writing-query-table-of-worksheet_1.png)

تُظهر لقطة الشاشة التالية ملف[ملف اكسل الناتج](5472574.xlsx) التي تم إنشاؤها بواسطة الكود وخصائصه التي تظهر كلا من[الاستعلام](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)القيم. كما ترى ، تم تحديد خانة الاختيار الاحتفاظ بالتنسيق الآن.

![ما يجب القيام به: image_بديل_نص](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **إخراج وحدة التحكم**
هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **استرداد نطاق نتائج جدول الاستعلام**
يوفر Aspose.Cells خيار قراءة العنوان ، على سبيل المثال ، نطاق نتائج خلايا لجدول استعلام. يوضح الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول الاستعلام. يمكن تنزيل ملف العينة[هنا](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
