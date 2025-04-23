---
title: 设置工作表缩放比例
type: docs
weight: 80
url: /zh/net/set-worksheet-zoom-factor/
---

## **Aspose.Cells - 设置工作表缩放比例**
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
## **NPOI - HSSF XSSF - 设置工作表缩放比例**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**设置工作表缩放比例**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[使用工作表](/cells/zh/net/working-with-worksheets-in-npoi-and-aspose-cells/)。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
