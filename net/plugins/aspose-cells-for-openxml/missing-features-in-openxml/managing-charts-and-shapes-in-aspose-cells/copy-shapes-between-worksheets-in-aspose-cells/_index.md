---
title: Copy Shapes between Worksheets in Aspose.Cells
type: docs
weight: 30
url: /net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

Sometimes, you need to copy elements on a worksheet, for example pictures, charts and other drawing objects, between worksheets. Aspose.Cells supports this feature. Charts, images and other objects can be copied with the highest degree of precision.

This article gives you a detailed understanding on how to copy shapes between worksheets. To illustrate, it creates a console application in Visual Studio.Net, copies pictures, charts and other drawing objects between worksheets with using Aspose.Cells.

{{% /alert %}} 

Below is the code for copying a chart from worksheet to another

**C#**

{{< highlight csharp >}}

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



{{< /highlight >}}

**Note:** For more details about copying multiple shapes you need to visit [here](http://www.aspose.com/docs/display/cellsnet/Copy+Shapes+between+Worksheets)
### **Download Sample Code**
- [Codeplex](https://asposeopenxml.codeplex.com/SourceControl/latest#Aspose.Cells Features missing in OpenXML/Copy Shapes between Worksheets/)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
- [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c/view/SourceCode#content)
### **Download Running Example**
- [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
