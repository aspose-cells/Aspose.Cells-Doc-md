---
title: اكتشف ما إذا كانت نقاط البيانات موجودة في المخطط الدائري الثاني أو الشريطي في مخطط دائري دائري أو مخطط دائري شريطي
type: docs
weight: 180
url: /ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **سيناريوهات الاستخدام الممكنة**
 يمكنك معرفة ما إذا كانت نقاط بيانات المتسلسلة موجودة في الدائرة الثانية*فطيرة فطيرة* الرسم البياني أو في شريط*شريط الفطيرة* الرسم البياني باستخدام Aspose.Cells. الرجاء استخدام[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)الملكية لتحديد ذلك.

 يرجى تنزيل ملف[نموذج ملف اكسل](5115193.xlsx) المستخدمة في نموذج التعليمات البرمجية التالي وانظر إخراج وحدة التحكم الخاصة به. إذا قمت بفتح ملف[نموذج ملف اكسل](5115193.xlsx) ستجد جميع نقاط البيانات الأقل من 10 داخل شريط*شريط الفطيرة*الرسم البياني كما هو موضح أيضًا من خلال إخراج وحدة التحكم.
## **اكتشف ما إذا كانت نقاط البيانات موجودة في المخطط الدائري الثاني أو الشريطي في مخطط دائري دائري أو مخطط دائري شريطي**
 يوضح نموذج التعليمات البرمجية التالي كيفية البحث عما إذا كانت نقاط البيانات موجودة في الدائرة أو الشريط الثاني على ملف*فطيرة فطيرة* أو*شريط الفطيرة*جدول.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **إخراج وحدة التحكم**
 يرجى الاطلاع على إخراج وحدة التحكم التالية الذي تم إنشاؤه بعد تنفيذ نموذج التعليمات البرمجية أعلاه باستخدام[نموذج ملف اكسل](5115193.xlsx) . إذا[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) يكون**خاطئة** ، تكون نقطة البيانات داخل الدائرة أو إذا كانت كذلك**حقيقي**، ثم تكون نقطة البيانات داخل الشريط.



{{< highlight "java" >}}

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
