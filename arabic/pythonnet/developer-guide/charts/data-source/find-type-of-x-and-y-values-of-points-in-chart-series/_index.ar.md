---
title: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني
description: تعلم كيفية تحديد نوع القيم X و Y في نقاط سلسلة الرسم البياني باستخدام Aspose.Cells لبايثون via .NET. سيرينا دليلك الفرق بين أنواع البيانات وكيفية الوصول إليها والعمل معها في رسومك البيانية.
keywords: Aspose.Cells لبايثون via .NET، التصوير البياني، قيم X، قيم Y، أنواع البيانات، الوصول، العمل، سلسلة الرسم البياني.
type: docs
weight: 150
url: /ar/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
 أحيانًا، ترغب في معرفة نوع قيم X و Y لنقاط الرسم البياني في سلسلة. يوفر Aspose.Cells لبايثون via .NET الخاصيتين [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) و [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) لهذا الغرض. يرجى ملاحظة أنك ستحتاج إلى استدعاء طريقة [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) قبل أن تتمكن من استخدام هاتين الخاصيتين بشكل فعال.

## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**
 يحمّل المثال التالي ملف إكسل العينة ويفتح أول رسم بياني داخل أول ورقة عمل. ثم يستدعي الطريقة [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) ويحدد نوع القيم X و Y لنقطة الرسم البياني الأولى ويطبعها على وحدة التحكم. يرجى مراجعة المخرجات في وحدة التحكم أدناه للرجوع.

## **الكود المثالي**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
