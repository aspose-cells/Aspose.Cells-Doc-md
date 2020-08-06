---
title: Set Worksheet Zoom Factor
type: docs
weight: 80
url: /net/set-worksheet-zoom-factor/
---

## **Aspose.Cells - Set Worksheet Zoom Factor**
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
## **NPOI - HSSF XSSF - Set Worksheet Zoom Factor**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Download Running Code**
Download **Set Worksheet Zoom Factor** form any of the below mentioned social coding sites:

- [CodePlex](https://asposecellsnpoi.codeplex.com/downloads/get/1536892)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

For more details, visit [Working with Worksheets](http://www.aspose.com/docs/display/cellsnet/Working+with+Worksheets).

{{% /alert %}}
