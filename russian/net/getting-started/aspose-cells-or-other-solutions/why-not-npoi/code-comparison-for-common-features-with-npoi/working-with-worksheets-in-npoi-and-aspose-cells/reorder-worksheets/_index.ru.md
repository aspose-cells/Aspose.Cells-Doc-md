---
title: Перестановка рабочих листов
type: docs
weight: 70
url: /ru/net/reorder-worksheets/
---

## **Aspose.Cells - Перестановка рабочих листов**
**C#**

{{< highlight cs >}}

 //Create a new Workbook.

Workbook workbook = new Workbook();

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet1 = worksheets[0];

Worksheet worksheet2 = worksheets.Add("Sheet2");

Worksheet worksheet3 = worksheets.Add("Sheet3");

//Move Sheets with in Workbook.

worksheet2.MoveTo(0);

worksheet1.MoveTo(1);

worksheet3.MoveTo(2);

//Save the excel file.

workbook.Save("../../data/AsposeMoveSheet.xls");

{{< /highlight >}}
## **NPOI - HSSF XSSF - Перестановка рабочих листов**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

wb.CreateSheet("new sheet");

wb.CreateSheet("second sheet");

wb.CreateSheet("third sheet");

wb.SetSheetOrder("second sheet", 0);

wb.SetSheetOrder("new sheet", 1);

wb.SetSheetOrder("third sheet", 2);

FileStream sw = File.Create("../../data/Reordered.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Скачать работающий код**
Скачайте **Переставить рабочие листы** с любого из перечисленных ниже сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/ReOrder.WorkSheets.zip)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Работа с листами](/cells/ru/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
