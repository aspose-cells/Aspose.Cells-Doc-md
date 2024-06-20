---
title: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني
type: docs
weight: 110
url: /ar/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، قد ترغب في معرفة نوع قيم X وY لنقاط الرسم البياني في سلسلة. توفر Aspose.Cells الخصائص [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) و [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) التي يمكن استخدامها لهذا الغرض. يرجى ملاحظة أنه يجب عليك استدعاء الطريقة [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) قبل أن تتمكن من استخدام هذه الخصائص بشكل فعال.

## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**

يقوم الكود النموذجي التالي بتحميل [ملف Excel عيني](64716920.xlsx) والوصول إلى الرسم البياني الأول داخل الورقة العمل الأولى. ثم يستدعي الطريقة [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) ويجد نوع قيم X وY لأول نقطة في الرسم البياني ويطبعها على وحدة التحكم. يرجى رؤية الناتج المعروض على وحدة التحكم كمرجع.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
