---
title: Установить коэффициент масштабирования рабочего листа
type: docs
weight: 80
url: /ru/net/set-worksheet-zoom-factor/
---
## **Aspose.Cells - Установить коэффициент масштабирования рабочего листа**
**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

worksheet.Zoom = 75;

//Saving the Excel file

workbook.Save("../../data/newWorksheet.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Установить коэффициент масштабирования рабочего листа**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Установить коэффициент масштабирования рабочего листа** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Работа с рабочими листами](/cells/ru/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
