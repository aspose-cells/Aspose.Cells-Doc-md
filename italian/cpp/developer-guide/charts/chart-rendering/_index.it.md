---
title: Rappresentazione del grafico
type: docs
weight: 30
url: /it/cpp/chart-rendering/
---
##  **Creazione di grafici**

Aspose.Cells Supporto API per creare una verità di grafici Excel come dettagliato nell'argomento[Creazione e personalizzazione di grafici Excel](/cells/it/cpp/creating-and-customizing-charts/). Per dimostrare l'utilizzo delle API Aspose.Cells per eseguire il rendering dei grafici nel formato immagine e PDF, creeremo un grafico di tipo Colonna come indicato nel seguente snippet.

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **Grafici di rendering**

Le API Aspose.Cells supportano la conversione dei grafici Excel in immagini e formati PDF senza richiedere strumenti o applicazioni aggiuntivi. Per fornire il supporto al rendering, la classe Chart ha esposto i metodi ToImage e ToPdf con una serie di sovraccarichi per soddisfare al meglio i requisiti dell'applicazione.

###  **Rendering di grafici in immagini**

Il metodo Chart.toImage dispone di una serie di sovraccarichi per supportare il rendering semplice e avanzato. Se il requisito dell'applicazione è visualizzare il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il metodo Chart.toImage come segue.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **Grafico di rendering allo PDF**

Per eseguire il rendering del grafico nel formato PDF, le API Aspose.Cells hanno esposto il metodo Chart.ToPdf con la possibilità di memorizzare il risultante PDF sul percorso del disco o sul flusso.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **Tipi di grafici supportati per il rendering**

Esistono alcuni tipi di grafici che attualmente non sono supportati per il rendering. Tali tipi di grafici contengono**N** nel **Supportato**colonna della tabella sottostante.

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
|Azione|StockHighLowChiudi|*S**|
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
