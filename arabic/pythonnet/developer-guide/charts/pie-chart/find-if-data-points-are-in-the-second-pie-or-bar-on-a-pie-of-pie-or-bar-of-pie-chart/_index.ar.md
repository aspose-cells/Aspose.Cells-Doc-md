---
title: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني
description: تعلم كيفية استخدام Aspose.Cells لبایتون via .NET لمعرفة ما إذا كانت نقاط البيانات في الدائري الثاني أو الشريط في مخطط دائري من نوع pie of pie أو bar of pie. ستوضح دليلنا كيفية التعرف على والوصول إلى الدائري أو الشريط الثانوي في مخطط مركب، مما يسمح لك بتحليل البيانات والتعامل معها بفعالية.
keywords: Aspose.Cells لبایتون via .NET، مخطط Pie of Pie، مخطط Bar of Pie، الدائري الثانوي، الشريط الثانوي، تحليل البيانات، معالجة البيانات.
type: docs
weight: 180
url: /ar/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك معرفة ما إذا كانت نقاط البيانات لمجموعة معينة في الدائري الثاني على مخطط *Pie of Pie* أو في الشريط على مخطط *Bar of Pie* باستخدام Aspose.Cells لبایتون via .NET. يرجى استخدام الخاصية [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) لتحديد ذلك.

يرجى تنزيل [ملف إكسل نموذجي](5115193.xlsx) المستخدم في رمز العينة أدناه ورؤية الإخراج من وحدة التحكم الخاصة به. إذا فتحت [ملف إكسل العيني](5115193.xlsx)، ستجد، أن جميع نقاط البيانات التي تقل عن 10 داخل الشريط *شريطي* على رسم بياني من الدائرة الدائرية كما يظهر أيضًا في إخراج وحدة التحكم.

## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**
يوضح الكود المثالي التالي كيفية العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **مخرجات الوحدة**
يرجى مراجعة المخرجات في وحدة التحكم الناتجة بعد تنفيذ الكود النموذجي أعلاه باستخدام ملف إكسل العيني [الملف العيني](5115193.xlsx). إذا كانت [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) **خاطئة**، فإن نقطة البيانات داخل الدائري، وإذا كانت **صحيحة**، فداخل الشريط.



{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
