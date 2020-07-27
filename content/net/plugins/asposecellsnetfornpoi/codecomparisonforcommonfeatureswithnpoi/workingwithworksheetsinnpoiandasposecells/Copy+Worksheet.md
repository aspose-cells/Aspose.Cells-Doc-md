+++
title = "Copy Worksheet" 
description = "" 
weight = 20931 
+++

Aspose.Cells for .NET : Copy Worksheet  

# Aspose.Cells for .NET : Copy Worksheet


## Aspose.Cells - Copy Worksheet

**C#**

{{< code lang="c#" >}}
//Create a new Workbook by excel file path
Workbook wb = new Workbook("../../data/workbook.xlsx");

//Create a Worksheets object with reference to the sheets of the Workbook.
WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing sheet within the Workbook.
sheets.AddCopy("Sheet1");
wb.Save("../../data/workbook.xlsx");

{{< /code >}}

## NPOI - HSSF XSSF - Copy Worksheet

**C#**

{{< code lang="c#" >}}
IWorkbook wb = new XSSFWorkbook();
wb.CreateSheet("new sheet");
wb.CreateSheet("second sheet");
ISheet cloneSheet = wb.CloneSheet(0);

FileStream sw = File.Create("newWorksheet.xls");
wb.Write(sw);
sw.Close();

{{< /code >}}

## Download Running Code

Download **Copy Worksheet** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposecellsnpoi.codeplex.com/downloads/get/1536885)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Copy.Worksheet.zip)

For more details, visit [Working with Worksheets](http://www.aspose.com/docs/display/cellsnet/Working+with+Worksheets).

