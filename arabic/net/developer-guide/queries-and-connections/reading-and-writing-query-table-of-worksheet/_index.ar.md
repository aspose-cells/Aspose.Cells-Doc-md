---
title: قراءة وكتابة جدول الاستعلام الخاص بورقة العمل
type: docs
weight: 40
url: /ar/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

يوفر Aspose.Cells مجموعة Worksheet.QueryTables التي تقوم بإرجاع كائن من نوع QueryTable بواسطة الفهرس. لديها الخاصيتين التاليتين

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

كلاهما قيم منطقية. يمكنك عرضها في Microsoft Excel عبر البيانات> الاتصالات> الخصائص.

{{% /alert %}}

## قراءة وكتابة جدول الاستعلام الخاص بورقة العمل

يقرأ نموذج التعليمات البرمجية التالي جدول الاستعلام الأول لورقة العمل الأولى ثم يقوم بطباعة كل من خصائص جدول الاستعلام. ثم يقوم بتعيين QueryTable.PreserveFormatting إلى true.

يمكنك تنزيل ملف Excel المصدر المستخدم في هذا الرمز وملف Excel الناتج الذي تم إنشاؤه بواسطة الكود من الروابط التالية.

- [مصدر ملف Excel](5115533.xlsx)
- [إخراج ملف Excel](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### إخراج وحدة التحكم

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## استرداد نطاق نتائج جدول الاستعلام

 يوفر Aspose.Cells خيارًا لقراءة العنوان ، على سبيل المثال ، نطاق نتائج خلايا لجدول استعلام. يوضح الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول الاستعلام. يمكن تنزيل ملف عينة[هنا](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
