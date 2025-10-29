---
title: العثور على نوع قيم x و y للنقاط في سلسلة الرسم البياني باستخدام Golang عبر C++
linktitle: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني
description: تعلم كيف تحدد نوع القيم X وY في نقاط سلسلة المخططات باستخدام Aspose.Cells for C++. دليلنا سيشرح أنواع قيم البيانات المختلفة ويعرض كيفية الوصول إليها والعمل معها في مخططاتك.
keywords: Aspose.Cells for C++، رسم بياني، قيم X، قيم Y، أنواع البيانات، الوصول، العمل بها، سلسلة المخططات.
type: docs
weight: 150
url: /ar/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، تريد معرفة نوع القيم X وY لنقاط مخطط في سلسلة. يوفر Aspose.Cells طريقتي `ChartPoint::get_XValueType` و `ChartPoint::get_YValueType` لهذا الغرض. يرجى ملاحظة أنه من الضروري استدعاء `Chart::Calculate()` قبل استخدام هذه الخصائص بشكل فعال.

## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**
الكود النموذجي التالي يحمّل ملف Excel [عينة](64716905.xlsx) ويصل إلى المخطط الأول داخل ورقة العمل الأولى. ثم يستدعي `Chart::Calculate()` ويحدد نوع القيم X وY لنقطة المخطط الأولى ويطبعها على وحدة التحكم. الرجاء مراجعة مخرجات وحدة التحكم أدناه كمرجع.

## **الكود المثالي**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
