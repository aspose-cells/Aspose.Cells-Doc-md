---
title: Exporter le graphique vers SVG avec l'attribut viewBox
type: docs
weight: 280
url: /fr/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exportez le graphique vers SVG avec l'attribut viewBox en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 Par défaut, lorsque le graphique est exporté au format SVG, le**viewBox** L'attribut n'est pas inclus dans son XML. Cependant, le Aspose.Cells for Python via .NET fournit[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) propriété qui, lorsqu'elle est définie sur**vrai** exporte le graphique vers SVG avec l'attribut viewBox.

{{% /alert %}}

##  Exporter le graphique vers SVG avec l'attribut viewBox

L'exemple de code suivant exporte le graphique au format SVG avec l'attribut viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez le**viewBox** attribut similaire à celui-ci.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
