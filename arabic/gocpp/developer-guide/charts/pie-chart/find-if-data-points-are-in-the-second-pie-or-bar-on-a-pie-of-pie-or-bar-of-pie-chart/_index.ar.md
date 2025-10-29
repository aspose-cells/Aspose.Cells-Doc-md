---
title: ابحث إذا كانت نقاط البيانات في المخطط الدائري الثاني أو الشريط في مخطط دائرية من دائرية أو مخطط شريط من دائرية باستخدام جولانج عبر C++
linktitle: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني
description: تعلم كيفية استخدام Aspose.Cells for C++ للعثور على ما إذا كانت نقاط البيانات في الفطيرة الثانية أو العمود على رسم بياني من نوع فطيرة من فطيرة أو رسم بياني من نوع عمود في فطيرة. سيُظهر دليلنا كيفية التعرف على والوصول إلى الفطيرة أو العامود الثانوي على رسم بياني مركب، مما يتيح لك تحليل البيانات ومعالجتها بفعالية.
keywords: Aspose.Cells for C++، رسم بياني من نوع فطيرة من فطيرة، رسم بياني من نوع عمود من فطيرة، فطيرة ثانوية، عمود ثانوي، تحليل البيانات، معالجة البيانات.
type: docs
weight: 180
url: /ar/go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك العثور على ما إذا كانت نقاط بيانات السلسلة في الدائرة الثانية في مخطط *Pie of Pie* أو في الشريط في مخطط *Bar of Pie* باستخدام Aspose.Cells. يرجى استخدام الخاصية [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/) لتحديد ذلك.

يرجى تنزيل [ملف إكسل نموذجي](5115193.xlsx) المستخدم في رمز العينة أدناه ورؤية الإخراج من وحدة التحكم الخاصة به. إذا فتحت [ملف إكسل العيني](5115193.xlsx)، ستجد، أن جميع نقاط البيانات التي تقل عن 10 داخل الشريط *شريطي* على رسم بياني من الدائرة الدائرية كما يظهر أيضًا في إخراج وحدة التحكم.

## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**
يوضح الكود المثالي التالي كيفية العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **مخرجات الوحدة**
يرجى الاطلاع على مخرجات وحدة التحكم التالية التي تم إنشاؤها بعد تنفيذ رمز العينة أعلاه مع ملف Excel التجريبي ([ملفExcel عينة](5115193.xlsx)). إذا كانت [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) **غير صحيحة**، فإن نقطة البيانات تقع داخل الفطيرة أو إذا كانت **صحيحة**، فإن نقطة البيانات تقع داخل العمود.

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
