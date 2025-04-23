---
title: تصدير الرسم البياني إلى SVG مع خاصية viewBox
type: docs
weight: 190
url: /ar/java/export-chart-to-svg-with-viewbox-attribute/
---

بشكل افتراضي، عند تصدير الرسم البياني إلى تنسيق SVG، فإن سمة viewBox لا تكون مُدرجة في XML. ومع ذلك، توفر Aspose.Cells خاصية [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) التي عند ضبطها على **true** يتم تصدير الرسم البياني إلى SVG مع سمة viewBox.

إذا فتحت ملف SVG الخاص بالرسم البياني في المفكرة، فستجد سمة viewBox مماثلة لهذه.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## مقتطف الكود

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## مقالات ذات صلة

- [عرض الرسم البياني](/cells/ar/java/chart-rendering/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
