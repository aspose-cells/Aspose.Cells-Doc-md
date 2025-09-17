##Adding Hyperlinks to Link Data in Aspose.Cells
A hyperlink is used to create a link between two entities. Everybody is familiar with the use of hyperlinks, especially on websites.
Using Aspose.Cells, developers can create different kinds of hyperlinks in Microsoft Excel files. This topic discusses what types of hyperlinks are supported by Aspose.Cells and how they can be used in our Excel files.
## **Adding Hyperlinks**
Three types of hyperlink can be added to a cell using Aspose.Cells:
- [Adding link to a URL](#adding-link-to-a-url).
- [Adding a link to another cell in the same file](#adding-a-link-to-a-cell-in-the-same-file).
- [Adding a link to an external file](#adding-a-link-to-an-external-file).
Aspose.Cells allows developers to add hyperlinks to Excel files either using the API or [designer spreadsheets](https://docs.aspose.com/cells/net/what-is-a-designer-spreadsheet/) (spreadsheets where hyperlinks are created manually and Aspose.Cells is used to import them into other spreadsheets).
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides different methods for adding different hyperlinks to Excel files.
### **Adding Link to a URL**
The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class contains a [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) collection. Each item in the Hyperlinks collection represents a Hyperlink. Add hyperlinks to URLs by calling the Hyperlinks collection's Add method. The Add method takes the following parameters:
- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range
- URL, the URL address.
**C#**
//Instantiating a Workbook object
Workbook workbook = new Workbook();
//Adding a new worksheet to the Workbook object
int i = workbook.Worksheets.Add();
//Obtaining the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.Worksheets[i];
//Adding a hyperlink to a URL at "A1" cell
worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");
//Saving the Excel file
workbook.Save("C:\\book1.xls");
### **Adding a Link to a Cell in the Same File**
It is possible to add hyperlinks to cells in the same Excel file by calling the Hyperlink collection's Add method. The Add method works for both internal and external hyperlinks. One version of the overloaded method takes the following parameters:
- Cell name,the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target cell.
**C#**
//Instantiating a Workbook object
Workbook workbook = new Workbook();
//Obtaining the reference of the first (default) worksheet
Worksheet worksheet = workbook.Worksheets[0];
//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
//the same Excel file
worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");
//Saving the Excel file
workbook.Save("C:\\book1.xls");
### **Adding a Link to an External File**
It is possible to add hyperlinks to external Excel files by calling the Hyperlinks collection's Add method. The Add method takes the following parameters:
- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target, external Excel file.
**C#**
//Instantiating a Workbook object
Workbook workbook = new Workbook();
//Adding a new worksheet to the Excel object
int i = workbook.Worksheets.Add();
//Obtaining the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.Worksheets[i];
//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
//the same Excel file
worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");
//Saving the Excel file
workbook.Save("C:\\book2.xls");
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
