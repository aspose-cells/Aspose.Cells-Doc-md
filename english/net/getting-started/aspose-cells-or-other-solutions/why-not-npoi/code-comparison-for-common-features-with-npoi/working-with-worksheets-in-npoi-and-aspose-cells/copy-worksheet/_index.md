---
title: Copy Worksheet
type: docs
weight: 40
url: /net/copy-worksheet/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Copy Worksheet**
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
## **NPOI - HSSF XSSF - Copy Worksheet**
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
## **Download Running Code**
Download **Copy Worksheet** form any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Copy.Worksheet.zip)

{{% alert color="primary" %}} 

For more details, visit [Working with Worksheets](/cells/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
