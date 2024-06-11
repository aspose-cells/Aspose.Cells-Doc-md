---
title: 自动调整工作表列宽
type: docs
weight: 30
url: /zh/net/auto-fit-columns-in-worksheet/
---

## **Aspose.Cells - 自动调整工作表列宽**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Auto-fitting the 1st column of the worksheet

//Adding a string value to the cell

worksheet.Cells["A1"].PutValue("This is a test input");

//Adding a double value to the cell

worksheet.Cells["B1"].PutValue(20.5);

//Adding an integer  value to the cell

worksheet.Cells["C1"].PutValue(15);

//Adding a boolean value to the cell

worksheet.Cells["D1"].PutValue(true);

worksheet.AutoFitColumn(0);

worksheet.AutoFitColumn(1);

worksheet.AutoFitColumn(2);

worksheet.AutoFitColumn(3);

//Saving the modified Excel file in bin/debug folder

workbook.Save("AutoFiltRowsandColumns.xls");

{{< /highlight >}}
## **NPOI - HSSF XSSF - 自动调整工作表列宽**
**C#**

{{< highlight cs >}}

 HSSFWorkbook hssfworkbook = new HSSFWorkbook();

ISheet sheet=hssfworkbook.CreateSheet("Sheet1");

IRow row=sheet.CreateRow(0);

row.CreateCell(0).SetCellValue("This is a test input");

row.CreateCell(1).SetCellValue("Hello");

row.CreateCell(2).SetCellValue("1234.0023");

sheet.AutoSizeColumn(0);

sheet.AutoSizeColumn(1);

sheet.AutoSizeColumn(2);

FileStream file = new FileStream(@"AutoFiltRowsandColumns(NPOI).xls", FileMode.Create);

hssfworkbook.Write(file);

file.Close();

{{< /highlight >}}
## **下载运行代码**
从以下任意社交编码网站下载**自动调整列宽**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.3/Auto.Fit.Columns.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[使用工作表](/cells/zh/net/working-with-worksheets-in-npoi-and-aspose-cells/)。

{{% /alert %}}
