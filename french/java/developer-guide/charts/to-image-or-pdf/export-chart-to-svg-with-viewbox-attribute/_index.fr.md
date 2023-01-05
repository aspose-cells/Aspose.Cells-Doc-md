---
title: Exporter le graphique vers SVG avec l'attribut viewBox
type: docs
weight: 190
url: /fr/java/export-chart-to-svg-with-viewbox-attribute/
---
 Par défaut, lorsque le graphique est exporté au format SVG, le**viewBox** L'attribut n'est pas inclus dans son XML. Cependant, Aspose.Cells fournit[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) propriété qui, lorsqu'elle est définie sur**vrai** exporte le graphique vers SVG avec l'attribut viewBox.

 Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez le**viewBox**attribut similaire à celui-ci.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Extrait de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Articles Liés

- [Rendu graphique](/cells/fr/java/chart-rendering/)
- [Exporter une feuille de calcul ou un graphique dans une image avec la largeur et la hauteur souhaitées](/cells/fr/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
