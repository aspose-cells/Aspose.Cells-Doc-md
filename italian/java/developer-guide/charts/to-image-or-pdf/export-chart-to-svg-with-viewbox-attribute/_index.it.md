---
title: Esporta grafico a SVG con l'attributo viewBox
type: docs
weight: 190
url: /it/java/export-chart-to-svg-with-viewbox-attribute/
---
 Per impostazione predefinita, quando il grafico viene esportato nel formato SVG, il file**viewBox** l'attributo non è incluso nel suo XML. Tuttavia, Aspose.Cells fornisce[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) proprietà che quando impostata su**VERO** esporta il grafico in SVG con l'attributo viewBox.

 Se apri lo SVG del grafico nel blocco note, troverai il**viewBox**attributo simile a questo.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Frammento di codice

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## articoli Correlati

- [Rappresentazione del grafico](/cells/it/java/chart-rendering/)
- [Esporta foglio di lavoro o grafico in immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
