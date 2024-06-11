---
title: 复制工作表
type: docs
weight: 40
url: /zh/net/copy-worksheet/
---

## **Aspose.Cells - 复制工作表**
**C#**

{{< highlight cs >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook("../../data/workbook.xlsx");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.AddCopy("Sheet1");

wb.Save("../../data/workbook.xlsx");


{{< /highlight >}}
## **NPOI - HSSF XSSF - 复制工作表**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

wb.CreateSheet("new sheet");

wb.CreateSheet("second sheet");

ISheet cloneSheet = wb.CloneSheet(0);

FileStream sw = File.Create("newWorksheet.xls");

wb.Write(sw);

sw.Close();


{{< /highlight >}}
## **下载运行代码**
从以下任意社交编码网站下载**复制工作表**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Copy.Worksheet.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[使用工作表](/cells/zh/net/working-with-worksheets-in-npoi-and-aspose-cells/)。

{{% /alert %}}
