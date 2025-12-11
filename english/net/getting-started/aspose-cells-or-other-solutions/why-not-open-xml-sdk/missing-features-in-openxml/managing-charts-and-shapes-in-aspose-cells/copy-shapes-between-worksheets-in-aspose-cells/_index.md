---  
title: Copy Shapes between Worksheets in Aspose.Cells  
type: docs  
weight: 30  
url: /net/copy-shapes-between-worksheets-in-aspose-cells/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Sometimes, you need to copy elements **in** a worksheet, for example pictures, charts, and other drawing objects, between worksheets. Aspose.Cells supports this feature. Charts, images, and other objects can be copied with the highest degree of precision.  

This article gives you a detailed understanding **of how to** copy shapes between worksheets. To illustrate, it creates a console application in Visual Studio .NET, copies pictures, charts, and other drawing objects between worksheets using Aspose.Cells.  

{{% /alert %}}  

Below is the code for copying a chart from one worksheet to another  

**C#**  

{{< highlight csharp >}}  

 string FilePath = @"..\..\..\Sample Files\";  

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";  

// Open the template file  

Workbook workbook = new Workbook(FileName);  

// Get the Chart from the "Chart" worksheet.  

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];  

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;  

// Copy the Chart to the Result worksheet  

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);  

// Save the workbook  

workbook.Save(FileName);  

{{< /highlight >}}  

**Note:** For more details about copying multiple shapes, you need to visit [here](/cells/net/copy-shapes-between-worksheets/)  

## **Download Sample Code**  
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)  

## **Download Running Example**  
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)  

{{< app/cells/assistant language="csharp" >}}
