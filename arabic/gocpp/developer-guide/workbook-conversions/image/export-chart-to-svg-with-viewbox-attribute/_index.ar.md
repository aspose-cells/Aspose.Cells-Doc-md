---
title: تصدير المخطط إلى SVG مع خاصية viewBox باستخدام C++
linktitle: تصدير الرسم البياني إلى SVG مع خاصية viewBox
type: docs
weight: 280
url: /ar/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: تصدير رسم بياني إلى صيغة SVG مع خاصية viewBox باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

بشكل افتراضي، عند تصدير الرسم البياني إلى تنسيق SVG، لا يتم تضمين سمة **viewBox** في XML الخاص به. ومع ذلك، يوفر Aspose.Cells خاصية [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/) التي عند تعيينها على **true** يقوم بتصدير الرسم البياني إلى SVG مع سمة viewBox.

{{% /alert %}}

## تصدير الرسم البياني إلى SVG بسمة viewBox

الرمز العينة التالي يقوم بتصدير الرسم البياني إلى تنسيق SVG مع سمة viewBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

إذا فتحت ملف SVG الخاص بالرسم البياني في المفكرة، فستجد سمة viewBox مماثلة لهذه.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
