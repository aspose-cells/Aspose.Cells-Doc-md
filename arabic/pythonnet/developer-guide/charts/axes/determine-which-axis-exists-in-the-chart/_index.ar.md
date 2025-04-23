---
title: تحديد المحور الموجود في الرسم البياني
description: تعلم كيفية تحديد وجود محور معين في مخطط تم إنشاؤه باستخدام Aspose.Cells لبايثون via .NET. دليلنا سيساعدك على فهم كيفية التعرف على والوصول إلى المحاور المختلفة في مخطط، بما في ذلك الفئات، القيم، والمحاور الثانوية.
keywords: Aspose.Cells لبايثون via .NET، مخطط، محور، الوجود، فئة، قيمة، ثانوي.
type: docs
weight: 140
url: /ar/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجود في المخطط أم لا. على سبيل المثال، يريد معرفة ما إذا كان محور القيم الثانوي موجود داخل المخطط أم لا. بعض المخططات مثل الكعكة، الكعكة المنفوخة، البيتزا، البيتزا المكدسة، الثلاثي الكعكة، الثلاثي المنفوخ، الدونات، الدونات المنفوخة، إلخ، لا تحتوي على محور.

توفر Aspose.Cells لبايثون via .NET الطريقة [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) لتحديد ما إذا كان للمخطط محور معين أم لا.

{{% /alert %}}

يوضح الرمز العيني التالي استخدام [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) لتحديد ما إذا كان لدى المخطط العيني العيني الأساسي والثانوي ومحور الفئة والقيمة.

## كود C# لتحديد أي محور موجود في المخطط

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

تم عرض إخراج وحدة التحكم للشفرة أدناه التي تعرض القيمة الصحيحة للفئة الأساسية ومحور القيمة والقيمة الخاطئة للفئة الثانوية ومحور القيمة.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
