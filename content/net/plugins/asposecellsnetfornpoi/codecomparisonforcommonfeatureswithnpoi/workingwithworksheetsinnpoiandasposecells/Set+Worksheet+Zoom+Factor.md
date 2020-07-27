+++
title = "Set Worksheet Zoom Factor" 
description = "" 
weight = 20935 
+++

Aspose.Cells for .NET : Set Worksheet Zoom Factor  

# Aspose.Cells for .NET : Set Worksheet Zoom Factor


## Aspose.Cells - Set Worksheet Zoom Factor

**C#**

{{< code lang="c#" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object
WorksheetCollection worksheets = workbook.Worksheets;
Worksheet worksheet = worksheets.Add("My Worksheet");

worksheet.Zoom = 75;

//Saving the Excel file
workbook.Save("../../data/newWorksheet.xls");

{{< /code >}}

## NPOI - HSSF XSSF - Set Worksheet Zoom Factor

**C#**

{{< code lang="c#" >}}
IWorkbook wb = new XSSFWorkbook();
ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");
wb.Write(sw);
sw.Close();
{{< /code >}}

## Download Running Code

Download **Set Worksheet Zoom Factor** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposecellsnpoi.codeplex.com/downloads/get/1536892)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

For more details, visit [Working with Worksheets](http://www.aspose.com/docs/display/cellsnet/Working+with+Worksheets).

