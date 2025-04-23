---
title: Grafico in Immagine
description: Scopri come utilizzare Aspose.Cells for .NET per convertire un grafico in un formato di immagine, come JPEG o PNG. La nostra guida mostrerà come esportare un grafico da Microsoft Excel e salvarlo come immagine autonoma per ulteriori utilizzi e manipolazioni.
keywords: Aspose.Cells for .NET, Grafico in Immagine, Microsoft Excel, Conversione di Immagini, Esportazione, Immagine Autonoma.
linktitle: Grafico in Immagine
type: docs
weight: 46
url: /it/net/chart-to-image/
---

## **Rendering di grafici**

Le API di Aspose.Cells supportano la conversione dei grafici di Excel in formati di immagine senza richiedere strumenti o applicazioni aggiuntive. Al fine di fornire supporto alla visualizzazione, la classe [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) ha esposto [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metodi con una varietà di sovraccarichi per soddisfare al meglio i requisiti dell'applicazione.

### **Rendering di grafici in immagini**

Il metodo [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) ha una varietà di sovraccarichi per supportare sia il rendering semplice che avanzato. Se il requisito dell'applicazione è quello di visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il metodo [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) come segue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

È anche possibile renderizzare i grafici in immagini con impostazioni avanzate. Le API di Aspose.Cells hanno esposto una versione sovraccaricata del metodo [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) che potrebbe accettare un'istanza di [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), consentendo di specificare parametri come risoluzione, modalità di smussatura, formato dell'immagine e così via.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **Tipi di grafico supportati per il rendering**

Ci sono alcuni tipi di grafico attualmente non supportati per il rendering. Tali tipi di grafico contengono **N** nella colonna **Supportato** della tabella sottostante.

|**Tipo grafico**|**Sottotipo grafico**|**Supportato**|
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

Nel caso in cui si tenti di rendere i tipi di grafico non supportati in immagine o PDF, si potrebbe ottenere immagini di dimensioni 0 o PDF vuoti.

{{% /alert %}}

## **Argomenti avanzati**
- [Converti grafico in PDF](/cells/it/net/chart-to-pdf/)
{{< app/cells/assistant language="csharp" >}}
