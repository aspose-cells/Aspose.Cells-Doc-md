##Copy Shapes between Worksheets in Aspose.Cells
Sometimes, you need to copy elements on a worksheet, for example pictures, charts and other drawing objects, between worksheets. Aspose.Cells supports this feature. Charts, images and other objects can be copied with the highest degree of precision.
This article gives you a detailed understanding on how to copy shapes between worksheets. To illustrate, it creates a console application in Visual Studio.Net, copies pictures, charts and other drawing objects between worksheets with using Aspose.Cells.
Below is the code for copying a chart from worksheet to another
**C#**
string FilePath = @"..\..\..\Sample Files\";
string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";
//Open the template file
Workbook workbook = new Workbook(FileName);
//Get the Chart from the "Chart" worksheet.
Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];
Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;
//Copy the Chart to the Result Worksheet
workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);
//Save the Worksheet
workbook.Save(FileName);
**Note:** For more details about copying multiple shapes you need to visit [here](https://docs.aspose.com/cells/net/copy-shapes-between-worksheets/)
## **Download Sample Code**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Download Running Example**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
