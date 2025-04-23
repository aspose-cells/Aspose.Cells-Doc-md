---
title: Exportera diagram till SVG med viewBox attribut
type: docs
weight: 190
url: /sv/java/export-chart-to-svg-with-viewbox-attribute/
---

Som standard, när diagrammet exporteras till SVG-format, ingår inte attributet **viewBox** i XML. Aspose.Cells tillhandahåller dock [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) egenskap som när den är inställd på **true** exporterar diagrammet till SVG med viewBox-attributet.

Om du öppnar diagrammets SVG i anteckningar kommer du att hitta **viewBox** -attributet som liknar detta.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## Kodsparandel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## Relaterade artiklar

- [Diagramrendering](/cells/sv/java/chart-rendering/)
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
