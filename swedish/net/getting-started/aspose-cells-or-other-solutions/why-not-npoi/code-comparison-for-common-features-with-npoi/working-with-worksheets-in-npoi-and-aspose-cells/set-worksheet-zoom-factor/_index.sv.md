---
title: Ställ in kalkylbladszoomfaktor
type: docs
weight: 80
url: /sv/net/set-worksheet-zoom-factor/
---
## **Aspose.Cells - Ställ in kalkylbladszoomfaktor**
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
## **NPOI - HSSF XSSF - Ställ in kalkylbladszoomfaktor**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Ställ in kalkylbladszoomfaktor** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Arbeta med arbetsblad](/cells/sv/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
