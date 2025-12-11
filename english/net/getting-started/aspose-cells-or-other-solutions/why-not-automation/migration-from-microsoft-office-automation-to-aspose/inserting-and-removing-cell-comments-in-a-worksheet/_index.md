---
title: Inserting and Removing Cell Comments in a Worksheet
type: docs
weight: 30
url: /net/inserting-and-removing-cell-comments-in-a-worksheet/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Generally, comments are used to add additional information to cells in a worksheet. We use them every now and then and we delete them when we do not need them any longer. Comments are useful if you need to document a particular value or to help you remember what a formula does. When you move the mouse pointer over a cell that has a comment, the comment pops up in a small box.

In this article, we compare how to add and remove comments from cells using VSTO and Aspose.Cells for .NET. Aspose.Cells for .NET works with Microsoft Excel files independently of Office Automation and gives you powerful tools for creating and manipulating spreadsheets.

{{% /alert %}}

## **Adding and Removing Comments on Cells**

To add comments to cells:

1. Open an existing Excel file.  
2. Add a comment to a cell.  
3. Save the file.

To remove the comments, the process is similar, with the exception that the comment is removed.

The code samples below illustrate first how to [add a comment](/cells/net/inserting-and-removing-cell-comments-in-a-worksheet/) and then how to [remove a comment](/cells/net/inserting-and-removing-cell-comments-in-a-worksheet/) with either VSTO or Aspose.Cells for .NET.

## **Inserting Comments**

These code snippets show how to add a comment to a cell first with [VSTO](/cells/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) and then with [Aspose.Cells for .NET](/cells/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **Inserting a Comment with VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using System.Reflection;

.......

// Instantiate the Application object.
Excel.Application excelApp = new Excel.ApplicationClass();

// Specify the template Excel file path.
string myPath = @"d:\test\Book1.xls";

// Open the Excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value);

// Get the A1 cell.
Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

// Add the comment with text.
rng1.AddComment("This is my comment");

// Save the file.
excelApp.ActiveWorkbook.Save();

// Quit the Application.
excelApp.Quit();

{{< /highlight >}}

### **Inserting a Comment with Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;
.......

// Specify the template Excel file path.
string myPath = @"d:\test\Book1.xls";

// Instantiate a new Workbook and open the Excel file.
Workbook workbook = new Workbook(myPath);

// Add a comment to the A1 cell.
int commentIndex = workbook.Worksheets[0].Comments.Add("A1");

// Access the newly added comment.
Comment comment = workbook.Worksheets[0].Comments[commentIndex];

// Set the comment note.
comment.Note = "This is my comment";

// Save the Excel file.
workbook.Save(@"d:\test\Book1.xls");

{{< /highlight >}}

## **Removing Comments**

To remove a comment from a cell, use the following lines of code for [VSTO](/cells/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) and [Aspose.Cells](/cells/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C#, VB).

### **Removing a Comment with VSTO**

**C#**

{{< highlight csharp >}}

 // Remove the comment.
 rng1.Comment.Delete();

{{< /highlight >}}

### **Removing a Comment with Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 // Remove the comment.
 workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
