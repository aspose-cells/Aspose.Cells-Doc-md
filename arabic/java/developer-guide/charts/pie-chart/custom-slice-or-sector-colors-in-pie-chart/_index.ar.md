---
title: شريحة مخصصة أو ألوان قطاعية في مخطط دائري
type: docs
weight: 30
url: /ar/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

تشرح هذه المقالة كيفية إضافة ألوان مخصصة إلى شرائح / قطاعات المخطط الدائري. بشكل افتراضي ، تستخدم المخططات الدائرية القالب الافتراضي Microsoft Excel. لاستخدام ألوان أخرى ، من الممكن إعادة تعريف الألوان في الرسم البياني.

{{% /alert %}}

لتعيين اللون المخصص للشرائح أو القطاعات الفردية للمخطط الدائري:

1.  الوصول إلى[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) أشياء[**تشارت بوينت**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  قم بتعيين لون من اختيارك باستخدام[**ChartPoint.getArea (). setForegroundColor ()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)طريقة.

تشرح هذه المقالة أيضًا كيفية التعيين:

- بيانات فئة الرسم البياني.
- عنوان مخطط مرتبط بخلية.
- إعدادات خط عنوان المخطط.
- موقف الأسطورة.

{{% alert color="primary" %}}

[**ChartPoint.getArea (). setForegroundColor ()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) ليست خاصة بالمخططات الدائرية ولكن يمكن استخدامها لجميع أنواع المخططات.

{{% /alert %}}

**ألوان الشرائح المخصصة في المخطط الدائري**

![ما يجب القيام به: image_بديل_نص](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
