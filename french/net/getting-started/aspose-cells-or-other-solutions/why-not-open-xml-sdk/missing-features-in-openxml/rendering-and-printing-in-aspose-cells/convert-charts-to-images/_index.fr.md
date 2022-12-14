---
title: Convertir des graphiques en images
type: docs
weight: 10
url: /fr/net/convert-charts-to-images/
---
**Graphiques**sont visuellement attrayants et permettent aux utilisateurs de voir facilement des comparaisons, des modèles et des tendances dans les données. Par exemple, plutôt que d'avoir à analyser plusieurs colonnes de numéros de feuille de calcul, vous pouvez voir en un coup d'œil si les ventes baissent ou augmentent au cours des périodes trimestrielles, ou comment les ventes réelles se comparent aux ventes prévues. Parfois, vous devez présenter le graphique dans vos applications ou pages web. Vous devrez peut-être l'insérer dans un document Word, un fichier PDF, une présentation Power Point ou dans un autre scénario. Vous voulez simplement que le graphique soit rendu sous forme d'image, afin que vous puissiez le coller facilement dans vos applications. Une image vaut la peine. Fréquemment, dans le cadre du travail, on doit présenter des informations statistiques et graphiques d'une manière facile à comprendre et à maintenir. Vous pouvez essayer la bureautique, mais la bureautique a ses propres inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, l'évolutivité/la vitesse, le prix, les fonctionnalités, etc. Automatisation côté serveur d'Office. Il existe une autre option que vous pouvez utiliser pour convertir un graphique Excel en image à l'aide de**Aspose.Cells**.
## **Conversion d'un graphique en EMF**
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
## **Conversion d'un graphique en BMP**
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
## **Conversion d'un graphique en JPEG**
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
## **Conversion d'un graphique en PNG**
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
## **Conversion d'un graphique en TIFF**
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
## **Conversion d'un graphique en TIFF multipage**
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
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Converting%20Chart%20to%20Image%20%28Aspose.Cells%29.zip)
