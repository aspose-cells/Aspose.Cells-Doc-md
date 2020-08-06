---
title: Display or Hide Row Column Headers in Aspose.Cells
type: docs
weight: 60
url: /net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}} 

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them, and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells, developers can control the visibility of these row and column headers.

{{% /alert %}} 
### **Controlling the Visibility of the Worksheets**
Aspose.Cells provides a class, [Workbook](/pages/createpage.action?spaceKey=cellsnet&title=Aspose.Cells.Workbook+class&linkCreation=true&fromPageId=5020669), that represents a Microsoft Excel file. The Workbook class contains a Worksheets collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [Worksheet](/pages/createpage.action?spaceKey=cellsnet&title=Aspose.Cells.Worksheet+class&linkCreation=true&fromPageId=5020669) class. The Worksheet class provides a wide range of properties and methods for managing worksheets. To control the visibility of row and column headers, use the Worksheet class' IsRowColumnHeadersVisible property. IsRowColumnHeadersVisible is a Boolean property, which means that it can only store a true or false value.

A complete example is given below that shows how to use the Worksheet class' IsRowColumnHeadersVisible property to hide row and column headers on the first worksheet in a file.

The screenshot shows Book1.xls, the input file. It contains three worksheets: Sheet1, Sheet2 and Sheet3. Each worksheet is showing row and column headers.

**Book1.xls: worksheet before modification**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls is opened by calling the Workbook class' Open method and the row and column headers on the first worksheet are hidden. The modified file is saved as output.xls.

**Output.xls: worksheet after modification** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();



{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsnet.codeplex.com/SourceControl/latest#Plugins/Aspose For VSTO/Aspose.Cells Features missing in VSTO/Display or Hide Row Column Headers/)
- [CodePlex](https://asposevsto.codeplex.com/SourceControl/latest#Aspose Only features Unavailable in VSTO/Aspose.Cells/Display or Hide Row Column Headers/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)
- [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836/view/SourceCode#content)
## **Download Sample Code**
- [CodePlex](https://asposecellsnet.codeplex.com/releases/view/618484)
- [CodePlex](https://asposevsto.codeplex.com/releases/view/618289)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
- [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836#content)
