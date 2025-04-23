---
title: كيفية إدارة التواريخ والأوقات
type: docs
weight: 600
url: /ar/net/how-to-manage-dates-and-times/
description: تعلم كيفية إدارة التواريخ والأوقات من خلال واجهة برمجة تطبيقات Aspose.Cells for .NET.
keywords: كيفية إدارة التواريخ والأوقات، نظام التاريخ 1900، نظام التاريخ 1904، ضبط التواريخ والأوقات، الحصول على التواريخ والأوقات، إدارة التواريخ والأوقات، تخزين التواريخ والأوقات في إكسل، عرض التواريخ والأوقات في الخلايا.
---

## **كيفية تخزين التواريخ والأوقات في إكسل**
يتم تخزين التواريخ والأوقات في الخلايا على أنها أرقام. وبالتالي، قيم الخلايا التي تحتوي على تواريخ وأوقات تكون من نوع رقمي. الرقم الذي يحدد تاريخًا ووقتًا يتكون من مكونات التاريخ (الجزء الصحيح) والوقت (الجزء الكسري). يُرجع خاصية Cell.DoubleValue هذا الرقم.

## **كيفية عرض التواريخ والأوقات في Aspose.Cells**
لعرض رقم كتاريخ ووقت، قم بتطبيق تنسيق التاريخ والوقت المطلوب على الخلية عبر الخاصية [Style.Number](https://reference.aspose.com/cells/net/aspose.cells/style/number/) أو [Style.Custom]() . تُرجع الخاصية CellValue.DateTimeValue كائن DateTime الذي يحدد التاريخ والوقت الذي يتمثل به الرقم الذي يحتويه الخلية.
<br>
<image src="1.png" width="70%" />

## **كيفية التبديل بين نظامي التواريخ في Aspose.Cells**
تخزن برنامج MS-Excel التواريخ كأرقام تسمى قيم متسلسلة. قيمة متسلسلة هي عدد صحيح هو عدد الأيام المنقضية من اليوم الأول في نظام التاريخ. يدعم Excel الأنظمة التالية للقيم المتسلسلة للتواريخ: 

1. نظام التاريخ 1900. اليوم الأول هو 1 يناير 1900، وقيمته المتسلسلة هي 1. أما آخر يوم فهو 31 ديسمبر 9999، وقيمته المتسلسلة هي 2،958،465. يُستخدم هذا النظام في جدول العمل افتراضيًا.
1. نظام التاريخ 1904. اليوم الأول هو 1 يناير 1904، وقيمته المتسلسلة هي 0. أما آخر يوم فهو 31 ديسمبر 9999، وقيمته المتسلسلة هي 2،957،003. لاستخدام هذا النظام في جدول العمل، قم بضبط الخاصية [Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) إلى true.


تُظهر هذا المثال أن القيم المتسلسلة المخزنة في نفس التاريخ في أنظمة تاريخ مختلفة هي مختلفة.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
النتيجة المخرجة:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **كيفية تعيين قيمة تاريخ ووقت في Aspose.Cells**
يُعين هذا المثال قيمة DateTime في الخلية A1 و A2، يضبط تنسيق مخصص ل A1 وتنسيق رقمي ل A2، ثم يخرج أنواع القيمة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

النتيجة المخرجة:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **كيفية الحصول على قيمة تاريخ ووقت في Aspose.Cells**
يُعين هذا المثال قيمة DateTime في الخلية A1 و A2، يضبط تنسيق مخصص ل A1 وتنسيق رقمي ل A2، يتحقق من أنواع القيمة في الخليتين، ثم يخرج قيمة DateTime وسلسلة مُنسَقة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

النتيجة المخرجة:
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
{{< app/cells/assistant language="csharp" >}}
