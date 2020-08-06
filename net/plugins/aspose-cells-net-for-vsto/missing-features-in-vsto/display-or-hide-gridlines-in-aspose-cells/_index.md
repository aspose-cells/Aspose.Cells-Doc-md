---
title: Display or Hide Gridlines in Aspose.Cells
type: docs
weight: 50
url: /net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}} 

All Excel worksheets have gridlines by default. They help delineate cells, so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.

{{% /alert %}} 
### **Controlling the Visibility of the Gridlines**
Aspose.Cells provides a class, [Workbook](/pages/createpage.action?spaceKey=cellsnet&title=Aspose.Cells.Workbook+class&linkCreation=true&fromPageId=5020671), that represents a Microsoft Excel file. The Workbook class contains a Worksheets collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](/pages/createpage.action?spaceKey=cellsnet&title=Aspose.Cells.Worksheet+class&linkCreation=true&fromPageId=5020671) class. The Worksheet class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the Worksheet class' IsGridlinesVisible property. IsGridlinesVisible is a Boolean property, which means that it can only store a true or false value.

A complete example is given below that demonstrates the use of the IsGridlinesVisible property of the Worksheet class to hide the gridlines of the first worksheet of the Excel file.

In the screenshot below, you can see that the Book1.xls file contains three worksheets: Sheet1, Sheet2 and Sheet3. All worksheets have gridlines.

**Book1.xls: worksheet view before modification** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

The Book1.xls file is opened by calling the Workbook class' Open method and the gridlines on the first worksheet are hidden. The modified file is saved as output.xls.

**Output.xls: worksheet after modification** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();



{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsnet.codeplex.com/SourceControl/latest#Plugins/Aspose For VSTO/Aspose.Cells Features missing in VSTO/Display or Hide Gridlines/)
- [CodePlex](https://asposevsto.codeplex.com/SourceControl/latest#Aspose Only features Unavailable in VSTO/Aspose.Cells/Display or Hide Gridlines/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)
- [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836/view/SourceCode#content)
## **Download Sample Code**
- [CodePlex](https://asposecellsnet.codeplex.com/releases/view/618484)
- [CodePlex](https://asposevsto.codeplex.com/releases/view/618289)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
- [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836#content)
