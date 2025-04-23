---
title: Экспорт диаграммы в SVG с атрибутом viewBox
type: docs
weight: 190
url: /ru/java/export-chart-to-svg-with-viewbox-attribute/
---

По умолчанию, когда диаграмма экспортируется в формат SVG, атрибут **viewBox** не включается в ее XML. Тем не менее, Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort), которое, когда установлено в **true**, экспортирует диаграмму в SVG с атрибутом viewBox.

Если вы откроете файл SVG диаграммы в блокноте, вы обнаружите атрибут **viewBox** аналогичный этому.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Фрагмент кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Связанные статьи

- [Отображение диаграммы](/cells/ru/java/chart-rendering/)
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
