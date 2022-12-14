---
title: الخط الجديد في Cells
type: docs
weight: 30
url: /ar/net/new-line-in-cells/
---
## **Aspose.Cells - الخط الجديد في Cells**
للتأكد من إمكانية قراءة النص في الخلية ، يمكن تطبيق فواصل أسطر واضحة والتفاف النص. يحول التفاف النص سطرًا واحدًا إلى عدة سطور في خلية ، حيث يتم وضع فواصل الأسطر الصريحة في فواصل في المكان الذي تريده بالضبط.

لالتفاف نص في خلية ، استخدم الخاصية Aspose.Cells.Style.IsTextWrapped.

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

Worksheet sheet = workbook.Worksheets[0];

sheet.Cells[2,2].Value = "Use \n with word wrap on to create a new line";

//Get Cell's Style

Style style = sheet.Cells[2, 2].GetStyle();

//Set Text Wrap property to true

style.IsTextWrapped = true;

//Set Cell's Style

sheet.Cells[2, 2].SetStyle(style);

workbook.Save("test.xlsx");

{{< /highlight >}}
## **NPOI - HSSF XSSF - خط جديد في Cells**
يجب أن يكون CellStyle.setWrapText صحيحًا للنص الملتف.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet = workbook.CreateSheet("Sheet1");

IRow row = sheet.CreateRow(2);

ICell cell = row.CreateCell(2);

cell.SetCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

ICellStyle cs = workbook.CreateCellStyle();

cs.WrapText = true;

cell.CellStyle = cs;

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**الخط الجديد في Cells** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[فواصل الأسطر وتغليف النص](/cells/ar/net/line-breaks-and-text-wrapping/).

{{% /alert %}}
