---
title: Converti i grafici in immagini
type: docs
weight: 10
url: /it/net/convert-charts-to-images/
---
**Grafici**sono visivamente accattivanti e consentono agli utenti di vedere facilmente confronti, modelli e tendenze nei dati. Ad esempio, invece di dover analizzare diverse colonne di numeri del foglio di lavoro, puoi vedere a colpo d'occhio se le vendite sono in calo o in aumento su periodi trimestrali o come le vendite effettive si confrontano con le vendite previste. A volte, è necessario presentare il grafico nelle vostre applicazioni o pagine web. Potrebbe essere necessario inserirlo in un documento Word, un file PDF, una presentazione in Power Point o in qualche altro scenario. Semplicemente vuoi che il grafico venga visualizzato come un'immagine, in modo da poterlo incollare facilmente nelle tue applicazioni. Una foto vale la pena. Spesso, nel corso del lavoro, è necessario presentare informazioni statistiche e grafiche in un modo facile da capire e da mantenere. Si potrebbe provare l'automazione dell'ufficio, ma l'automazione dell'ufficio ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio, sicurezza, stabilità, scalabilità/velocità, prezzo, funzionalità ecc. automazione lato server di Office. Esiste un'altra opzione che è possibile utilizzare per convertire un grafico Excel in un'immagine utilizzando**Aspose.Cells**.
## **Conversione del grafico in EMF**
{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by

//passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a sample value to "A1" cell

worksheet.Cells["A1"].PutValue(50);

//Adding a sample value to "A2" cell

worksheet.Cells["A2"].PutValue(100);

//Adding a sample value to "A3" cell

worksheet.Cells["A3"].PutValue(150);

//Adding a sample value to "B1" cell

worksheet.Cells["B1"].PutValue(4);

//Adding a sample value to "B2" cell

worksheet.Cells["B2"].PutValue(20);

//Adding a sample value to "B3" cell

worksheet.Cells["B3"].PutValue(50);

//Adding a chart to the worksheet

int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);

//Accessing the instance of the newly added chart

Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"

chart.NSeries.Add("A1:B3", true);

//Converting chart to image.

chart.ToImage(MyDir + "Chart to EMF Image.Emf", System.Drawing.Imaging.ImageFormat.Emf);


{{< /highlight >}}
## **Conversione del grafico in BMP**
{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by

//passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a sample value to "A1" cell

worksheet.Cells["A1"].PutValue(50);

//Adding a sample value to "A2" cell

worksheet.Cells["A2"].PutValue(100);

//Adding a sample value to "A3" cell

worksheet.Cells["A3"].PutValue(150);

//Adding a sample value to "B1" cell

worksheet.Cells["B1"].PutValue(4);

//Adding a sample value to "B2" cell

worksheet.Cells["B2"].PutValue(20);

//Adding a sample value to "B3" cell

worksheet.Cells["B3"].PutValue(50);

//Adding a chart to the worksheet

int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);

//Accessing the instance of the newly added chart

Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"

chart.NSeries.Add("A1:B3", true);

//Converting chart to image.

chart.ToImage(MyDir + "Chart to BMP Image.Bmp", System.Drawing.Imaging.ImageFormat.Bmp);

{{< /highlight >}}
## **Conversione del grafico in JPEG**
{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by

//passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a sample value to "A1" cell

worksheet.Cells["A1"].PutValue(50);

//Adding a sample value to "A2" cell

worksheet.Cells["A2"].PutValue(100);

//Adding a sample value to "A3" cell

worksheet.Cells["A3"].PutValue(150);

//Adding a sample value to "B1" cell

worksheet.Cells["B1"].PutValue(4);

//Adding a sample value to "B2" cell

worksheet.Cells["B2"].PutValue(20);

//Adding a sample value to "B3" cell

worksheet.Cells["B3"].PutValue(50);

//Adding a chart to the worksheet

int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);

//Accessing the instance of the newly added chart

Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"

chart.NSeries.Add("A1:B3", true);

//Converting chart to image.

chart.ToImage(MyDir + "Chart to JPEG Image.Jpeg", System.Drawing.Imaging.ImageFormat.Jpeg);


{{< /highlight >}}
## **Conversione del grafico in PNG**
{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by

//passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a sample value to "A1" cell

worksheet.Cells["A1"].PutValue(50);

//Adding a sample value to "A2" cell

worksheet.Cells["A2"].PutValue(100);

//Adding a sample value to "A3" cell

worksheet.Cells["A3"].PutValue(150);

//Adding a sample value to "B1" cell

worksheet.Cells["B1"].PutValue(4);

//Adding a sample value to "B2" cell

worksheet.Cells["B2"].PutValue(20);

//Adding a sample value to "B3" cell

worksheet.Cells["B3"].PutValue(50);

//Adding a chart to the worksheet

int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);

//Accessing the instance of the newly added chart

Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"

chart.NSeries.Add("A1:B3", true);

//Converting chart to image.

chart.ToImage(MyDir + "Chart to PNG Image.Png", System.Drawing.Imaging.ImageFormat.Png);


{{< /highlight >}}
## **Conversione del grafico in TIFF**
{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by

//passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a sample value to "A1" cell

worksheet.Cells["A1"].PutValue(50);

//Adding a sample value to "A2" cell

worksheet.Cells["A2"].PutValue(100);

//Adding a sample value to "A3" cell

worksheet.Cells["A3"].PutValue(150);

//Adding a sample value to "B1" cell

worksheet.Cells["B1"].PutValue(4);

//Adding a sample value to "B2" cell

worksheet.Cells["B2"].PutValue(20);

//Adding a sample value to "B3" cell

worksheet.Cells["B3"].PutValue(50);

//Adding a chart to the worksheet

int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);

//Accessing the instance of the newly added chart

Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"

chart.NSeries.Add("A1:B3", true);

//Converting chart to image.

chart.ToImage(MyDir + "Chart to Tiff Image.Tiff", System.Drawing.Imaging.ImageFormat.Tiff);


{{< /highlight >}}
## **Conversione di grafici in TIFF multipagina**
{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by

//passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a sample value to "A1" cell

worksheet.Cells["A1"].PutValue(50);

//Adding a sample value to "A2" cell

worksheet.Cells["A2"].PutValue(100);

//Adding a sample value to "A3" cell

worksheet.Cells["A3"].PutValue(150);

//Adding a sample value to "B1" cell

worksheet.Cells["B1"].PutValue(4);

//Adding a sample value to "B2" cell

worksheet.Cells["B2"].PutValue(20);

//Adding a sample value to "B3" cell

worksheet.Cells["B3"].PutValue(50);

//Adding a chart to the worksheet

int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);

//Accessing the instance of the newly added chart

Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"

chart.NSeries.Add("A1:B3", true);

ImageOrPrintOptions options = new ImageOrPrintOptions();

options.HorizontalResolution = 300;

options.VerticalResolution = 300;

options.TiffCompression = TiffCompression.CompressionLZW;

options.IsCellAutoFit = false;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

options.OnePagePerSheet = true;

//Converting chart to image.

chart.ToImage(MyDir + "Chart to Tiff Image.tiff", options);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Converting%20Chart%20to%20Image%20%28Aspose.Cells%29.zip)
