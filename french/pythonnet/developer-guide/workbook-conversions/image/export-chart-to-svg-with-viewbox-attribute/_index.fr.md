---
title: Exporter le graphique en SVG avec l attribut viewBox
type: docs
weight: 280
url: /fr/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exporter un graphique au format SVG avec l attribut viewBox en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Exporter un graphique au format SVG avec l attribut viewBox en Python via NET, Convertir un graphique en SVG avec l attribut viewBox en Python, Convertir un graphique au format SVG avec l attribut viewBox en Python.
---

{{% alert color="primary" %}}

Par défaut, lorsque le graphique est exporté au format SVG, l'attribut **viewBox** n'est pas inclus dans son XML. Cependant, Aspose.Cells pour Python via .NET fournit [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) propriété qui, lorsqu'elle est définie sur **true**, exporte le graphique au format SVG avec l'attribut viewBox.

{{% /alert %}}

## Exporter le graphique en SVG avec l'attribut viewBox

Le code d'exemple suivant exporte le graphique au format SVG avec l'attribut viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez l'attribut **viewBox** similaire à ceci.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
