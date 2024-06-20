---
title: Diagramrendering
linktitle: Till bild eller PDF
type: docs
weight: 40
url: /sv/java/chart-rendering/
---

## **Skapa diagram**

Aspose.Cells API:er stödjer att skapa en mängd olika Excel-diagram som detaljeras under ämnet [Skapa och anpassa Excel-diagram](/cells/sv/java/creating-and-customizing-charts/). För att demonstrera användningen av Aspose.Cells API:er för att rendera diagram i bild- och PDF-format, kommer vi att skapa ett stapeldiagram enligt följande kodsnutt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Rendering av diagram**

Aspose.Cells API:er stödjer att konvertera Excel-diagram till bilder och PDF-format utan att kräva några ytterligare verktyg eller program. För att erbjuda renderingsstöd, har [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-klassen exponerat [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))- och [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream))-metoder med en mängd olika överbelastningar för att bäst passa applikationskraven.

### **Rendera diagram till bilder**

[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-metoden har en mängd olika överbelastningar för att stödja enkel såväl som avancerad rendering. Om applikationskravet är att rendera diagrammet i dess standarddimensioner rekommenderar vi att du använder [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-metoden enligt följande.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Det är också möjligt att rendera diagram till bilder med avancerade inställningar. Aspose.Cells API:er har exponerat en överbelastningsversion av [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-metoden som kan acceptera en instans av [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) samtidigt som du kan specificera parametrar som upplösning, renderingstips, bildformat och så vidare.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Rendera diagram till PDF**

För att rendera diagrammet till PDF-format har Aspose.Cells API:er exponerat [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream))-metoden med förmågan att lagra det resulterande PDF på diskvägen eller en instans av OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Supportade diagramtyper för rendering**

Det finns några diagramtyper som för närvarande inte stöds för rendering. Sådana diagramtyper innehåller **N** i kolumnen **Stöd** i nedanstående tabell.

|**Diagramtyp**|**Diagramundertyp**|**Stöd**|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

Om du försöker rendera de icke-supportade diagramtyperna till bild eller PDF kan du sluta med bilder som är 0 i storlek eller blanka PDF:er.

{{% /alert %}}


## **Fortsatta ämnen**
- [Konvertera diagram till bild i SVG-format](/cells/sv/java/converting-chart-to-image-in-svg-format/)
- [Skapa diagram-PDF med önskad sidstorlek](/cells/sv/java/create-chart-pdf-with-desired-page-size/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/java/export-chart-to-svg-with-viewbox-attribute/)
