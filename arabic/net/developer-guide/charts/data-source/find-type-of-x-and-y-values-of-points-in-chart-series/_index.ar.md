---
title: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني
description: تعلم كيفية تحديد نوع قيم X و Y في نقاط سلسلة الرسم البياني باستخدام Aspose.Cells for .NET. سيقوم دليلنا بشرح أنواع قيم البيانات المختلفة ويظهر لك كيفية الوصول إليها والعمل معها في رسوماتك.
keywords: Aspose.Cells for .NET، الرسم البياني، قيم X، قيم Y، أنواع البيانات، الوصول، العمل معها، سلسلة الرسم البياني.
type: docs
weight: 150
url: /ar/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، ترغب في معرفة نوع قيم X و Y لنقاط الرسم البياني في سلسلة. توفر Aspose.Cells خصائص ChartPoint.XValueType و ChartPoint.YValueType التي يمكن استخدامها لهذا الغرض. يرجى ملاحظة أنه يجب عليك استدعاء طريقة Chart.Calculate() قبل أن تتمكن من استخدام هذه الخصائص بشكل فعال.
## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**
يقوم الكود العيني التالي بتحميل [ملف Excel عيني](64716905.xlsx) والوصول إلى الرسم البياني الأول في الورقة العمل الأولى. ثم يقوم بدعوة طريقة Chart.Calculate() والعثور على نوع قيم X و Y لأول نقطة في الرسم البياني ويطبعها على وحدة التحكم. يرجى الاطلاع على الإخراج الموجود أدناه كمرجع.

## **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
