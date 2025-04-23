---
title: Convertire grafici in immagini
type: docs
weight: 10
url: /it/net/convert-charts-to-images/
---

**I grafici** sono visualmente accattivanti e facilitano la visualizzazione di confronti, pattern e tendenze nei dati. Ad esempio, anziché dover analizzare diverse colonne di numeri del foglio di calcolo, è possibile vedere in un'occhiata se le vendite stanno diminuendo o aumentando nei periodi trimestrali, o come le vendite effettive si confrontano con le vendite previste. A volte è necessario presentare il grafico nelle proprie applicazioni o pagine web. Potresti aver bisogno di inserirlo in un documento di Word, un file PDF, una presentazione di PowerPoint o in qualche altro scenario. Semplicemente desideri che il grafico sia renderizzato come un'immagine, in modo da poterlo incollare nelle tue applicazioni con facilità. Un'immagine vale più di mille parole. Spesso, nel corso del lavoro, si deve presentare informazioni statistiche e grafiche in modo facile da comprendere e da mantenere. Potresti provare l'automazione di Office ma l'automazione di Office ha i suoi svantaggi. Sono coinvolti diversi motivi e problemi: ad esempio, sicurezza, stabilità, scalabilità/velocità, prezzo, funzionalità ecc. In breve, ci sono molte ragioni, con la principale che Microsoft stesso raccomanda vivamente di evitare l'automazione di Office dalle soluzioni software: considerazioni per l'automazione lato server di Office. C'è un'altra opzione che puoi usare per convertire un grafico di Excel in un'immagine usando **Aspose.Cells**.
## **Conversión de gráfico a EMF**
{{< highlight csharp >}}

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
## **Conversión de gráfico a BMP**
{{< highlight csharp >}}

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
## **Conversión de gráfico a JPEG**
{{< highlight csharp >}}

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
## **Conversión de gráfico a PNG**
{{< highlight csharp >}}

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
## **Conversión de gráfico a TIFF**
{{< highlight csharp >}}

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
## **Conversión de gráfico a TIFF multipágina**
{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
