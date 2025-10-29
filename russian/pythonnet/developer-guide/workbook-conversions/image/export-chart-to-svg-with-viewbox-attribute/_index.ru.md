---
title: Экспорт диаграммы в SVG с атрибутом viewBox
type: docs
weight: 280
url: /ru/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Экспорт графика в SVG с атрибутом  viewBox  с использованием Aspose.Cells для Python via .NET API.
keywords: Python Экспорт графика в SVG с атрибутом  viewBox , Экспорт графика в SVG с атрибутом  viewBox  в Python via NET, Преобразование графика Python в SVG с атрибутом  viewBox .
---

{{% alert color="primary" %}}

По умолчанию, при экспорте графика в формат SVG, атрибут **viewBox** не включается в его XML. Однако Aspose.Cells для Python via .NET предоставляет свойство [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/), которое, когда установлено в **true**, экспортирует график в SVG с атрибутом **viewBox**.

{{% /alert %}}

## Экспорт диаграммы в SVG с атрибутом viewBox

В следующем образце кода диаграмма экспортируется в формат SVG с атрибутом viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Если вы откроете файл SVG диаграммы в блокноте, вы обнаружите атрибут **viewBox** аналогичный этому.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
