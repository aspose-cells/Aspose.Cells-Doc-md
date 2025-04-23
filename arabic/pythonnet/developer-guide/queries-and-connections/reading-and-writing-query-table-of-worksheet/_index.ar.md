---
title: قراءة وكتابة جدول الاستعلام لورقة العمل
type: docs
weight: 40
url: /ar/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells لـ Python via .NET مجموعة Worksheet.QueryTables والتي تعيد كائن من نوع QueryTable حسب الفهرس. لديها الخاصيتان التاليتان

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

هذه قيم بوليانيتين. يمكنك مشاهدتها في Microsoft Excel عبر Data > Connections > Properties.

{{% /alert %}}

## قراءة وكتابة جدول الاستعلام لورقة العمل

الكود العيني التالي يقرأ أول جدول استعلام في الورقة العمل الأولى ثم يطبع كل من خصائص جدول الاستعلام. ثم يضبط QueryTable.PreserveFormatting ليكون صحيحًا.

يمكنك تحميل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج الذي تم إنشاؤه بواسطة الكود من الروابط التالية.

- [ملف Excel المصدر](5115533.xlsx)
- [ملف Excel الناتج](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### إخراج الكونسول

إليك إخراج الكونسول للكود العيني أعلاه

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## استرداد نطاق نتيجة جدول الاستعلام

يوفر Aspose.Cells لـ Python via .NET خيار قراءة العنوان، أي نطاق نتائج الخلايا لجدول الاستعلام. يوضح الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول استعلام. يمكن تنزيل الملف النموذجي من [هنا](72417290.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

