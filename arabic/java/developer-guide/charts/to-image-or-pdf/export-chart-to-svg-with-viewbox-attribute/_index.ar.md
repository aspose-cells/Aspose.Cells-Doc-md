---
title: تصدير المخطط إلى SVG مع سمة viewBox
type: docs
weight: 190
url: /ar/java/export-chart-to-svg-with-viewbox-attribute/
---
 بشكل افتراضي ، عندما يتم تصدير المخطط إلى تنسيق SVG ، فإن ملف**viewBox** السمة غير مدرجة في XML الخاص بها. ومع ذلك ، يوفر Aspose.Cells[**ImageOrPrintOptions.setSVGFitToViewPort ()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) الخاصية التي عند التعيين على**حقيقي** يصدر المخطط إلى SVG بسمة viewBox.

 إذا فتحت SVG للرسم البياني في المفكرة ، فستجد ملف**viewBox** سمة مشابهة لهذا.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## مقتطف الرمز

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## مقالات ذات صلة

- [عرض المخطط](/cells/ar/java/chart-rendering/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة مع العرض والارتفاع المطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
