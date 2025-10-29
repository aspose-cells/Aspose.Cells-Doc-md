---
title: Экспорт диаграммы в SVG с атрибутом viewBox с использованием C++
linktitle: Экспорт диаграммы в SVG с атрибутом viewBox
type: docs
weight: 280
url: /ru/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Экспортировать диаграмму в SVG формат с атрибутом viewBox с помощью Aspose.Cells с Golang через C++.
---

{{% alert color="primary" %}}

По умолчанию, когда диаграмма экспортируется в формат SVG, атрибут **viewBox** не включается в его XML. Однако Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/), которое, когда установлено в **истину**, экспортирует диаграмму в SVG с атрибутом viewBox.

{{% /alert %}}

## Экспорт диаграммы в SVG с атрибутом viewBox

В следующем образце кода диаграмма экспортируется в формат SVG с атрибутом viewBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

Если вы откроете файл SVG диаграммы в блокноте, вы обнаружите атрибут **viewBox** аналогичный этому.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
