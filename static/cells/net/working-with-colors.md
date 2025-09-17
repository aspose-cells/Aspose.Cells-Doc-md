##Working With Colors
## **Aspose.Cells - Working With Colors**
**C#**
Workbook workbook = new Workbook(); // Creating a Workbook object
workbook.Worksheets.Add();
Worksheet worksheet = workbook.Worksheets[0];
//Accessing cell from the worksheet
Cell cell = worksheet.Cells["B2"];
Style style = cell.GetStyle();
//Setting the foreground color to yellow
style.BackgroundColor = Color.Yellow;
//Setting the background pattern to vertical stripe
style.Pattern = BackgroundType.VerticalStripe;
//Saving the modified style to the "B2" cell.
cell.SetStyle(style);
// === Setting Foreground ===
//Adding custom color to the palette at 55th index
Color color = Color.FromArgb(212, 213, 0);
workbook.ChangePalette(color, 55);
//Accessing cell from the worksheet
cell = worksheet.Cells["B3"];
//Adding some value to the cell
cell.PutValue("Hello Aspose!");
workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats
## **NPOI - HSSF XSSF - Working With Colors**
**C#**
IWorkbook wb = new XSSFWorkbook();
// Create a Worksheet
ISheet ws = wb.CreateSheet("Sheet1");
// Aqua background
ICellStyle style = wb.CreateCellStyle();
style.FillBackgroundColor = IndexedColors.Aqua.Index;
style.FillPattern = FillPattern.BigSpots;
IRow row = ws.CreateRow(0);
ICell cell = row.CreateCell(1);
cell.SetCellValue("X");
cell.CellStyle = style;
// Orange "foreground", foreground being the fill foreground not the font color.
style = wb.CreateCellStyle();
style.FillBackgroundColor = IndexedColors.Orange.Index;
style.FillPattern = FillPattern.SolidForeground;
cell = row.CreateCell(2);
cell.SetCellValue("X");
cell.CellStyle = style;
FileStream sw = File.Create("test.xlsx");
wb.Write(sw);
sw.Close();
## **Download Running Code**
Download **Working With Colors** form any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.1/Working.With.Colors.zip)
For more details, visit [Data Formating Features](http://www.aspose.com/docs/display/cellsjava/Working+with+Data+Formatting).
