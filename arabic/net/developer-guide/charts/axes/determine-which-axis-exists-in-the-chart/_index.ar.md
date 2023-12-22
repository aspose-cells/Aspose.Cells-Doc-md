---
title: تحديد المحور الموجود في المخطط
description: تعرف على كيفية تحديد المحور الموجود في المخطط الذي تم إنشاؤه باستخدام Aspose.Cells for .NET. سيساعدك دليلنا على فهم كيفية تحديد المحاور المختلفة في المخطط والوصول إليها، بما في ذلك الفئة والقيمة والمحاور الثانوية.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /ar/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المستخدم إلى معرفة ما إذا كان هناك محور معين موجود في المخطط. على سبيل المثال، يريد معرفة ما إذا كان محور القيمة الثانوية موجودًا داخل المخطط أم لا. بعض المخططات مثل Pie وPieExploded وPiePie وPieBar وPie3D وPie3DExploded وDoughnut وDoughnutExploded وما إلى ذلك لا تحتوي على محور.

 Aspose.Cells يوفر[**Chart.HasAxis(AxisType axisType، bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) طريقة لتحديد ما إذا كان المخطط يحتوي على محور معين أم لا.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي استخدام[**Chart.HasAxis(AxisType axisType، bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)لتحديد ما إذا كان نموذج المخطط يحتوي على الفئة الأساسية والثانوية ومحور القيمة.

##  كود C# لتحديد المحور الموجود في المخطط

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## إخراج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

تم عرض مخرجات وحدة التحكم الخاصة بالرمز أدناه والتي تظهر صحيحًا للفئة الأساسية ومحور القيمة وخطأ للفئة الثانوية ومحور القيمة.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
