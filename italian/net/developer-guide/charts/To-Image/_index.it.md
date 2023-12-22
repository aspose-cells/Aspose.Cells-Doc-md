---
title: Dal grafico all'immagine
description: Scopri come utilizzare Aspose.Cells for .NET per convertire un grafico in un formato immagine, ad esempio JPEG o PNG. La nostra guida mostrerà come esportare un grafico da Microsoft Excel e salvarlo come immagine autonoma per ulteriore utilizzo e manipolazione.
keywords: Aspose.Cells for .NET, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.
linktitle: Dal grafico all'immagine
type: docs
weight: 46
url: /it/net/chart-to-image/
---
##  **Grafici di rendering**

 Aspose.Cells Le API supportano la conversione dei grafici Excel in formati di immagini senza richiedere strumenti o applicazioni aggiuntivi. Per fornire supporto per il rendering, il file[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) la classe ha esposto[**Immaginare**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metodi con una varietà di sovraccarichi per soddisfare al meglio i requisiti dell'applicazione.

###  **Rendering di grafici in immagini**

 IL[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Il metodo ha una serie di sovraccarichi per supportare il rendering semplice e avanzato. Se il requisito dell'applicazione è visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il file[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)metodo come segue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 È anche possibile eseguire il rendering dei grafici in immagini con impostazioni avanzate. Aspose.Cells Le API hanno esposto una versione di sovraccarico di[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) metodo che potrebbe accettare un'istanza di[**OpzioniImmagineOrStampa**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)consentendo al tempo stesso di specificare parametri quali risoluzione, modalità di smussamento, formato immagine e così via.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Tipi di grafici supportati per il rendering**

 Esistono alcuni tipi di grafici che attualmente non sono supportati per il rendering. Tali tipi di grafici contengono**N** nel **Supportato** colonna della tabella sottostante.

|**Tipo di grafico**|**Sottotipo di grafico**|**Supportato**|
| :- | :- | :- |
|**Colonna**|Colonna|*S**|
| |Colonna in pila|*S**|
| |Colonna100PercentImpilata|*S**|
| |Colonna3DCraggruppata|*S**|
| |Colonna3DStacked|*S**|
| |Colonna3D100PercentImpilata|*S**|
| |Colonna3D|*S**|
|**Sbarra**|Sbarra|*S**|
| |Bar Stacked|*S**|
| |Bar100PercentImpilato|*S**|
| |Bar3DClustered|*S**|
| |Bar3DStacked|*S**|
| |Bar3D100PercentImpilato|*S**|
|**Linea**|Linea|*S**|
| |LineStacked|*S**|
| |Linea 100% in pila|*S**|
| |LineaConMarcatoriDati|*S**|
| |LineStackedWithDataMarkers|*S**|
| |Line100PercentStackedWithDataMarkers|*S**|
| |Linea3D|*S**|
|**Torta**|Torta|*S**|
| |Torta3D|*S**|
| |PiePie|*S**|
| |TortaEsplosa|*S**|
| |Pie3DEsploso|*S**|
| |PieBar|*S**|
|**Dispersione**|Dispersione|*S**|
| |ScatterConnectedByCurvesWithDataMarker|*S**|
| |ScatterConnectedByCurvesWithoutDataMarker|*S**|
| |ScatterConnectedByLinesWithDataMarker|*S**|
| |ScatterConnectedByLinesWithoutDataMarker|*S**|
|**La zona**|La zona|*S**|
| |AreaStacked|*S**|
| |Area100PercentImpilata|*S**|
| |Area3D|*S**|
| |Area3DStacked|*S**|
| |Area3D100PercentImpilata|*S**|
|**Ciambella**|Ciambella|*S**|
| |Ciambellaesploso|*S**|
|**Radar**|Radar|*S**|
| |RadarConDataMarkers|*S**|
| |Radarriempito|*S**|
|**Superficie**|Superficie3D|N|
| |SuperficieWireframe3D|N|
| |Contornosuperficie|N|
| |SurfaceContourWireframe|N|
|**Bolla**|Bolla|*S**|
| |Bubble3D|N|
|**Azione**|StockHighLowChiudi|*S**|
| |StockApriAltoBassoChiudi|*S**|
| |StockVolumeHighLowChiudi|*S**|
| |StockVolumeOpenHighLowClose|*S**|
|**Cilindro**|Cilindro|*S**|
| |Cilindro impilato|*S**|
| |Cilindro100%impilato|*S**|
| |Barra cilindrica|*S**|
| |Barra cilindrica impilata|*S**|
| |Barra cilindrica 100% impilata|*S**|
| |Colonna cilindrica3D|*S**|
|**Cono**|Cono|*S**|
| |Cono Stacked|*S**|
| |Cono100%impilato|*S**|
| |ConicalBar|*S**|
| |ConicalBarStacked|*S**|
| |ConicalBar100PercentStacked|*S**|
| |Colonna conica3D|*S**|
|**Piramide**|Piramide|*S**|
| |PyramidStacked|*S**|
| |Piramide100%Impilato|*S**|
| |PyramidBar|*S**|
| |PyramidBarStacked|*S**|
| |PyramidBar100PercentStacked|*S**|
| |PiramideColonna3D|*S**|
|**BoxBaffi**|BoxBaffi|Y|
|**Imbuto**|Imbuto|*S**|
|**Linea Pareto**|Linea Pareto|*S**|
|**Sprazzo di sole**|Sprazzo di sole|*S**|
|**Mappa ad albero**|Mappa ad albero|*S**|
|**Cascata**|Cascata|*S**|
|**Istogramma**|Istogramma|Y|
|**Carta geografica**|Carta geografica|*N**|

{{% alert color="primary" %}}

Nel caso in cui provi a eseguire il rendering dei tipi di grafico non supportati in immagine o PDF, potresti ritrovarti con immagini di dimensioni 0 o PDF vuoto.

{{% /alert %}}

##  **Argomenti avanzati**
- [Converti grafico in PDF](/cells/it/net/chart-to-pdf/)
