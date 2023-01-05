---
title: Stellen Sie den Arbeitsblatt-Zoomfaktor ein
type: docs
weight: 80
url: /de/net/set-worksheet-zoom-factor/
---
## **Aspose.Cells - Stellen Sie den Arbeitsblatt-Zoomfaktor ein**
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
## **NPOI - HSSF XSSF - Arbeitsblatt-Zoomfaktor festlegen**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Stellen Sie den Arbeitsblatt-Zoomfaktor ein** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Arbeiten mit Arbeitsblättern](/cells/de/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
