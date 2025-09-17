##Working with Freeze Panes
## **Aspose.Cells - Working with Freeze Panes**
**C#**
//Instantiating a Workbook object
Workbook workbook = new Workbook();
//Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.Worksheets[0];
worksheet.FreezePanes(2, 2, 2, 0);
workbook.Save("output-FreezeFile-Aspose.Cells.xls");
For more details, visit [FreezePanes Method](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index).
## **NPOI - HSSF XSSF - Working with Freeze Panes**
**C#**
HSSFWorkbook hssfworkbook = new HSSFWorkbook();
ISheet sheet1 = hssfworkbook.CreateSheet("new sheet");
ISheet sheet2 = hssfworkbook.CreateSheet("second sheet");
ISheet sheet3 = hssfworkbook.CreateSheet("third sheet");
// Freeze just one row
sheet1.CreateFreezePane(0, 2, 0, 2);
// Freeze just one column
sheet2.CreateFreezePane(2, 0, 2, 0);
// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).
sheet3.CreateFreezePane(2, 2);
FileStream file = new FileStream(@"output-FreezeFile-NPOI.xls", FileMode.Create);
hssfworkbook.Write(file);
file.Close();
## **Download Running Code**
Download **Working with Freeze Panes** form any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.3/Freeze.Panes.zip)
For more details, visit [Working with Worksheets](https://docs.aspose.com/cells/net/working-with-worksheets-in-npoi-and-aspose-cells/).
