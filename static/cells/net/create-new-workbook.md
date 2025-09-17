##Create New Workbook
## **Aspose.Cells - Create New Workbook**
Workbook class is available for simple use
**C#**
Workbook workbook = new Workbook(); // Creating a Workbook object
workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats
## **NPOI - HSSF XSSF - Create New Workbook**
Create new Workbook using Workbook class and save using FileOutputStream.
**C#**
IWorkbook workbook = new XSSFWorkbook();
workbook.CreateSheet("Sheet A1");
workbook.CreateSheet("Sheet A2");
workbook.CreateSheet("Sheet A3");
FileStream sw = File.Create("test.xlsx");
workbook.Write(sw);
sw.Close();
## **Download Running Code**
Download **Create New Workbook** form any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
