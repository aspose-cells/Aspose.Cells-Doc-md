---
title: تصدير الرسم البياني إلى SVG مع خاصية viewBox
type: docs
weight: 280
url: /ar/python-net/export-chart-to-svg-with-viewbox-attribute/
description: تصدير الرسم البياني إلى SVG بخاصية viewBox باستخدام Aspose.Cells for Python via .NET API.
keywords: تصدير الرسم البياني إلى SVG بخاصية viewBox في Python, تصدير الرسم البياني إلى SVG بخاصية viewBox في Python via NET, تحويل الرسم البياني إلى SVG بخاصية viewBox في Python.
---

{{% alert color="primary" %}}

بشكل افتراضي، عند تصدير الرسم البياني إلى تنسيق SVG، لا تتم تضمين خاصية **viewBox** في XML الخاص به. ومع ذلك، يوفر Aspose.Cells for Python via .NET خاصية [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) عندما يتم تعيينها على **true** يتم تصدير الرسم البياني إلى SVG بخاصية viewBox.

{{% /alert %}}

## تصدير الرسم البياني إلى SVG بسمة viewBox

الرمز العينة التالي يقوم بتصدير الرسم البياني إلى تنسيق SVG مع سمة viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

إذا فتحت ملف SVG الخاص بالرسم البياني في المفكرة، فستجد سمة viewBox مماثلة لهذه.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
