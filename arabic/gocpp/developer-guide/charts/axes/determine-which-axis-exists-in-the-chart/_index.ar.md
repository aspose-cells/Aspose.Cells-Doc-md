---
title: تحديد أي محور موجود في المخطط باستخدام Golang عبر C++
description: تعلم كيفية تحديد أي محور موجود في رسم بياني تم إنشاؤه باستخدام Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية التعرف على والوصول إلى المحاور المختلفة في الرسم، بما في ذلك الفئة، القيمة، والمحاور الثانوية.
keywords: Aspose.Cells for C++، رسم بياني، محور، الوجود، الفئة، القيمة، الثانوي.
type: docs
weight: 140
url: /ar/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجود في المخطط أم لا. على سبيل المثال، يريد معرفة ما إذا كان محور القيم الثانوي موجود داخل المخطط أم لا. بعض المخططات مثل الكعكة، الكعكة المنفوخة، البيتزا، البيتزا المكدسة، الثلاثي الكعكة، الثلاثي المنفوخ، الدونات، الدونات المنفوخة، إلخ، لا تحتوي على محور.

توفر Aspose.Cells [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) لتحديد ما إذا كان لدى المخطط محور معين أم لا.

{{% /alert %}}

 يوضح الكود التالي استخدام [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) لتحديد ما إذا كان الرسم البياني التجريبي يحتوي على محور فئة وقيمة أساسي وثانوي.

## كود C++ لتحديد أي محور موجود في الرسم البياني

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## الناتج على واجهة الأوامر الناتجة عن الكود المثال

تم عرض إخراج وحدة التحكم للشفرة أدناه التي تعرض القيمة الصحيحة للفئة الأساسية ومحور القيمة والقيمة الخاطئة للفئة الثانوية ومحور القيمة.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
