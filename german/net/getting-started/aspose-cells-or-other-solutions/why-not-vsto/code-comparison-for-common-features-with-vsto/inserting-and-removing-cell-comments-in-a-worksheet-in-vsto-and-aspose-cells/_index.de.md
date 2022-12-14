---
title: Einfügen und Entfernen von Cell-Kommentaren in einem Arbeitsblatt in VSTO und Aspose.Cells
type: docs
weight: 150
url: /de/net/inserting-and-removing-cell-comments-in-a-worksheet-in-vsto-and-aspose-cells/
---
So fügen Sie Kommentare zu Zellen hinzu:

1. Öffnen Sie eine vorhandene Excel-Datei.
1. Fügen Sie einer Zelle einen Kommentar hinzu.
1. Speicher die Datei.

Um die Kommentare zu entfernen, ist der Vorgang ähnlich, mit der Ausnahme, dass der Kommentar entfernt wird.

Die folgenden Codebeispiele veranschaulichen zuerst, wie Sie einen Kommentar hinzufügen und dann einen Kommentar entweder mit VSTO oder Aspose.Cells for .NET entfernen.
## **Kommentare einfügen**
Diese Codeausschnitte zeigen, wie Sie einer Zelle zuerst mit VSTO (C#) und dann mit Aspose.Cells for .NET (C#) einen Kommentar hinzufügen.
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
## **Kommentare entfernen**
Um einen Kommentar aus einer Zelle zu entfernen, verwenden Sie die folgenden Codezeilen für VSTO (C#) und Aspose.Cells for .NET (C#).
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
## **Beispielcode herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
- [Quellenschmiede](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/herunterladen)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).Postleitzahl)
