---
title: Create New Workbook
type: docs
weight: 20
url: /net/create-new-workbook/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Create New Workbook**
The Workbook class is available for simple use.

**C#**

{{< highlight cs >}}
 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); // Workbooks can be saved in many formats
{{< /highlight >}}

## **NPOI - HSSF XSSF - Create New Workbook**
Create a new workbook using the Workbook class and save it using a FileOutputStream.

**C#**

{{< highlight cs >}}
 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();
{{< /highlight >}}

## **Download Running Code**
Download **Create New Workbook** from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
