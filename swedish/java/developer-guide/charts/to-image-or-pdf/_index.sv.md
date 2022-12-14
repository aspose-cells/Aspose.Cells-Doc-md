---
title: Diagramrendering
linktitle: Till bild eller pdf
type: docs
weight: 40
url: /sv/java/chart-rendering/
---
## **Skapa diagram**

 Aspose.Cells API:er stöder för att skapa en mängd Excel-diagram som beskrivs under ämnet[Skapa och anpassa Excel-diagram](/cells/sv/java/creating-and-customizing-charts/)För att demonstrera användningen av Aspose.Cells API:er för att rendera diagrammen i bild- och PDF-format, kommer vi att skapa ett diagram av typen Kolumn enligt följande utdrag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Återgivning av diagram**

 Aspose.Cells API:er stöder för att konvertera Excel-diagram till bilder och PDF-format utan att behöva några ytterligare verktyg eller applikationer. För att ge renderingsstöd,[**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)klass har avslöjat[**att föreställa sig**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**till pdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) metoder med en sanning av överbelastningar för att bäst passa applikationskraven.

### **Återge diagram till bilder**

 De[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-metoden har en sanning av överbelastningar för att stödja enkel såväl som avancerad rendering. Om applikationskravet är att återge diagrammet i dess standarddimensioner, föreslår vi att du använder[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) metod enligt följande.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Det är också möjligt att rendera diagrammen till bilder med avancerade inställningar. Aspose.Cells API:er har avslöjat en överbelastningsversion av[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) metod som skulle kunna acceptera en instans av[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)samtidigt som man tillåter att ange parametrar som upplösning, renderingstips, bildformat och så vidare.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Återge diagram till PDF**

 För att rendera diagrammet till PDF-format har API:erna Aspose.Cells avslöjat[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) metod med möjlighet att lagra den resulterande PDF-filen på skivväg eller en instans av OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Sjökortstyper som stöds för rendering**

 Det finns några diagramtyper som för närvarande inte stöds för rendering. Sådana diagramtyper innehåller** N** i**Stöds** kolumn i tabellen nedan.

|**Diagramtyp**|**Diagram undertyp**|**Stöds**|
|:- |:- |:- |
|**Kolumn**|Kolumn|**Y**|
||KolumnStackad|**Y**|
||Kolumn100ProcentStackad|**Y**|
||Kolumn3DClustrerad|**Y**|
||Kolumn3DStackad|**Y**|
||Kolumn3D100PercentStacked|**Y**|
||Kolumn 3D|**Y**|
|**Bar**|Bar|**Y**|
||BarStacked|**Y**|
||Bar100PercentStacked|**Y**|
||Bar3DClustered|**Y**|
||Bar3DStacked|**Y**|
||Bar3D100PercentStacked|**Y**|
|**Linje**|Linje|**Y**|
||LineStacked|**Y**|
||Line100PercentStacked|**Y**|
||LineWithDataMarkers|**Y**|
||LineStackedWithDataMarkers|**Y**|
||Line100PercentStackedWithDataMarkers|**Y**|
||Line3D|**Y**|
|**Paj**|Paj|**Y**|
||Pie3D|**Y**|
||PiePie|**Y**|
||PieExploderade|**Y**|
||Pie3DE exploderade|**Y**|
||PieBar|**Y**|
|**Sprida ut**|Sprida ut|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||ScatterConnectedByCurvesWithoutDataMarker|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Område**|Område|**Y**|
||AreaStacked|**Y**|
||Area100PercentStacked|**Y**|
||Area3D|**Y**|
||Area3DStacked|**Y**|
||Area3D100PercentStacked|**Y**|
|**Munk**|Munk|**Y**|
||Doughnut Exploderade|**Y**|
|**Radar**|Radar|**Y**|
||RadarWithDataMarkers|**Y**|
||Radarfylld|**Y**|
|**Yta**|Surface3D|N|
||SurfaceWireframe3D|N|
||Ytkontur|N|
||SurfaceContourWireframe|N|
|**Bubbla**|Bubbla|**Y**|
||Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
||LagerÖppnaHögLågStäng|**Y**|
||LagervolymHögLågStäng|**Y**|
||Lagervolym ÖppenHögLågStäng|**Y**|
|**Cylinder**|Cylinder|**Y**|
||CylinderStacked|**Y**|
||Cylinder100PercentStacked|**Y**|
||Cylindrical Bar|**Y**|
||CylindricalBarStacked|**Y**|
||CylindricalBar100PercentStacked|**Y**|
||CylindricalColumn3D|**Y**|
|**Kon**|Kon|**Y**|
||ConeStacked|**Y**|
||Cone100PercentStacked|**Y**|
||ConicalBar|**Y**|
||ConicalBarStacked|**Y**|
||ConicalBar100PercentStacked|**Y**|
||Konisk kolumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
||PyramidStackad|**Y**|
||Pyramid100ProcentStacked|**Y**|
||PyramidBar|**Y**|
||PyramidBarStacked|**Y**|
||PyramidBar100PercentStacked|**Y**|
||PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Tratt**|Tratt|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Trädkarta**|Trädkarta|**Y**|
|**Vattenfall**|Vattenfall|**Y**|
|**Histogram**|Histogram|Y|
|**Karta**|Karta|**N**|

{{% alert color="primary" %}}

Om du försöker rendera diagramtyperna som inte stöds till bild eller PDF, kan du sluta med 0-stora bilder eller tom PDF.

{{% /alert %}}


## **Förhandsämnen**
- [Konvertera diagram till bild i SVG-format](/cells/sv/java/converting-chart-to-image-in-svg-format/)
- [Skapa diagram PDF med önskad sidstorlek](/cells/sv/java/create-chart-pdf-with-desired-page-size/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/java/export-chart-to-svg-with-viewbox-attribute/)
