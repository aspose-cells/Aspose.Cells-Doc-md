---
title: Rappresentazione del grafico
type: docs
weight: 30
url: /it/cpp/chart-rendering/
---
## **Creazione di grafici**

Aspose.Cells Le API supportano la creazione di una verità di grafici Excel come dettagliato nell'argomento[Creazione e personalizzazione di grafici Excel](/cells/it/cpp/creating-and-customizing-charts/). Per dimostrare l'utilizzo delle API Aspose.Cells per il rendering dei grafici in formato immagine e PDF, creeremo un grafico di tipo Colonna come da seguente frammento.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **Grafici di rendering**

Le API Aspose.Cells supportano la conversione dei grafici Excel in immagini e formati PDF senza richiedere strumenti o applicazioni aggiuntivi. Per fornire il supporto per il rendering, la classe Chart ha esposto i metodi ToImage e ToPdf con una varietà di overload per soddisfare al meglio i requisiti dell'applicazione.

### **Rendering di grafici in immagini**

Il metodo Chart.toImage ha una verità di sovraccarichi per supportare il rendering semplice e avanzato. Se il requisito dell'applicazione è quello di rendere il grafico nelle sue dimensioni predefinite, ti suggeriamo di utilizzare il metodo Chart.toImage come segue.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Grafico di rendering a PDF**

Per eseguire il rendering del grafico nel formato PDF, le API Aspose.Cells hanno esposto il metodo Chart.ToPdf con la possibilità di memorizzare il risultante PDF nel percorso del disco o nello Stream.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Tipi di grafici supportati per il rendering**

Esistono alcuni tipi di grafici che attualmente non sono supportati per il rendering. Tali tipi di grafici contengono**Ni** nel**Supportato** colonna della tabella sottostante.

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
|Azione|MagazzinoAltoBassoChiudi|**S**|
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
