---
title: Diagramm nach SVG mit viewBox-Attribut exportieren
type: docs
weight: 190
url: /de/java/export-chart-to-svg-with-viewbox-attribute/
---
 Wenn das Diagramm in das Format SVG exportiert wird, wird standardmäßig die**viewBox** -Attribut ist nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) Eigenschaft, die, wenn festgelegt auf**wahr** Exportiert das Diagramm nach SVG mit dem viewBox-Attribut.

 Wenn Sie die SVG des Diagramms im Notizblock öffnen, finden Sie die**viewBox**ähnliches Attribut.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Code-Auszug

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Zum Thema passende Artikel

- [Diagrammdarstellung](/cells/de/java/chart-rendering/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
