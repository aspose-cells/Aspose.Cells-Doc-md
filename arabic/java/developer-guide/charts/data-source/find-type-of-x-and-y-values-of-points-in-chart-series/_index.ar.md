---
title: ابحث عن نوع قيم X و Y للنقاط في سلسلة المخططات
type: docs
weight: 110
url: /ar/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، تريد معرفة نوع قيم X و Y لنقاط المخطط في سلسلة. يوفر Aspose.Cells[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)و[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)الخصائص التي يمكن استخدامها لهذا الغرض. يرجى ملاحظة ، سوف تضطر إلى الاتصال[**Chart.calculate ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) قبل أن تتمكن من استخدام هذه الخصائص بفعالية.

## **ابحث عن نوع قيم X و Y للنقاط في سلسلة المخططات**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716920.xlsx)والوصول إلى المخطط الأول داخل ورقة العمل الأولى. ثم يستدعي[**Chart.calculate ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()والبحث عن نوع قيم X و Y لنقطة المخطط الأولى وطباعتها على وحدة التحكم. يرجى الاطلاع على إخراج وحدة التحكم الموضح أدناه للحصول على مرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
