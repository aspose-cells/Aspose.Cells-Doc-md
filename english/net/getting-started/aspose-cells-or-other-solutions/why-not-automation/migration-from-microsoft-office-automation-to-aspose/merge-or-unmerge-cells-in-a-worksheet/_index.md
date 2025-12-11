---
title: Merge or UnMerge Cells in a Worksheet
type: docs
weight: 40
url: /net/merge-or-unmerge-cells-in-a-worksheet/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

While working with worksheets, you often need to create a title/heading in a single cell that spans the top of your worksheet. You might be creating an invoice and want fewer columns for the total or summary values. When you want to make one cell out of two or more cells, you merge the cells. We carry out the task using VSTO and Aspose.Cells for .NET independently.

{{% /alert %}}

## **Description**

Open an existing Excel file, merge some cells in the first worksheet of the workbook, and save the Excel file.

## **Merging Cells**

Following are the parallel code snippets for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.
Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template Excel file path.
string myPath=@"d:\test\MyBook.xls";

//Open the Excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value,
Missing.Value, Missing.Value);

//Get the range of cells, i.e., A1:C1.
Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.
rng1.Merge(Missing.Value);

//Save the file.
excelApp.ActiveWorkbook.Save();

//Quit the Application.
excelApp.Quit();

{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......
using Aspose.Cells;
.......

//Instantiate a new Workbook.
Workbook workbook = new Workbook();

//Specify the template Excel file path.
string myPath=@"d:\test\MyBook.xls";

//Open the Excel file.
workbook.Open(myPath);

//Get the range of cells, i.e., A1:C1.
Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.
rng1.Merge();

//Save the file.
workbook.Save(@"d:\test\MyBook.xls");

{{< /highlight >}}

## **Unmerging the Cells**

To unmerge the cell(s), use the following lines of code for VSTO (C#, VB) and Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (merged cell).
Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

 //Unmerge the cell.
rng1.UnMerge();    

{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (merged cell).
Cells rng1 = workbook.Worksheets[0].Cells;

 //Unmerge the cell.
rng1.UnMerge(0, 0, 1, 3);  

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
