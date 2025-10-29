---
title: Exporter un graphique au format SVG avec l’attribut viewBox en utilisant C++
linktitle: Exporter le graphique en SVG avec l attribut viewBox
type: docs
weight: 280
url: /fr/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exporter un graphique au format SVG avec l attribut viewBox en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Par défaut, lorsque le graphique est exporté au format SVG, l'attribut **viewBox** n'est pas inclus dans son XML. Cependant, Aspose.Cells fournit la propriété [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/) qui, lorsqu'elle est définie sur **true**, exporte le graphique en SVG avec l'attribut viewBox.

{{% /alert %}}

## Exporter le graphique en SVG avec l'attribut viewBox

Le code d'exemple suivant exporte le graphique au format SVG avec l'attribut viewBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez l'attribut **viewBox** similaire à ceci.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
