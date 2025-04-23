---
title: Convertir gráficos en imágenes
type: docs
weight: 10
url: /es/net/convert-charts-to-images/
---

**Los gráficos** son visualmente atractivos y facilitan que los usuarios vean comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de tener que analizar varias columnas de números de hojas de cálculo, puedes ver de un vistazo si las ventas están cayendo o aumentando durante los períodos trimestrales, o cómo se comparan las ventas reales con las proyectadas. A veces, es necesario presentar el gráfico en tus aplicaciones o páginas web. Es posible que necesites insertarlo en un documento de Word, un archivo PDF, una presentación de Power Point u otro escenario. Simplemente quieres que el gráfico se represente como una imagen, para que puedas pegarlo en tus aplicaciones con facilidad. Una imagen vale más que mil palabras. Frecuentemente, en el transcurso del trabajo, uno tiene que presentar información estadística y gráfica de manera fácil de entender y de mantener. Puedes intentar la Automatización de Office, pero la automatización de Office tiene sus propias desventajas. Hay varias razones y problemas involucrados: por ejemplo, Seguridad, Estabilidad, Escalabilidad / Velocidad, Precio, Funciones, etc. En resumen, hay muchas razones, siendo la principal que Microsoft en sí misma desaconseja fuertemente la automatización de Office desde soluciones de software: Consideraciones para la Automatización del lado del servidor de Office. Existe otra opción que puedes utilizar para convertir un gráfico de Excel en una imagen usando **Aspose.Cells**.
## **Convertir gráfico a EMF**
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
## **Convertir gráfico a BMP**
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
## **Convertir gráfico a JPEG**
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
## **Convertir gráfico a PNG**
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
## **Convertir gráfico a TIFF**
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
## **Convertir gráfico a TIFF de varias páginas**
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
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Converting%20Chart%20to%20Image%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
