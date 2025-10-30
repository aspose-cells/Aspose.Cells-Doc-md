---
title: Diagram till Bild
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att konvertera ett diagram till ett bildformat, som JPEG eller PNG. Vår guide visar hur man exporterar ett diagram från Microsoft Excel och sparar det som en fristående bild för vidare användning och manipulation.
keywords: Aspose.Cells för Python via .NET, Diagram till bild, Microsoft Excel, Bildkonvertering, Export, Fristående bild.
linktitle: Diagram till Bild
type: docs
weight: 46
url: /sv/python-net/chart-to-image/
---

## **Rendering av diagram**

Aspose.Cells för Python via .NET API:er stödjer att konvertera Excel-diagram till bildformat utan att kräva ytterligare verktyg eller applikationer. För att möjliggöra rendering stöd har [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) klassen exponerade [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) metodgar med flera överlagrade versioner för att bäst passa applikationskraven.

### **Rendera diagram till bilder**

Metoden [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) har olika överbelastningar för att stödja enkel samt avancerad rendering. Om applikationskravet är att rendera diagrammet i dess standarddimensioner föreslår vi att du använder metoden [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) enligt följande.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

Det är också möjligt att rendera diagram till bilder med avancerade inställningar. Aspose.Cells för Python via .NET API:er har exponerade en överlagrad version av [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) metoden som kan ta emot en instans av [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), samtidigt som du kan specificera parametrar som upplösning, mjukhetsläge, bildformat och annat.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

## **Supportade diagramtyper för rendering**

Det finns några diagramtyper som för närvarande inte stöds för rendering. Sådana diagramtyper innehåller **N** i **Stöds** kolumnen i nedanstående tabell.

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
- [Konvertera Diagram till PDF](/cells/sv/python-net/chart-to-pdf/)
{{< app/cells/assistant language="python-net" >}}
