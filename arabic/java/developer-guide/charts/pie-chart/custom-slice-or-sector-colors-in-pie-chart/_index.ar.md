---
title: ألوان شريحة أو قطاع مخصصة في الرسم البياني الدائري
type: docs
weight: 30
url: /ar/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

يشرح هذا المقال كيفية إضافة ألوان مخصصة إلى شرائح/قطاعات الرسم البياني الدائري. بشكل افتراضي، تستخدم الرسومات الدائرية القوالب الافتراضية لمايكروسوفت إكسل. يمكن إعادة تعريف الألوان في الرسم البياني لاستخدام ألوان أخرى.

{{% /alert %}}

لضبط اللون المخصص لشرائح أو قطاعات الرسم البياني الدائري:

1. الوصول إلى [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) و[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1. تعيين لون من اختيارك باستخدام الطريقة [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor).

يشرح هذا المقال أيضًا كيفية ضبط:

- بيانات فئة الرسم البياني.
- عنوان الرسم البياني المرتبط بخلية.
- إعدادات خط عنوان الرسم البياني.
- موقع وسام.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) ليس محددًا لرسومات دائرية ولكن يمكن استخدامه لجميع أنواع الرسوم البيانية.

{{% /alert %}}

**ألوان شرائح مخصصة في الرسم البياني الدائري**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
{{< app/cells/assistant language="java" >}}
