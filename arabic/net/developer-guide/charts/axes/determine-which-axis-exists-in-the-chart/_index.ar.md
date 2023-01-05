---
title: حدد المحور الموجود في المخطط
type: docs
weight: 140
url: /ar/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتاج المستخدم إلى معرفة ما إذا كان هناك محور معين في المخطط. على سبيل المثال ، يريد معرفة ما إذا كان محور القيمة الثانوية موجودًا داخل المخطط أم لا. لا تحتوي بعض المخططات مثل Pie و PieExploded و PiePie و PieBar و Pie3D و Pie3DExploded و Donut و DoughnutExploded وما إلى ذلك على محور.

 يوفر Aspose.Cells[**Chart.HasAxis (نوع محور نوع المحور ، منطقي هو أساسي)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) طريقة لتحديد ما إذا كان المخطط له محور معين أم لا.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي استخدام[**Chart.HasAxis (نوع محور نوع المحور ، منطقي هو أساسي)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)لتحديد ما إذا كان مخطط العينة يحتوي على فئة أساسية وثانوية ومحور القيمة.

## C# كود لتحديد المحور الموجود بالمخطط

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## ناتج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

تم عرض ناتج وحدة التحكم للرمز أدناه والذي يعرض صحيحًا للفئة الأساسية ومحور القيمة وخطأ للفئة الثانوية ومحور القيمة.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
