---
title: Esporta il grafico in SVG con attributo viewBox
type: docs
weight: 190
url: /it/java/export-chart-to-svg-with-viewbox-attribute/
---

Per impostazione predefinita, quando il grafico viene esportato in formato SVG, l'attributo **viewBox** non è incluso nel suo XML. Tuttavia, Aspose.Cells fornisce la proprietà [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) che, quando impostata su **true**, esporta il grafico in SVG con l'attributo viewBox.

Se apri l'SVG del grafico in notepad, troverai l'attributo **viewBox** simile a questo.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Estratto del Codice

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Articoli correlati

- [Rendering del grafico](/cells/it/java/chart-rendering/)
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
