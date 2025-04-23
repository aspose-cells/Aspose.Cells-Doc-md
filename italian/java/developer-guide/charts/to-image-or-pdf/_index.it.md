---
title: Rendering del grafico
linktitle: In immagine o PDF
type: docs
weight: 40
url: /it/java/chart-rendering/
---

## **Creazione di grafici**

Le API di Aspose.Cells supportano la creazione di una varieta di grafici di Excel come dettagliato nell'argomento [Creazione e personalizzazione dei grafici di Excel](/cells/it/java/creating-and-customizing-charts/). Al fine di dimostrare l'utilizzo delle API di Aspose.Cells per rendere i grafici in formato immagine e PDF, creeremo un grafico di tipo Colonna come nel seguente frammento di codice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Rendering di grafici**

Le API di Aspose.Cells supportano la conversione dei grafici di Excel in immagini e formati PDF senza richiedere alcun altro strumento o applicazione aggiuntiva. Al fine di fornire supporto per il rendering, la classe [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) ha esposto i metodi [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) & [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) con una varietà di sovraccarichi per soddisfare al meglio le esigenze dell'applicazione.

### **Rendering di grafici in immagini**

Il metodo [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) ha una varietà di sovraccarichi per supportare un rendering semplice e avanzato. Se il requisito dell'applicazione è di rendere il grafico nelle sue dimensioni predefinite, ti consigliamo di utilizzare il metodo [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) come segue.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

È anche possibile rendere i grafici in immagini con impostazioni avanzate. Le API di Aspose.Cells hanno esposto una versione sovrasatura del metodo [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) che potrebbe accettare un'istanza di [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) consentendo di specificare parametri come risoluzione, suggerimenti per il rendering, formato dell'immagine e così via.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Rendering del grafico in PDF**

Al fine di rendere il grafico in formato PDF, le API di Aspose.Cells hanno esposto il metodo [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) con la capacità di memorizzare il PDF risultante nel percorso disco o in un'istanza di OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

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
- [Conversione del grafico in Immagine in formato SVG](/cells/it/java/converting-chart-to-image-in-svg-format/)
- [Crea Grafico PDF con Dimensione Pagina Desiderata](/cells/it/java/create-chart-pdf-with-desired-page-size/)
- [Esportare il grafico in SVG con attributo viewBox](/cells/it/java/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="java" >}}
