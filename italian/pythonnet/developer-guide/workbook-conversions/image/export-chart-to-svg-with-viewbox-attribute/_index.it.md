---
title: Esporta il grafico in SVG con attributo viewBox
type: docs
weight: 280
url: /it/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Esporta il grafico in SVG con attributo viewBox utilizzando Aspose.Cells per Python via .NET API.
keywords: Python Esporta il grafico in SVG con attributo viewBox, Esportare il grafico in SVG con attributo viewBox in Python via NET, Convertire il grafico in SVG con attributo viewBox in Python.
---

{{% alert color="primary" %}}

Per impostazione predefinita, quando il grafico viene esportato in formato SVG, l'attributo **viewBox** non è incluso nel suo XML. Tuttavia, Aspose.Cells for Python via .NET fornisce la proprietà [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) che, quando impostata su **true**, esporta il grafico in SVG con l'attributo viewBox.

{{% /alert %}}

## Esportare il grafico in SVG con attributo viewBox

Il seguente codice di esempio esporta il grafico nel formato SVG con l'attributo viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Se apri l'SVG del grafico in notepad, troverai l'attributo **viewBox** simile a questo.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
