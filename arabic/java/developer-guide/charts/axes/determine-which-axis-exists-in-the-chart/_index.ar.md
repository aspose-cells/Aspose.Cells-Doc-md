---
title: حدد المحور الموجود في المخطط
type: docs
weight: 130
url: /ar/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتاج المستخدم إلى معرفة ما إذا كان هناك محور معين في المخطط. على سبيل المثال ، يريد معرفة ما إذا كان محور القيمة الثانوية موجودًا داخل المخطط أم لا. لا تحتوي بعض المخططات مثل Pie و PieExploded و PiePie و PieBar و Pie3D و Pie3DExploded و Donut و DoughnutExploded وما إلى ذلك على محور.

 يوفر Aspose.Cells[**Chart.hasAxis (int axisType ، قيمة منطقية أساسية)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) طريقة لتحديد ما إذا كان المخطط يحتوي على محور معين أم لا.

{{% /alert %}}

## حدد المحور الموجود في المخطط

تُظهر لقطة الشاشة التالية مخططًا يحتوي فقط على الفئة الأساسية ومحور القيمة. لا يحتوي على أي فئة ثانوية ومحور قيمة.

![ما يجب القيام به: image_بديل_نص](determine-which-axis-exists-in-the-chart_1.png)

 يوضح نموذج التعليمات البرمجية التالي استخدام[**Chart.hasAxis (int axisType ، قيمة منطقية أساسية)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)لتحديد ما إذا كان مخطط العينة يحتوي على الفئة الأساسية والثانوية ومحور القيمة. تم عرض ناتج وحدة التحكم للرمز أدناه والذي يعرض صحيحًا للفئة الأساسية ومحور القيمة وخطأ للفئة الثانوية ومحور القيمة.

### كود Java لتحديد المحور الموجود بالمخطط

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### ناتج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
