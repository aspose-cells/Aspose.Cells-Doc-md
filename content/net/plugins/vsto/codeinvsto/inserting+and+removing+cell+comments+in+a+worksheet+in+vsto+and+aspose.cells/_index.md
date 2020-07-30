---
title : "Inserting and Removing Cell Comments in a Worksheet in VSTO and Aspose.Cells" 
description : "" 
weight : 16803 
toc : false
type: docs
url: /net/plugins/vsto/codeinvsto/inserting+and+removing+cell+comments+in+a+worksheet+in+vsto+and+aspose.cells/
---

# Aspose.Cells for .NET : Inserting and Removing Cell Comments in a Worksheet in VSTO and Aspose.Cells


To add comments to cells:

1.  Open an existing Excel file.
2.  Add a comment to a cell.
3.  Save the file.

To remove the comments, the process is similar, with the exception that the comment is removed.

The code samples below illustrate first how to add a comment and then how to remove a comment with either VSTO or Aspose.Cells for .NET.

## Inserting Comments

These code snippets show how to add a comment to a cell first with VSTO (C#) and then with Aspose.Cells for .NET (C#).

### VSTO

{{< code lang="cs" >}}
//Instantiate the Application object.
 Excel.Application excelApp = Application;

//Specify the template excel file path.
  string myPath = "Book1.xls";

//Open the excel file.
 excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
            Missing.Value, Missing.Value,
            Missing.Value, Missing.Value,
            Missing.Value, Missing.Value,
            Missing.Value, Missing.Value,
            Missing.Value, Missing.Value,
            Missing.Value, Missing.Value);

//Get the A1 cell.
 Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.
 rng1.AddComment("This is my comment");

//Save the file.
  excelApp.ActiveWorkbook.Save();
//Quit the Application.
  excelApp.Quit();
{{< /code >}}

### Aspose.Cells

{{< code lang="cs" >}}
//Specify the template excel file path.
string myPath = "Book1.xls";

//Instantiate a new Workbook.
//Open the excel file.
 Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.
 int commentIndex = workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment
 Comment comment = workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note
 comment.Note = "This is my comment";
//Save As the excel file.
 workbook.Save("Book1.xls");
{{< /code >}}

## Removing Comments

To remove a comment from a cell, use the following lines of code for VSTO (C#) and Aspose.Cells for .NET (C#).

### VSTO

{{< code lang="cs" >}}
//Remove the comment.
  rng1.Comment.Delete();

{{< /code >}}

### Aspose.Cells

{{< code lang="cs" >}}
//removing comments
 workbook.Worksheets[0].Comments.RemoveAt("A1");
{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposevsto.codeplex.com/downloads/get/1459781)
*   [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
*   [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20(Aspose.Cells).zip/download)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20(Aspose.Cells).zip)

