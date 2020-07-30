---
title : "Working with Freeze Panes" 
description : "" 
weight : 20937 
toc : false
type: docs
url: /net/plugins/npoi/codeinnpoi/worksheets/working+with+freeze+panes/
---

# Aspose.Cells for .NET : Working with Freeze Panes


## Aspose.Cells - Working with Freeze Panes

**C#**

{{< code lang="c#" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.Worksheets[0];

worksheet.FreezePanes(2, 2, 2, 0);

workbook.Save("output-FreezeFile-Aspose.Cells.xls");

{{< /code >}}

For more details, visit [FreezePanes Method](http://www.aspose.com/api/net/cells/aspose.cells/worksheet/methods/freezepanes/index).

## NPOI - HSSF XSSF - Working with Freeze Panes

**C#**

{{< code lang="c#" >}}
HSSFWorkbook hssfworkbook = new HSSFWorkbook();

ISheet sheet1 = hssfworkbook.CreateSheet("new sheet");
ISheet sheet2 = hssfworkbook.CreateSheet("second sheet");
ISheet sheet3 = hssfworkbook.CreateSheet("third sheet");

// Freeze just one row
sheet1.CreateFreezePane(0, 2, 0, 2);
// Freeze just one column
sheet2.CreateFreezePane(2, 0, 2, 0);
// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).
sheet3.CreateFreezePane(2, 2);

FileStream file = new FileStream(@"output-FreezeFile-NPOI.xls", FileMode.Create);
hssfworkbook.Write(file);
file.Close();

{{< /code >}}

## Download Running Code

Download **Working with Freeze Panes** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposecellsnpoi.codeplex.com/downloads/get/1565290)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.3/Freeze.Panes.zip)

For more details, visit [Working with Worksheets](http://www.aspose.com/docs/display/cellsnet/Working+with+Worksheets).

