---
title: Cells'de Yeni Hat
type: docs
weight: 30
url: /tr/net/new-line-in-cells/
---
## **Aspose.Cells - Cells'de Yeni Hat**
Bir hücredeki metnin okunabilmesini sağlamak için açık satır sonları ve metin kaydırma uygulanabilir. Metin kaydırma, bir hücrede bir satırı birkaç satıra dönüştürür; bu açık satır sonları, tam olarak istediğiniz yerde aralara konur.

Metni bir hücreye kaydırmak için Aspose.Cells.Style.IsTextWrapped özelliğini kullanın.

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
## **NPOI - HSSF XSSF - Cells'de Yeni Satır**
Sarılmış metin için CellStyle.setWrapText doğru olmalıdır.

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
## **Çalışan Kodu İndir**
 İndirmek**Cells'de Yeni Hat** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Satır Sonları ve Metin Sarma](/cells/tr/net/line-breaks-and-text-wrapping/).

{{% /alert %}}
