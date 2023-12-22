---
title: ابحث عن نوع قيم X وY للنقاط في سلسلة المخططات
description: تعرف على كيفية تحديد نوع قيم X وY في نقاط سلسلة المخطط باستخدام Aspose.Cells for .NET. سيشرح دليلنا الأنواع المختلفة لقيم البيانات ويوضح لك كيفية الوصول إليها والتعامل معها في مخططاتك.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /ar/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، تريد معرفة نوع قيم X وY لنقاط المخطط في سلسلة. Aspose.Cells يوفر خصائص ChartPoint.XValueType وChartPoint.YValueType التي يمكن استخدامها لهذا الغرض. يرجى ملاحظة أنه سيتعين عليك استدعاء الأسلوب Chart.Calculate() قبل أن تتمكن من استخدام هذه الخصائص بشكل فعال.
##  **ابحث عن نوع قيم X وY للنقاط في سلسلة المخططات**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[عينة من ملف إكسل](64716905.xlsx) ويصل إلى المخطط الأول داخل ورقة العمل الأولى. ثم يستدعي الأسلوب Chart.Calculate() ويبحث عن نوع قيم X وY لنقطة المخطط الأولى ويطبعها على وحدة التحكم. يرجى الاطلاع على مخرجات وحدة التحكم الموضحة أدناه للحصول على مرجع.
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **إخراج وحدة التحكم**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
