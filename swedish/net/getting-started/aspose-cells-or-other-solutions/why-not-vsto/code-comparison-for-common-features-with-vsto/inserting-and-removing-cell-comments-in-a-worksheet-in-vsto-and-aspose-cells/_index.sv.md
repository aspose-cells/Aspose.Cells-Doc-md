---
title: Infoga och ta bort Cell kommentarer i ett arbetsblad i VSTO och Aspose.Cells
type: docs
weight: 150
url: /sv/net/inserting-and-removing-cell-comments-in-a-worksheet-in-vsto-and-aspose-cells/
---
Så här lägger du till kommentarer till celler:

1. Öppna en befintlig Excel-fil.
1. Lägg till en kommentar till en cell.
1. Spara filen.

För att ta bort kommentarerna är processen liknande, med undantag för att kommentaren tas bort.

Kodexemplen nedan illustrerar först hur man lägger till en kommentar och sedan hur man tar bort en kommentar med antingen VSTO eller Aspose.Cells for .NET.
## **Lägger in kommentarer**
Dessa kodavsnitt visar hur man lägger till en kommentar till en cell först med VSTO (C#) och sedan med Aspose.Cells for .NET (C#).
### **VSTO**
{{< highlight "csharp" >}}

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

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

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

{{< /highlight >}}
## **Ta bort kommentarer**
För att ta bort en kommentar från en cell, använd följande kodrader för VSTO (C#) och Aspose.Cells for .NET (C#).
### **VSTO**
{{< highlight "csharp" >}}

 //Remove the comment.

  rng1.Comment.Delete();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //removing comments

 workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
## **Ladda ner provkod**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).blixtlås)
