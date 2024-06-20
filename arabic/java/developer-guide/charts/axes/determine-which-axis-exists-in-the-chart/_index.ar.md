---
title: تحديد المحور الموجود في الرسم البياني
type: docs
weight: 130
url: /ar/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجودًا في الرسم البياني أم لا. على سبيل المثال، يريد معرفة ما إذا كان محور القيم الثانوي موجود داخل الرسم البياني أم لا. بعض الرسوم البيانية مثل Pie وPieExploded وPiePie وPieBar وPie3D وPie3DExploded وDoughnut وDoughnutExploded إلخ ليس لديها محور.

توفر Aspose.Cells [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) لتحديد ما إذا كان لدى المخطط محور معين أم لا.

{{% /alert %}}

## تحديد المحور الموجود في الرسم البياني

الصورة الملتقطة التالية تظهر رسمًا بيانيًا يحتوي فقط على الفئة الرئيسية ومحور القيمة. لا يحتوي على أي فئة ثانوية أو محور قيمة.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

يبرز الرمز النموذجي التالي استخدام [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) لتحديد ما إذا كان لدى الرسم البياني النموذجي محور أساسي وثانوي للفئة والقيمة. يتم عرض نتيجة وحدة التحكم من الرمز النموذجي أدناه والتي تعرض صحيح للفئة الأساسية والمحور القيم ويعرض خطأ للفئة الثانوية والمحور القيم.

### كود Java لتحديد المحور الموجود في الرسم البياني

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

هنا ناتج وحدة الطرفية للكود النموذجي أعلاه.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
