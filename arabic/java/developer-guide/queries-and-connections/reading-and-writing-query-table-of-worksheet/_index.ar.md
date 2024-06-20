---
title: قراءة وكتابة جدول الاستعلام لورقة العمل
type: docs
weight: 560
url: /ar/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells مجموعة [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) التي تُرجع مجموعة [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection). للحصول على [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) محدد، استخدم خاصية [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\)) وقم بتمرير مؤشر الQueryTable. تحتوي فئة [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) على الخاصيتين التاليتين لضبط جدول الاستعلام.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

هذه قيمان منطقيتان. يمكنك مشاهدتهما في Microsoft Excel عبر الطريقة البيانات > الاتصالات > الخصائص.

{{% /alert %}} 
## **قراءة وكتابة جدول الاستعلام في ورقة العمل**
يقرأ الكود التالي [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) الأول في الورقة العمل الأولى ثم يطبع خاصيتي [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) كلاهما. ثم يضبط [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) على **صحيح**.

تُظهر الصورة المقتطفة التالية [ملف إكسل المصدري](5472578.xlsx) المستخدم في الكود وخصائصه التي تُظهر قيم كلا من [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable).

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

تُظهر الصورة المقتطفة التالية [ملف إكسل المولد](5472574.xlsx) الذي تم إنشاؤه بواسطة الكود وخصائصه التي تُظهر قيم كلا من [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). كما يمكنك رؤية خانة اختيار الحفظ بتنسيقها مفعلة الآن.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **مخرجات الوحدة**
إليك إخراج الكونسول للكود العيني أعلاه

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **استرجاع نطاق نتيجة جدول الاستعلام**
تقدم Aspose.Cells الخيار لقراءة العنوان أي نطاق النتائج لخلايا جدول الاستعلام. يوضح الكود التالي هذه الميزة عن طريق قراءة عنوان نطاق نتيجة جدول الاستعلام. يمكن تنزيل الملف المثالي [هنا](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
