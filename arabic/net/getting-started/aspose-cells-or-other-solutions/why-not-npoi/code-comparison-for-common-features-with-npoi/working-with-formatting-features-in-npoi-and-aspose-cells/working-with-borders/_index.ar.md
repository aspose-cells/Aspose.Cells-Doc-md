﻿---
title: العمل مع الحدود
type: docs
weight: 10
url: /ar/net/working-with-borders/
---
## **Aspose.Cells - العمل مع الحدود**
**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Worksheets.Add();

Worksheet worksheet = workbook.Worksheets[0];

// Style the cell with borders all around.

Style style = workbook.CreateStyle();

style.SetBorder(BorderType.BottomBorder, CellBorderType.Thin, Color.Black);

style.SetBorder(BorderType.LeftBorder, CellBorderType.Thin, Color.Green);

style.SetBorder(BorderType.RightBorder, CellBorderType.Thin, Color.Blue);

style.SetBorder(BorderType.TopBorder, CellBorderType.MediumDashed, Color.Black);

Cell cell = worksheet.Cells["A1"];

cell.SetStyle(style);            

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats


{{< /highlight >}}
## **NPOI - HSSF XSSF - العمل مع الحدود**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

// Create a Worksheet

ISheet ws = wb.CreateSheet("Sheet1");

ICellStyle style = wb.CreateCellStyle();

//Setting the line of the top border

style.BorderTop = BorderStyle.Thick;

style.TopBorderColor = 256;

style.BorderLeft = BorderStyle.Thick;

style.LeftBorderColor = 256;

style.BorderRight = BorderStyle.Thick;

style.RightBorderColor = 256;

style.BorderBottom = BorderStyle.Thick;

style.BottomBorderColor = 256;

IRow row = ws.CreateRow(0);

ICell cell = row.CreateCell(1);

cell.CellStyle = style;

FileStream sw = File.Create("test.xlsx");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**العمل مع الحدود** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.1/Working.With.Borders.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ميزات تشكيل البيانات](http://www.aspose.com/docs/display/cellsjava/Working+with+Data+Formatting).

{{% /alert %}}