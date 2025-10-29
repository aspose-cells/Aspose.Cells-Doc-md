---
title: كيفية إدارة التواريخ والأوقات
type: docs
weight: 600
url: /ar/python-net/how-to-manage-dates-and-times/
description: تعلم كيف يمكنك إدارة التواريخ والأوقات من خلال API الخاص بـ Aspose.Cells لبايثون via .NET.
keywords: كيفية إدارة التواريخ والأوقات، نظام التاريخ 1900، نظام التاريخ 1904، ضبط التواريخ والأوقات، الحصول على التواريخ والأوقات، إدارة التواريخ والأوقات، تخزين التواريخ والأوقات في إكسل، عرض التواريخ والأوقات في الخلايا.
---

## **كيفية تخزين التواريخ والأوقات في إكسل**
يتم تخزين التواريخ والأوقات في الخلايا على أنها أرقام. وبالتالي، قيم الخلايا التي تحتوي على تواريخ وأوقات تكون من نوع رقمي. الرقم الذي يحدد تاريخًا ووقتًا يتكون من مكونات التاريخ (الجزء الصحيح) والوقت (الجزء الكسري). يُرجع خاصية Cell.DoubleValue هذا الرقم.

## **كيفية عرض التواريخ والأوقات في Aspose.Cells**
لعرض رقم كتاريخ ووقت، طبق تنسيق التاريخ والوقت المطلوب على خلية عبر خاصية [Style.number](https://reference.aspose.com/cells/python-net/aspose.cells/style/number/) أو [Style.Custom]() . تعيد خاصية CellValue.DateTimeValue كائن DateTime، الذي يحدد التاريخ والوقت الممثلين بواسطة الرقم الموجود في الخلية.
<br>
<image src="1.png" width="70%" />

## **كيفية التبديل بين نظامي التواريخ في Aspose.Cells**
تخزن برنامج MS-Excel التواريخ كأرقام تسمى قيم متسلسلة. قيمة متسلسلة هي عدد صحيح هو عدد الأيام المنقضية من اليوم الأول في نظام التاريخ. يدعم Excel الأنظمة التالية للقيم المتسلسلة للتواريخ: 

1. نظام التاريخ 1900. اليوم الأول هو 1 يناير 1900، وقيمته المتسلسلة هي 1. أما آخر يوم فهو 31 ديسمبر 9999، وقيمته المتسلسلة هي 2،958،465. يُستخدم هذا النظام في جدول العمل افتراضيًا.
1. نظام التاريخ 1904. التاريخ الأول هو 1 يناير 1904، وقيمته التسلسلية هي 0. التاريخ الأخير هو 31 ديسمبر 9999، وقيمته التسلسلية هي 2،957،003. لاستخدام هذا النظام في دفتر العمل، قم بتعيين خاصية [**Workbook.settings.date1904**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/date1904/) إلى true.


تُظهر هذا المثال أن القيم المتسلسلة المخزنة في نفس التاريخ في أنظمة تاريخ مختلفة هي مختلفة.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Datetime-1904.py" >}}
النتيجة المخرجة:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **كيفية تعيين قيمة تاريخ ووقت في Aspose.Cells**
يُعين هذا المثال قيمة DateTime في الخلية A1 و A2، يضبط تنسيق مخصص ل A1 وتنسيق رقمي ل A2، ثم يخرج أنواع القيمة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Set-Datetime.py" >}}

النتيجة المخرجة:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **كيفية الحصول على قيمة تاريخ ووقت في Aspose.Cells**
يُعين هذا المثال قيمة DateTime في الخلية A1 و A2، يضبط تنسيق مخصص ل A1 وتنسيق رقمي ل A2، يتحقق من أنواع القيمة في الخليتين، ثم يخرج قيمة DateTime وسلسلة مُنسَقة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Get-Datetime.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
