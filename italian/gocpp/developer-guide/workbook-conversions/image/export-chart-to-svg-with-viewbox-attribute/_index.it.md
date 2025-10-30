---
title: Esporta Grafico in SVG con attributo viewBox usando C++
linktitle: Esporta il grafico in SVG con attributo viewBox
type: docs
weight: 280
url: /it/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Esporta un grafico in formato SVG con attributo viewBox usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Per impostazione predefinita, quando il grafico viene esportato nel formato SVG, l'attributo **viewBox** non è incluso nel suo XML. Tuttavia, Aspose.Cells fornisce [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/) proprietà che, quando impostata su **true**, esporta il grafico in SVG con l'attributo viewBox.

{{% /alert %}}

## Esportare il grafico in SVG con attributo viewBox

Il seguente codice di esempio esporta il grafico nel formato SVG con l'attributo viewBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

Se apri l'SVG del grafico in notepad, troverai l'attributo **viewBox** simile a questo.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
