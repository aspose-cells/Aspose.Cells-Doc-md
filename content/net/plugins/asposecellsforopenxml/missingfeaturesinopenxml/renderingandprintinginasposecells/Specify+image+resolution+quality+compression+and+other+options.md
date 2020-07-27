+++
title = "Specify image resolution quality compression and other options" 
description = "" 
weight = 20885 
+++

Aspose.Cells for .NET : Specify image resolution, quality, compression and other options  

# Aspose.Cells for .NET : Specify image resolution, quality, compression and other options


string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Chart to Image with Image Options.tiff";//Instantiating a Workbook objectWorkbook workbook = new Workbook();//Adding a new worksheet to the Excel objectint sheetIndex = workbook.Worksheets.Add();//Obtaining the reference of the newly added worksheet by//passing its sheet indexWorksheet worksheet = workbook.Worksheets\[sheetIndex\];//Adding a sample value to "A1" cellworksheet.Cells\["A1"\].PutValue(50);//Adding a sample value to "A2" cellworksheet.Cells\["A2"\].PutValue(100);//Adding a sample value to "A3" cellworksheet.Cells\["A3"\].PutValue(150);//Adding a sample value to "B1" cellworksheet.Cells\["B1"\].PutValue(4);//Adding a sample value to "B2" cellworksheet.Cells\["B2"\].PutValue(20);//Adding a sample value to "B3" cellworksheet.Cells\["B3"\].PutValue(50);//Adding a chart to the worksheetint chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Column, 5, 0, 15, 5);//Accessing the instance of the newly added chartAspose.Cells.Charts.Chart chart = worksheet.Charts\[chartIndex\];//Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"chart.NSeries.Add("A1:B3", true);ImageOrPrintOptions options = new ImageOrPrintOptions();options.HorizontalResolution = 300;options.VerticalResolution = 300;options.TiffCompression = TiffCompression.CompressionLZW;options.IsCellAutoFit = false;options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;options.OnePagePerSheet = true;//Converting chart to image.chart.ToImage(FileName, options);

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Chart%20to%20Image%20with%20Image%20Options%20%28Aspose.Cells%29.zip)

