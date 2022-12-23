---
title: Rappresentazione del grafico
linktitle: Per immagine o Pdf
type: docs
weight: 45
url: /it/net/chart-rendering/
---
## **Grafici di rendering**

 Le API Aspose.Cells supportano la conversione dei grafici Excel in immagini e formati PDF senza richiedere strumenti o applicazioni aggiuntivi. Al fine di fornire supporto per il rendering, il[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) classe ha esposto[**Immaginare**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)metodi con una verità di sovraccarichi per soddisfare al meglio i requisiti dell'applicazione.

### **Rendering di grafici in immagini**

 Il[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) Il metodo ha una verità di sovraccarichi per supportare il rendering semplice e avanzato. Se il requisito dell'applicazione è quello di visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il file[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)metodo come segue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 È anche possibile eseguire il rendering dei grafici in immagini con impostazioni avanzate. Aspose.Cells Le API hanno esposto una versione di sovraccarico di[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metodo che potrebbe accettare un'istanza di[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), pur consentendo di specificare parametri come risoluzione, modalità di smoothing, formato dell'immagine e così via.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Grafico di rendering a PDF**

 Per eseguire il rendering del grafico nel formato PDF, le API Aspose.Cells hanno esposto il[**Grafico.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)metodo con la possibilità di memorizzare il risultante PDF sul percorso del disco o Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Tipi di grafici supportati per il rendering**

 Esistono alcuni tipi di grafici che attualmente non sono supportati per il rendering. Tali tipi di grafici contengono** Ni** nel**Colonna Supportato** della tabella sottostante.

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

Nel caso in cui provi a eseguire il rendering dei tipi di grafico non supportati su image o PDF, potresti ritrovarti con immagini di dimensione 0 o PDF vuoto.

{{% /alert %}}

## **Argomenti avanzati**
- [Converti il grafico in PDF con la dimensione della pagina desiderata](/cells/it/net/chart-to-pdf/)
