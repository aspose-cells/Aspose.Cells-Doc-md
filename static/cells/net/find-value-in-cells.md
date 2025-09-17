##Find Value in Cells
## **Aspose.Cells - Find Value in Cells**
In Microsoft Excel, users can search for cells that contain specific data. For example, clicking **Edit** and then **Find** opens the Search dialog. Users enters a value and clicks **OK** to search for it. Excel highlights matching fields.
**C#**
//Instantiating a Workbook object
Workbook workbook = new Workbook("../../data/test.xlsx");
//Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.Worksheets[0];
//Finding the cell containing the specified formula
Cells cells = worksheet.Cells;
//Instantiate FindOptions
FindOptions findOptions = new FindOptions();
//Finding the cell containing a string value that starts with "Or"
findOptions.LookAtType = LookAtType.StartWith;
Cell cell = cells.Find("SH", null, findOptions);
//Printing the name of the cell found after searching worksheet
Console.WriteLine("Name of the cell containing String: " + cell.Name);
## **Download Running Code**
Download **Find Value in Cells** form any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)
For more details, visit [Find or Search Data](https://docs.aspose.com/cells/net/find-or-search-data/).
