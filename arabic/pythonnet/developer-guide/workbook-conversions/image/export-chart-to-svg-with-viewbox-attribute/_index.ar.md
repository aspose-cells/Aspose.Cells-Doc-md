---
title: تصدير الرسم البياني إلى SVG مع سمة viewBox
type: docs
weight: 280
url: /ar/python-net/export-chart-to-svg-with-viewbox-attribute/
description: تصدير المخطط إلى SVG مع سمة viewBox باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 بشكل افتراضي، عندما يتم تصدير المخطط إلى تنسيق SVG، سيتم عرض الملف**viewBox** لم يتم تضمين السمة في XML الخاص به. غير أن Aspose.Cells for Python via .NET يوفر[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) الخاصية التي عند تعيينها على**حقيقي** تصدير المخطط إلى SVG مع سمة viewBox.

{{% /alert %}}

##  تصدير الرسم البياني إلى SVG مع سمة viewBox

يقوم نموذج التعليمات البرمجية التالي بتصدير المخطط إلى تنسيق SVG باستخدام سمة viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 إذا قمت بفتح SVG للمخطط في المفكرة، فستجد**viewBox** صفة مشابهة لهذا.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
