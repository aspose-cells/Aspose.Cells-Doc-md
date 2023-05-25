---
title: Da grafico a immagine
linktitle: Da grafico a immagine
type: docs
weight: 46
url: /it/net/chart-to-image/
---
##  **Grafici di rendering**

 Aspose.Cells Le API supportano la conversione dei grafici Excel in formati immagine senza richiedere strumenti o applicazioni aggiuntivi. Al fine di fornire supporto per il rendering, il[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) classe ha esposto[**Immaginare**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metodi con una verità di sovraccarichi per soddisfare al meglio i requisiti dell'applicazione.

###  **Rendering di grafici in immagini**

 IL[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Il metodo ha una verità di sovraccarichi per supportare il rendering semplice e avanzato. Se il requisito dell'applicazione è quello di visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il file[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)metodo come segue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 È anche possibile eseguire il rendering dei grafici in immagini con impostazioni avanzate. Aspose.Cells Le API hanno esposto una versione di sovraccarico di[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metodo che potrebbe accettare un'istanza di[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), pur consentendo di specificare parametri come risoluzione, modalità di smoothing, formato dell'immagine e così via.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Tipi di grafici supportati per il rendering**

 Esistono alcuni tipi di grafici che attualmente non sono supportati per il rendering. Tali tipi di grafici contengono**N** nel **Supportato** colonna della tabella sottostante.

|**Tipo di grafico**|**Sottotipo grafico**|**Supportato**|
| :- | :- | :- |
|**Colonna**|Colonna|*Y**|
| |ColonnaImpilato|*Y**|
| |Column100PercentStacked|*Y**|
| |Column3DClustered|*Y**|
| |Column3DStacked|*Y**|
| |Column3D100Percent Stacked|*Y**|
| |Colonna 3D|*Y**|
|**Sbarra**|Sbarra|*Y**|
| |Bar Stacked|*Y**|
| |Bar100Percent Stacked|*Y**|
| |Bar3DClustered|*Y**|
| |Bar3DSimpilato|*Y**|
| |Bar3D100Percent Stacked|*Y**|
|**Linea**|Linea|*Y**|
| |LineImpilato|*Y**|
| |Riga100Percent Stacked|*Y**|
| |LineWithDataMarkers|*Y**|
| |LineStackedWithDataMarkers|*Y**|
| |Line100PercentStackedWithDataMarkers|*Y**|
| |Linea3D|*Y**|
|**Torta**|Torta|*Y**|
| |Pie3D|*Y**|
| |PiePie|*Y**|
| |Torta Esplosa|*Y**|
| |Pie3DEsploso|*Y**|
| |PieBar|*Y**|
|**Disperdere**|Disperdere|*Y**|
| |ScatterConnectedByCurvesWithDataMarker|*Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|*Y**|
| |ScatterConnectedByLinesWithDataMarker|*Y**|
| |ScatterConnectedByLinesWithoutDataMarker|*Y**|
|**La zona**|La zona|*Y**|
| |Area Stacked|*Y**|
| |Area100Percent Stacked|*Y**|
| |Area3D|*Y**|
| |Area3DSimpilato|*Y**|
| |Area3D100Percent Stacked|*Y**|
|**Ciambella**|Ciambella|*Y**|
| |Ciambella Esploso|*Y**|
|**Radar**|Radar|*Y**|
| |RadarConMarcatoriDati|*Y**|
| |RadarRiempito|*Y**|
|**Superficie**|Superficie3D|N|
| |SuperficieWireframe3D|N|
| |SuperficieContorno|N|
| |SuperficieContornoWireframe|N|
|**Bolla**|Bolla|*Y**|
| |Bolla3D|N|
|**Azione**|MagazzinoAltoBassoChiudi|*Y**|
| |StockOpenHighLowClose|*Y**|
| |MagazzinoVolumeAltoBassoChiudi|*Y**|
| |MagazzinoVolumeApriAltoBassoChiudi|*Y**|
|**Cilindro**|Cilindro|*Y**|
| |CilindroImpilato|*Y**|
| |Cilindro impilato al 100%.|*Y**|
| |Barra cilindrica|*Y**|
| |Barra Cilindrica Impilata|*Y**|
| |Barra cilindrica100% impilata|*Y**|
| |Colonna cilindrica 3D|*Y**|
|**Cono**|Cono|*Y**|
| |ConoImpilato|*Y**|
| |Cono100Percent Stacked|*Y**|
| |Barra conica|*Y**|
| |ConicalBarImpilato|*Y**|
| |ConicalBar100PercentStacked|*Y**|
| |Colonna conica 3D|*Y**|
|**Piramide**|Piramide|*Y**|
| |Piramide Impilata|*Y**|
| |Pyramid100Percent Stacked|*Y**|
| |PyramidBar|*Y**|
| |PyramidBar Impilato|*Y**|
| |PyramidBar100Percent Stacked|*Y**|
| |Piramide Colonna 3D|*Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Imbuto**|Imbuto|*Y**|
|**Linea di Pareto**|Linea di Pareto|*Y**|
|**Sprazzo di sole**|Sprazzo di sole|*Y**|
|**Mappa ad albero**|Mappa ad albero|*Y**|
|**Cascata**|Cascata|*Y**|
|**Istogramma**|Istogramma|Y|
|**Carta geografica**|Carta geografica|*N**|

{{% alert color="primary" %}}

Nel caso in cui provi a eseguire il rendering dei tipi di grafico non supportati su image o PDF, potresti ritrovarti con immagini di dimensione 0 o PDF vuoto.

{{% /alert %}}

##  **Argomenti avanzati**
- [Converti grafico in PDF](/cells/it/net/chart-to-pdf/)
