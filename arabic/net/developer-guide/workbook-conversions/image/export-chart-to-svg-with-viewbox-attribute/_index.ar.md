---
title: تصدير المخطط إلى SVG مع سمة viewBox
type: docs
weight: 280
url: /ar/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 بشكل افتراضي ، عندما يتم تصدير المخطط إلى تنسيق SVG ، فإن ملف**viewBox** السمة غير مدرجة في XML الخاص بها. ومع ذلك ، يوفر Aspose.Cells[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) الخاصية التي عند التعيين على**حقيقي** يقوم بتصدير المخطط إلى SVG بسمة viewBox.

{{% /alert %}}

## تصدير المخطط إلى SVG مع سمة viewBox

يقوم نموذج التعليمات البرمجية التالي بتصدير المخطط إلى تنسيق SVG بسمة viewBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 إذا قمت بفتح SVG الرسم البياني في المفكرة ، فستجد ملف**viewBox**سمة مشابهة لهذا.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
