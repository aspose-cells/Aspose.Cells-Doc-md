---
title: تحديد المحور الموجود في الرسم البياني
description: تعلم كيفية تحديد المحور الذي يوجد في مخطط تم إنشاؤه باستخدام Aspose.Cells for .NET. سيساعدك دليلنا على فهم كيفية تحديد والوصول إلى المحاور المختلفة في المخطط، بما في ذلك محور الفئة والقيم والمحاور الثانوية.
keywords: Aspose.Cells for .NET، مخطط، محور، وجود، فئة، قيمة، ثانوي.
type: docs
weight: 140
url: /ar/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجود في المخطط أم لا. على سبيل المثال، يريد معرفة ما إذا كان محور القيم الثانوي موجود داخل المخطط أم لا. بعض المخططات مثل الكعكة، الكعكة المنفوخة، البيتزا، البيتزا المكدسة، الثلاثي الكعكة، الثلاثي المنفوخ، الدونات، الدونات المنفوخة، إلخ، لا تحتوي على محور.

توفر Aspose.Cells [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) لتحديد ما إذا كان لدى المخطط محور معين أم لا.

{{% /alert %}}

يوضح الرمز العيني التالي استخدام [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) لتحديد ما إذا كان لدى المخطط العيني العيني الأساسي والثانوي ومحور الفئة والقيمة.

## كود C# لتحديد أي محور موجود في المخطط

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

تم عرض إخراج وحدة التحكم للشفرة أدناه التي تعرض القيمة الصحيحة للفئة الأساسية ومحور القيمة والقيمة الخاطئة للفئة الثانوية ومحور القيمة.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
