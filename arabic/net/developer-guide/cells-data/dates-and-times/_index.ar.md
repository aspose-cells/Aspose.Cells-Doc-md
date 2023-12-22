---
title: كيفية إدارة التواريخ والأوقات
type: docs
weight: 600
url: /ar/net/how-to-manage-dates-and-times/
description: تعرف على كيفية إدارة التواريخ والأوقات من خلال Aspose.Cells for .NET API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **كيفية تخزين التواريخ والأوقات في إكسيل**
يتم تخزين التواريخ والأوقات في الخلايا كأرقام. وبالتالي، فإن قيم الخلايا التي تحتوي على التواريخ والأوقات تكون من النوع الرقمي. يتكون الرقم الذي يحدد التاريخ والوقت من مكونات التاريخ (جزء صحيح) والوقت (جزء كسري). الخاصية Cell.DoubleValue ترجع هذا الرقم.

##  **كيفية عرض التاريخ والأوقات في Aspose.Cells**
لعرض رقم كتاريخ ووقت، قم بتطبيق تنسيق التاريخ والوقت المطلوب على خلية عبر[رقم الطراز](https://reference.aspose.com/cells/net/aspose.cells/style/number/) أو[مخصص]() ملكية. تقوم الخاصية CellValue.DateTimeValue بإرجاع كائن DateTime، الذي يحدد التاريخ والوقت الذي يمثله الرقم الموجود في الخلية.
<br>
<image src="1.png" width="70%" />

##  **كيفية تبديل نظامين للتاريخ في Aspose.Cells**
يقوم MS-Excel بتخزين التواريخ كأرقام تسمى القيم التسلسلية. القيمة التسلسلية هي عدد صحيح يمثل عدد الأيام المنقضية من اليوم الأول في نظام التاريخ. يدعم Excel أنظمة التاريخ التالية للقيم التسلسلية:

1. نظام التاريخ 1900 التاريخ الأول هو 1 يناير 1900، وقيمته التسلسلية هي 1. وآخر تاريخ هو 31 ديسمبر 9999، وقيمته التسلسلية 2,958,465. يتم استخدام نظام التاريخ هذا في المصنف بشكل افتراضي.
1.  نظام التاريخ 1904 التاريخ الأول هو 1 يناير 1904، وقيمته التسلسلية هي 0. وآخر تاريخ هو 31 ديسمبر 9999، وقيمته التسلسلية 2,957,003. لاستخدام نظام التاريخ هذا في المصنف، قم بتعيين[المصنف.الإعدادات.التاريخ1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) الملكية إلى صحيح.


يوضح هذا المثال أن القيم التسلسلية المخزنة في نفس التاريخ في أنظمة تاريخ مختلفة مختلفة.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
نتيجة الإخراج:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **كيفية تعيين قيمة التاريخ والوقت في Aspose.Cells**
يقوم هذا المثال بتعيين قيمة DateTime في الخلية A1 وA2، وتعيين التنسيق المخصص لـ A1 وتنسيق الأرقام لـ A2، ثم إخراج أنواع القيم.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

نتيجة الإخراج:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **كيفية الحصول على قيمة DateTime في Aspose.Cells**
يقوم هذا المثال بتعيين قيمة DateTime في الخلية A1 وA2، وتعيين التنسيق المخصص لـ A1 وتنسيق الأرقام لـ A2، والتحقق من أنواع القيم لخليتين، ثم إخراج قيمة DateTime والسلسلة المنسقة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

نتيجة الإخراج:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
