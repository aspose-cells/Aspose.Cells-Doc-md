---
title: Новая строка в ячейках
type: docs
weight: 30
url: /ru/net/new-line-in-cells/
---

## **Aspose.Cells - Новая строка в ячейках**
Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.

Чтобы переносить текст в ячейке, используйте свойство Aspose.Cells.Style.IsTextWrapped.

**C#**

{{< highlight cs >}}

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
## **NPOI - HSSF XSSF - Новая строка в ячейках**
CellStyle.setWrapText должно быть true для переноса текста.

**C#**

{{< highlight cs >}}

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
## **Скачать работающий код**
Загрузите **Новая строка в ячейках** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Разрывы строк и перенос текста](/cells/ru/net/line-breaks-and-text-wrapping/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
