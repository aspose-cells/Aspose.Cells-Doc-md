---
title: Diagramrendering
linktitle: Till bild eller pdf
type: docs
weight: 45
url: /sv/net/chart-rendering/
---
## **Återgivning av diagram**

 Aspose.Cells API:er stöder för att konvertera Excel-diagram till bilder och PDF-format utan att behöva några ytterligare verktyg eller applikationer. För att ge renderingsstöd,[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) klass har avslöjat[**Att föreställa sig**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**Till pdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)metoder med en sanning av överbelastningar för att bäst passa applikationskraven.

### **Återge diagram till bilder**

 De[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**Till pdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) Metoden har en sanning av överbelastningar för att stödja enkel såväl som avancerad rendering. Om applikationskravet är att återge diagrammet i dess standarddimensioner, föreslår vi att du använder[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)metod enligt följande.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Det är också möjligt att rendera diagrammen till bilder med avancerade inställningar. Aspose.Cells API:er har avslöjat en överbelastningsversion av[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metod som skulle kunna acceptera en instans av[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), samtidigt som du tillåter att ange parametrar som upplösning, utjämningsläge, bildformat och så vidare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Återge diagram till PDF**

 För att rendera diagrammet till PDF-format har API:erna Aspose.Cells avslöjat[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)metod med möjligheten att lagra den resulterande PDF-filen på skivväg eller Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

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
- [Konvertera diagram till PDF med önskad sidstorlek](/cells/sv/net/chart-to-pdf/)
