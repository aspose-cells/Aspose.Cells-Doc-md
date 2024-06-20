---
title: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني
type: docs
weight: 910
url: /ar/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك إيجاد ما إذا كانت نقاط البيانات في الفقاعة الثانية على مخطط 'بي of بي' أو في العامود على مخطط 'عمود من بي' باستخدام Aspose.Cells. يرجى استخدام خاصية [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) لتحديدها.

يرجى تنزيل [ملف الإكسل المثالي](5473373.xlsx) المستخدم في الكود المثالي التالي واطلع على إخراج وحدة التحكم. إذا قمت بفتح [ملف الإكسل المثالي](5473373.xlsx)، ستجد أن جميع نقاط البيانات التي تقل عن 10 داخل العمود على مخطط 'عمود من بي' كما هو موضح أيضًا في إخراج وحدة التحكم.
## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**
يوضح الكود المثالي التالي كيفية العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **مخرجات الوحدة**
يرجى رؤية إخراج وحدة التحكم التالي الذي تم إنشاؤه بعد تنفيذ الكود المثالي أعلاه مع [ملف الإكسل المثالي](5473373.xlsx). إذا كان [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) خاطئًا، فإن نقطة البيانات داخل الفقاعة وإذا كان صحيحًا، فإن نقطة البيانات داخل العمود.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
