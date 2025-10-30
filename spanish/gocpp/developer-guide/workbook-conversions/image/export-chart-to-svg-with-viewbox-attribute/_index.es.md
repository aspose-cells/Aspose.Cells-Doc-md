---
title: Exportar gráfico a SVG con atributo viewBox usando C++
linktitle: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 280
url: /es/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exportar un gráfico a formato SVG con atributo viewBox usando Aspose.Cells con Golang mediante C++
---

{{% alert color="primary" %}}

De forma predeterminada, cuando el gráfico se exporta al formato SVG, el atributo **viewBox** no se incluye en su XML. Sin embargo, Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/) que, cuando se establece en **true**, exporta el gráfico a SVG con el atributo viewBox.

{{% /alert %}}

## Exportar gráfico a SVG con el atributo viewBox

El siguiente código de ejemplo exporta el gráfico al formato SVG con el atributo viewBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

Si abres el SVG del gráfico en el bloc de notas, encontrarás el atributo **viewBox** similar a este:

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
