---
title: تحديد منطقة الطباعة
type: docs
weight: 30
url: /ar/net/set-print-area/
---

## **Aspose.Cells - تحديد منطقة الطباعة**
بشكل افتراضي، تشمل منطقة الطباعة فقط جميع مناطق ورق العمل التي تحتوي على بيانات. يمكن للمطورين إنشاء منطقة طباعة محددة لورق العمل.

لتحديد منطقة طباعة محددة، استخدم خاصية PrintArea لفئة [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). قم بتعيين مجموعة خلايا تحدد منطقة الطباعة لهذه الخاصية.

**C#**

{{< highlight cs >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

workbook.Worksheets.Add("new sheet");

workbook.Worksheets.Add("second sheet");

Worksheet sheet1 = workbook.Worksheets[0];

sheet1.Cells[0, 0].Value = 1;

sheet1.Cells[0, 1].Value = 2;

sheet1.Cells[0, 2].Value = 3;

sheet1.Cells[1, 0].Value = 4;

sheet1.Cells[1, 1].Value = 5;

Worksheet sheet2 = workbook.Worksheets[1];

sheet2.Cells[0, 0].Value = 2.1;

sheet2.Cells[0, 4].Value = 2.2;

sheet2.Cells[0, 5].Value = 2.3;

sheet2.Cells[1, 4].Value = 2.4;

sheet2.Cells[1, 5].Value = 2.5;

// Accessing the first worksheet in the Workbook file

Worksheet sheet = workbook.Worksheets[0];

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.PageSetup;

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.PrintArea = "A1:F20";

workbook.Save("test.xlsx");

{{< /highlight >}}
## **NPOI - HSSF XSSF - تحديد منطقة الطباعة**
تتوفر طريقة Workbook.setPrintArea لتعيين خصائص الصفحة لمنطقة الطباعة

**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("new sheet");

ISheet sheet2 = wb.CreateSheet("second sheet");

// Set the columns to repeat from column 0 to 2 on the first sheet

IRow row1 = sheet1.CreateRow(0);

row1.CreateCell(0).SetCellValue(1);

row1.CreateCell(1).SetCellValue(2);

row1.CreateCell(2).SetCellValue(3);

IRow row2 = sheet1.CreateRow(1);

row2.CreateCell(1).SetCellValue(4);

row2.CreateCell(2).SetCellValue(5);


IRow row3 = sheet2.CreateRow(1);

row3.CreateCell(0).SetCellValue(2.1);

row3.CreateCell(4).SetCellValue(2.2);

row3.CreateCell(5).SetCellValue(2.3);

IRow row4 = sheet2.CreateRow(2);

row4.CreateCell(4).SetCellValue(2.4);

row4.CreateCell(5).SetCellValue(2.5);

// Set the columns to repeat from column 0 to 2 on the first sheet

wb.SetRepeatingRowsAndColumns(0, 0, 2, -1, -1);

// Set the the repeating rows and columns on the second sheet.

wb.SetRepeatingRowsAndColumns(1, 4, 5, 1, 2);

//set the print area for the first sheet

wb.SetPrintArea(0, 1, 2, 0, 3);

FileStream sw = File.Create("test.xlsx");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تحديد منطقة الطباعة** من أي من مواقع التعديل الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Set.Print.Area.Aspose.Cells.zip)

{{% alert color="primary" %}} 

للحصول على مزيد من التفاصيل، قم بزيارة [ضبط خيارات الطباعة](/cells/ar/net/setting-print-options/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
