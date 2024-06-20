---
title: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني
description: تعلم كيفية استخدام Aspose.Cells for .NET لمعرفة ما إذا كانت نقاط البيانات في الدائرة الدائرية الثانية أو الشريط في رسم بياني من الدائرة الدائرية الفرعية أو الشريطي من الدائرة الدائرية. سيقدم دليلنا كيفية تحديد والوصول إلى الدائرة الفرعية أو الشريط الثاني في رسم بياني مركب، مما يتيح لك تحليل البيانات وتلاعبها بفعالية.
keywords: Aspose.Cells for .NET, رسم بياني من الدائرة الدائرية الفرعية, رسم بياني من الشريطي الفرعي, دائرة فرعية, شريط فرعي, تحليل البيانات, تلاعب البيانات.
type: docs
weight: 180
url: /ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك معرفة ما إذا كانت نقاط بيانات السلسلة في الدائرة الدائرية الثانية على *دائرة دائرية* أو في الشريط *شريطي* باستخدام Aspose.Cells. يرجى استخدام [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) خاصية لتحديده.

يرجى تنزيل [ملف إكسل نموذجي](5115193.xlsx) المستخدم في رمز العينة أدناه ورؤية الإخراج من وحدة التحكم الخاصة به. إذا فتحت [ملف إكسل العيني](5115193.xlsx)، ستجد، أن جميع نقاط البيانات التي تقل عن 10 داخل الشريط *شريطي* على رسم بياني من الدائرة الدائرية كما يظهر أيضًا في إخراج وحدة التحكم.
## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**
يوضح الكود المثالي التالي كيفية العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **مخرجات الوحدة**
يرجى الاطلاع على الناتج في وحدة التحكم التالية الذي تم إنشاؤه بعد تنفيذ الشيفرة العينة أعلاه مع [ملف إكسل عينة](5115193.xlsx). إذا كان [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) هو **false**، فإن نقطة البيانات داخل الفطيرة وإذا كانت **true**، فإن نقطة البيانات داخل الشريط.



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
