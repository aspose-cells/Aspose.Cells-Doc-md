---
title: ابحث عن نوع قيم X و Y للنقاط في سلسلة المخططات
type: docs
weight: 150
url: /ar/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **سيناريوهات الاستخدام الممكنة**
في وقت ما ، تريد معرفة نوع قيم X و Y لنقاط المخطط في سلسلة. يوفر Aspose.Cells خصائص ChartPoint.XValueType و ChartPoint.YValueType التي يمكن استخدامها لهذا الغرض. يرجى ملاحظة أنه سيتعين عليك استدعاء طريقة Chart.Calculate () قبل أن تتمكن من استخدام هذه الخصائص بفعالية.
## **ابحث عن نوع قيم X و Y للنقاط في سلسلة المخططات**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716905.xlsx) والوصول إلى المخطط الأول داخل ورقة العمل الأولى. ثم يستدعي طريقة Chart.Calculate () ويجد نوع قيم X و Y لنقطة المخطط الأولى ويطبعها على وحدة التحكم. يرجى الاطلاع على إخراج وحدة التحكم الموضح أدناه للحصول على مرجع.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **إخراج وحدة التحكم**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
