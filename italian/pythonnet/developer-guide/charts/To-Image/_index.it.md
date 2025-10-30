---
title: Grafico in Immagine
description: Impara come usare Aspose.Cells per Python via .NET per convertire un grafico in un formato immagine, come JPEG o PNG. La nostra guida dimostrerà come esportare un grafico da Microsoft Excel e salvarlo come immagine autonoma per un uso e manipolazione successivi.
keywords: Aspose.Cells per Python via .NET, Grafico in Immagine, Microsoft Excel, Conversione Immagine, Esportazione, Immagine Autonoma.
linktitle: Grafico in Immagine
type: docs
weight: 46
url: /it/python-net/chart-to-image/
---

## **Rendering di grafici**

Le API di Aspose.Cells per Python via .NET supportano la conversione dei Grafici Excel in formati immagine senza richiedere strumenti o applicazioni aggiuntive. Per fornire supporto di rendering, la classe [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) ha esposto i metodi [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) con una varietà di sovraccarichi per adattarsi meglio ai requisiti dell'applicazione.

### **Rendering di grafici in immagini**

Il metodo [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) ha una varietà di sovraccarichi per supportare sia il rendering semplice che avanzato. Se il requisito dell'applicazione è quello di visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il metodo [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) come segue.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

È anche possibile rendere i grafici in immagini con impostazioni avanzate. Le API di Aspose.Cells per Python via .NET hanno esposto una versione sovraccaricata del metodo [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) che può accettare un'istanza di [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), consentendo di specificare parametri come risoluzione, modalità di levigatura, formato immagine e altro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

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
- [Converti grafico in PDF](/cells/it/python-net/chart-to-pdf/)
{{< app/cells/assistant language="python-net" >}}
