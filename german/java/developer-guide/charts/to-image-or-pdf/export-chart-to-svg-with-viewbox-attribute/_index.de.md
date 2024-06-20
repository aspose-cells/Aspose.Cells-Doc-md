---
title: Diagramm als SVG mit viewBox Attribut exportieren
type: docs
weight: 190
url: /de/java/export-chart-to-svg-with-viewbox-attribute/
---

Standardmäßig wird bei der Exportierung des Diagramms in das SVG-Format das **viewBox**-Attribut nicht in seinem XML eingeschlossen. Allerdings bietet Aspose.Cells die [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort)-Eigenschaft, die, wenn auf **true** gesetzt, das Diagramm als SVG mit dem viewBox-Attribut exportiert.

Wenn Sie das SVG des Diagramms in Notepad öffnen, finden Sie das **viewBox**-Attribut ähnlich wie dieses.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Code-Snippet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Verwandte Artikel

- [Diagrammrendering](/cells/de/java/chart-rendering/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
