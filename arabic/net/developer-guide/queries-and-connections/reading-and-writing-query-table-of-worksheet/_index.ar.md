---
title: قراءة وكتابة جدول الاستعلام لورقة العمل
type: docs
weight: 40
url: /ar/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

توفر Aspose.Cells مجموعة Worksheet.QueryTables التي تعيد كائن نوع QueryTable عن طريق الفهرس. لديها الخاصيةان التالية

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

هذه قيم بوليانيتين. يمكنك مشاهدتها في Microsoft Excel عبر Data > Connections > Properties.

{{% /alert %}}

## قراءة وكتابة جدول الاستعلام لورقة العمل

الكود العيني التالي يقرأ أول جدول استعلام في الورقة العمل الأولى ثم يطبع كل من خصائص جدول الاستعلام. ثم يضبط QueryTable.PreserveFormatting ليكون صحيحًا.

يمكنك تحميل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج الذي تم إنشاؤه بواسطة الكود من الروابط التالية.

- [ملف Excel المصدر](5115533.xlsx)
- [ملف Excel الناتج](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### إخراج الكونسول

إليك إخراج الكونسول للكود العيني أعلاه

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## استرداد نطاق نتيجة جدول الاستعلام

توفر Aspose.Cells خيار قراءة العنوان أي نطاق نتائج الخلايا لجدول الاستعلام. يُظهر الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول الاستعلام. يمكن تنزيل الملف النموذجي من [هنا](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
