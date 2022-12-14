---
title: Rappresentazione del grafico
linktitle: Per immagine o Pdf
type: docs
weight: 40
url: /it/java/chart-rendering/
---
## **Creazione di grafici**

 Aspose.Cells Le API supportano la creazione di una verità di grafici Excel come dettagliato nell'argomento[Creazione e personalizzazione di grafici Excel](/cells/it/java/creating-and-customizing-charts/)Per dimostrare l'utilizzo delle API Aspose.Cells per il rendering dei grafici in formato immagine e PDF, creeremo un grafico di tipo Colonna come da seguente frammento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Grafici di rendering**

 Aspose.Cells Le API supportano la conversione dei grafici Excel in immagini e formati PDF senza richiedere strumenti o applicazioni aggiuntivi. Al fine di fornire supporto per il rendering, il[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)classe ha esposto[**immaginare**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) metodi con una verità di sovraccarichi per soddisfare al meglio i requisiti dell'applicazione.

### **Rendering di grafici in immagini**

 Il[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) ha una verità di sovraccarichi per supportare il rendering semplice e avanzato. Se il requisito dell'applicazione è quello di visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il file[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) metodo come segue.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

È anche possibile eseguire il rendering dei grafici in immagini con impostazioni avanzate. Aspose.Cells Le API hanno esposto una versione di sovraccarico di[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) metodo che potrebbe accettare un'istanza di[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)pur consentendo di specificare parametri come risoluzione, suggerimenti di rendering, formato immagine e così via.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Rendering del grafico in PDF**

 Per eseguire il rendering del grafico in formato PDF, le API Aspose.Cells hanno esposto il file[**Grafico.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) con la possibilità di archiviare il PDF risultante nel percorso del disco o in un'istanza di OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Tipi di grafici supportati per il rendering**

 Esistono alcuni tipi di grafici che attualmente non sono supportati per il rendering. Tali tipi di grafici contengono** Ni** nel**Supportato** colonna della tabella sottostante.

|**Tipo di grafico**|**Sottotipo grafico**|**Supportato**|
|:- |:- |:- |
|**Colonna**|Colonna|**S**|
||ColonnaImpilato|**S**|
||Column100PercentStacked|**S**|
||Column3DClustered|**S**|
||Column3DStacked|**S**|
||Column3D100Percent Stacked|**S**|
||Colonna 3D|**S**|
|**Sbarra**|Sbarra|**S**|
||Bar Stacked|**S**|
||Bar100Percent Stacked|**S**|
||Bar3DClustered|**S**|
||Bar3DSimpilato|**S**|
||Bar3D100Percent Stacked|**S**|
|**Linea**|Linea|**S**|
||LineImpilato|**S**|
||Riga100Percent Stacked|**S**|
||LineWithDataMarkers|**S**|
||LineStackedWithDataMarkers|**S**|
||Line100PercentStackedWithDataMarkers|**S**|
||Linea3D|**S**|
|**Torta**|Torta|**S**|
||Pie3D|**S**|
||PiePie|**S**|
||Torta Esplosa|**S**|
||Pie3DEsploso|**S**|
||PieBar|**S**|
|**Disperdere**|Disperdere|**S**|
||ScatterConnectedByCurvesWithDataMarker|**S**|
||ScatterConnectedByCurvesWithoutDataMarker|**S**|
||ScatterConnectedByLinesWithDataMarker|**S**|
||ScatterConnectedByLinesWithoutDataMarker|**S**|
|**La zona**|La zona|**S**|
||Area Stacked|**S**|
||Area100Percent Stacked|**S**|
||Area3D|**S**|
||Area3DSimpilato|**S**|
||Area3D100Percentuale impilata|**S**|
|**Ciambella**|Ciambella|**S**|
||Ciambella Esploso|**S**|
|**Radar**|Radar|**S**|
||RadarConMarcatoriDati|**S**|
||RadarRiempito|**S**|
|**Superficie**|Superficie3D|N|
||SuperficieWireframe3D|N|
||SuperficieContorno|N|
||SuperficieContornoWireframe|N|
|**Bolla**|Bolla|**S**|
||Bolla3D|N|
|**Azione**|MagazzinoAltoBassoChiudi|**S**|
||StockOpenHighLowClose|**S**|
||MagazzinoVolumeAltoBassoChiudi|**S**|
||MagazzinoVolumeApriAltoBassoChiudi|**S**|
|**Cilindro**|Cilindro|**S**|
||CilindroImpilato|**S**|
||Cilindro impilato al 100%.|**S**|
||Barra cilindrica|**S**|
||Barra Cilindrica Impilata|**S**|
||Barra cilindrica100% impilata|**S**|
||Colonna cilindrica 3D|**S**|
|**Cono**|Cono|**S**|
||ConoImpilato|**S**|
||Cono100Percent Stacked|**S**|
||Barra conica|**S**|
||ConicalBarImpilato|**S**|
||ConicalBar100PercentStacked|**S**|
||Colonna conica 3D|**S**|
|**Piramide**|Piramide|**S**|
||Piramide Impilata|**S**|
||Pyramid100Percent Stacked|**S**|
||PyramidBar|**S**|
||PyramidBar Impilato|**S**|
||PyramidBar100Percent Stacked|**S**|
||Piramide Colonna 3D|**S**|
|**BoxWhisker**|BoxWhisker|Y|
|**Imbuto**|Imbuto|**S**|
|**Linea di Pareto**|Linea di Pareto|**S**|
|**Sprazzo di sole**|Sprazzo di sole|**S**|
|**Mappa ad albero**|Mappa ad albero|**S**|
|**Cascata**|Cascata|**S**|
|**Istogramma**|Istogramma|Y|
|**Carta geografica**|Carta geografica|**N**|

{{% alert color="primary" %}}

Nel caso in cui provi a eseguire il rendering dei tipi di grafico non supportati in immagine o PDF, potresti ritrovarti con immagini di dimensioni 0 o PDF vuoto.

{{% /alert %}}


## **Argomenti avanzati**
- [Conversione del grafico in immagine in formato SVG](/cells/it/java/converting-chart-to-image-in-svg-format/)
- [Crea grafico PDF con dimensione pagina desiderata](/cells/it/java/create-chart-pdf-with-desired-page-size/)
- [Esporta il grafico in SVG con l'attributo viewBox](/cells/it/java/export-chart-to-svg-with-viewbox-attribute/)
