+++
title = "Create and Save New Workbooks" 
description = "" 
weight = 16795 
+++

Aspose.Cells for .NET : Create and Save New Workbooks  

# Aspose.Cells for .NET : Create and Save New Workbooks


##### Migration Tips:

1\. Create Workbook object  
2\. Get current Worksheet.  
3\. Insert some text in any cell.  
4\. Save the Workbook.

#### VSTO

Below is code example for VSTO

{{< code lang="cs" >}}
 Excel.Workbook newWorkbook = this.Application.Workbooks.Add();
 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;
 Excel.Range cells = worksheet.Cells;
 cells.set_Item(1,1,"Some Text");
 newWorkbook.Save();
{{< /code >}}

#### Aspose.Cells

Below is code example for Aspose.Cells

{{< code lang="cs" >}}
 Workbook newWorkbook = new Workbook();
 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");
 Cells cells = worksheet.Cells;
 cells[0,0].PutValue("Some Text");
 newWorkbook.Save(fileName);
{{< /code >}}

##### Download

*   [CodePlex](https://asposevsto.codeplex.com/downloads/get/1459765)
*   [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)

