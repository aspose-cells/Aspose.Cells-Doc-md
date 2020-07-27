+++
title = "Create New Workbook" 
description = "" 
weight = 20925 
+++

Aspose.Cells for .NET : Create New Workbook  

# Aspose.Cells for .NET : Create New Workbook


## Aspose.Cells - Create New Workbook

`Workbook` class is available for simple use

**C#**

{{< code lang="c#" >}}
Workbook workbook = new Workbook(); // Creating a Workbook object
workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats
{{< /code >}}

## NPOI - HSSF XSSF - Create New Workbook

Create new Workbook using `Workbook` class and save using `FileOutputStream`.

**C#**

{{< code lang="c#" >}}
IWorkbook workbook = new XSSFWorkbook();
workbook.CreateSheet("Sheet A1");
workbook.CreateSheet("Sheet A2");
workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");
workbook.Write(sw);
sw.Close();
{{< /code >}}

## Download Running Code

Download **Create New Workbook** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1479038)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)

For more details, visit [File Handling Features](http://www.aspose.com/docs/display/cellsnet/File+Handling+Features).

