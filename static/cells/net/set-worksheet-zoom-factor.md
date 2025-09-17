##Set Worksheet Zoom Factor
## **Aspose.Cells - Set Worksheet Zoom Factor**
**C#**
//Instantiating a Workbook object
Workbook workbook = new Workbook();
//Adding a new worksheet to the Workbook object
WorksheetCollection worksheets = workbook.Worksheets;
Worksheet worksheet = worksheets.Add("My Worksheet");
worksheet.Zoom = 75;
//Saving the Excel file
workbook.Save("../../data/newWorksheet.xls");
## **NPOI - HSSF XSSF - Set Worksheet Zoom Factor**
**C#**
IWorkbook wb = new XSSFWorkbook();
ISheet sheet1 = wb.CreateSheet("First Sheet");
sheet1.SetZoom(3, 4); // 75 percent
FileStream sw = File.Create("../../data/newWorksheet.xls");
wb.Write(sw);
sw.Close();
## **Download Running Code**
Download **Set Worksheet Zoom Factor** form any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)
For more details, visit [Working with Worksheets](https://docs.aspose.com/cells/net/working-with-worksheets-in-npoi-and-aspose-cells/).
