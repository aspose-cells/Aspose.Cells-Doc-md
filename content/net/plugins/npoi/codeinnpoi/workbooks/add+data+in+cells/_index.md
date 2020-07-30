---
title : "Add Data in Cells" 
description : "" 
weight : 20924 
toc : false
type: docs
url: /net/plugins/npoi/codeinnpoi/workbooks/add+data+in+cells/
---

# Aspose.Cells for .NET : Add Data in Cells


## Aspose.Cells - Add Data in Cells

Aspose.Cells provides a class, `Workbook`, that represents a Microsoft Excel file. `Workbook` class contains a `WorksheetCollection` that allows access to each worksheet in the Excel file. A worksheet is represented by the `Worksheet` class. The `Worksheet` class provides a `Cells`collection. Each item in the `Cells` collection represents an object of the `Cell` class.

**C#**

{{< code lang="c#" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file
Worksheet worksheet = workbook.Worksheets[0];

int x = 1;
for (int i = 1; i <= 15; i++)
{
    for (int j = 0; j < 15; j++)
    {
        worksheet.Cells[i, j].Value = x++;
    }
}

workbook.Save("test.xlsx");

{{< /code >}}

## NPOI HSSF XSSF - Add Data in Cells

In NPOI `row.createCell(1).setCellValue` can be used to add data in cells.

**C#**

{{< code lang="c#" >}}
IWorkbook workbook = new XSSFWorkbook();
ISheet sheet1 = workbook.CreateSheet("Sheet1");
sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");
int x = 1;
for (int i = 1; i <= 15; i++)
{
	IRow row = sheet1.CreateRow(i);
	for (int j = 0; j < 15; j++)
	{
		row.CreateCell(j).SetCellValue(x++);
	}
}
FileStream sw = File.Create("test.xlsx");
workbook.Write(sw);
sw.Close();
{{< /code >}}

## Download Running Code

Download **Add Data in Cells** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1479039)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

For more details, visit [Adding Data to Cells](http://www.aspose.com/docs/display/cellsnet/Adding+Data+to+Cells).

