---
title: Diagramme in Bilder umwandeln
type: docs
weight: 10
url: /de/net/convert-charts-to-images/
---

**Diagramme** sind optisch ansprechend und erleichtern es Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen. Anstatt mehrere Spalten mit Arbeitsblattzahlen analysieren zu müssen, können Sie auf einen Blick erkennen, ob die Umsätze über Quartale hinweg fallen oder steigen oder wie sich die tatsächlichen Umsätze mit den prognostizierten Umsätzen vergleichen. Manchmal müssen Sie das Diagramm in Ihren Anwendungen oder Webseiten präsentieren. Sie möchten es möglicherweise in ein Word-Dokument, eine PDF-Datei, eine Powerpoint-Präsentation oder in einem anderen Szenario einfügen. Sie möchten das Diagramm einfach als Bild darstellen, um es problemlos in Ihre Anwendungen einfügen zu können. Ein Bild sagt mehr als tausend Worte. Häufig muss man im beruflichen Alltag statistische und grafische Informationen auf verständliche und leicht zu handhabende Weise präsentieren. Sie könnten versuchen, die Büroautomatisierung zu verwenden, aber die Büroautomatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, z. B. Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis, Funktionen usw. Kurz gesagt, es gibt viele Gründe, wobei der Hauptgrund darin besteht, dass Microsoft selbst dringend von der Büroautomatisierung von Softwarelösungen abrät: Überlegungen zur serverseitigen Automatisierung von Office. Es gibt eine andere Option, die Sie verwenden können, um ein Excel-Diagramm in ein Bild umzuwandeln, und zwar mit Hilfe von **Aspose.Cells**.
## **Konvertierung von Diagramm in EMF**
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
## **Konvertierung von Diagramm in BMP**
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
## **Konvertierung von Diagramm in JPEG**
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
## **Konvertierung von Diagramm in PNG**
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
## **Konvertierung von Diagramm in TIFF**
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
## **Konvertierung von Diagramm in Multipage-TIFF**
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
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Converting%20Chart%20to%20Image%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
