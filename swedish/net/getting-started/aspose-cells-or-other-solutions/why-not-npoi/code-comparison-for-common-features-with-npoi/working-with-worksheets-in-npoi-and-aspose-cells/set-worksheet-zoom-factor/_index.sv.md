---
title: Ställ in arbetsbladets zoomfaktor
type: docs
weight: 80
url: /sv/net/set-worksheet-zoom-factor/
---

## **Aspose.Cells - Ställ in arbetsbladets zoomfaktor**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

worksheet.Zoom = 75;

//Saving the Excel file

workbook.Save("../../data/newWorksheet.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Ställ in arbetsbladets zoomfaktor**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner formuläret **Ställ in arbetsbladets zoomfaktor** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

För mer information, besök [Arbeta med kalkylblad](/cells/sv/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
