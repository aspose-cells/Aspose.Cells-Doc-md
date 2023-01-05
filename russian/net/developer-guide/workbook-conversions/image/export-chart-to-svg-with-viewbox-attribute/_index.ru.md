---
title: Экспорт диаграммы в SVG с атрибутом viewBox
type: docs
weight: 280
url: /ru/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

 По умолчанию, когда диаграмма экспортируется в формат SVG,**видбокс** атрибут не включен в его XML. Тем не менее, Aspose.Cells обеспечивает[**Имажеорпринтоптионс.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) свойство, которое при установке на**истинный** экспортирует диаграмму в SVG с атрибутом viewBox.

{{% /alert %}}

## Экспорт диаграммы в SVG с атрибутом viewBox

Следующий пример кода экспортирует диаграмму в формат SVG с атрибутом viewBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

 Если вы откроете график SVG в блокноте, вы найдете**видбокс**аналогичный этому атрибут.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
