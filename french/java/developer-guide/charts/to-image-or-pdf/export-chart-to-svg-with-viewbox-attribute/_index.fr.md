---
title: Exporter le graphique en SVG avec l attribut viewBox
type: docs
weight: 190
url: /fr/java/export-chart-to-svg-with-viewbox-attribute/
---

Par défaut, lors de l'exportation du graphique au format SVG, l'attribut **viewBox** n'est pas inclus dans son XML. Cependant, Aspose.Cells fournit une propriété [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) qui, lorsqu'elle est définie sur **true**, exporte le graphique au format SVG avec l'attribut viewBox.

Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez l'attribut **viewBox** similaire à ceci.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Extrait de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Articles Connexes

- [Rendu du graphique](/cells/fr/java/chart-rendering/)
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
