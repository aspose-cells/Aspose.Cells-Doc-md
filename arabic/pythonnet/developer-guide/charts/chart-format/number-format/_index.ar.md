---
title: تعيين كود تنسيق القيم لسلسلة الرسم البياني
description: تعلم كيفية تعيين رمز التنسيق للقيم في سلسلة الرسم البياني في Aspose.Cells لبايثون via .NET. سيساعدك دليلنا على فهم كيفية تنسيق بيانات سلسلة الرسم البياني باستخدام رمز التنسيق المناسب، لعرض بياناتك بدقة واحترافية.
keywords: Aspose.Cells لبايثون via .NET، سلسلة الرسم البياني، رمز تنسيق القيم، التنسيق، عرض البيانات، الدقة، الاحترافية.
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/python-net/set-the-values-format-code-of-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك تعيين رمز تنسيق القيم في سلسلة الرسم البياني باستخدام خاصية [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code). ليست هذه الخاصية مفيدة فقط للسلاسل القائمة على النطاق داخل ورقة العمل، بل تعمل بشكل جيد أيضًا للسلاسل التي تم إنشاؤها باستخدام مصفوفة من القيم.

## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
 يضيف الكود التالي سلسلة في رسم بياني فارغ لم يكن لديه سلاسل من قبل. يضاف السلسلة باستخدام مصفوفة القيم. بعد إضافة السلسلة، يتم تنسيقها برمز $#,##0 باستخدام خاصية [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code) وتحول الرقم 10000 إلى $10,000. تُظهر لقطة الشاشة تأثير الكود على ملف إكسل عينة (51740712.xlsx) وملف إكسل الناتج (51740713.xlsx) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **الكود المثالي**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
{{< app/cells/assistant language="python-net" >}}
