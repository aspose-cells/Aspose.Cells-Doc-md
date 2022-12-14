---
title: Einfügen und Entfernen von Cell-Kommentaren in einem Arbeitsblatt
type: docs
weight: 30
url: /de/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

Im Allgemeinen werden Kommentare verwendet, um zusätzliche Informationen zu Zellen in einem Arbeitsblatt hinzuzufügen. Wir verwenden sie hin und wieder und löschen sie, wenn wir sie nicht mehr benötigen. Kommentare sind nützlich, wenn Sie einen bestimmten Wert dokumentieren müssen oder um sich daran zu erinnern, was eine Formel bewirkt. Wenn Sie den Mauszeiger über eine Zelle bewegen, die einen Kommentar enthält, wird der Kommentar in einem kleinen Feld angezeigt.

In diesem Artikel vergleichen wir das Hinzufügen und Entfernen von Kommentaren aus Zellen mit VSTO und Aspose.Cells for .NET. Aspose.Cells for .NET funktioniert mit Microsoft Excel-Dateien unabhängig von Office Automation und bietet Ihnen leistungsstarke Tools zum Erstellen und Bearbeiten von Tabellenkalkulationen.

{{% /alert %}}

## **Hinzufügen und Entfernen von Kommentaren zu Cells**

So fügen Sie Kommentare zu Zellen hinzu:

1. Öffnen Sie eine vorhandene Excel-Datei.
1. Fügen Sie einer Zelle einen Kommentar hinzu.
1. Speicher die Datei.

Um die Kommentare zu entfernen, ist der Vorgang ähnlich, mit der Ausnahme, dass der Kommentar entfernt wird.

 Die folgenden Codebeispiele veranschaulichen zunächst, wie das geht[Einen Kommentar hinzufügen](/cells/de/net/inserting-and-removing-cell-comments-in-a-worksheet/) und dann wie[einen Kommentar entfernen](/cells/de/net/inserting-and-removing-cell-comments-in-a-worksheet/) entweder mit VSTO oder Aspose.Cells for .NET.

## **Kommentare einfügen**

 Diese Codeschnipsel zeigen, wie man zuerst mit einen Kommentar zu einer Zelle hinzufügt[VSTO](/cells/de/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) und dann mit[Aspose.Cells for .NET](/cells/de/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **Einfügen eines Kommentars mit VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **Einfügen eines Kommentars mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **Kommentare entfernen**

 Um einen Kommentar aus einer Zelle zu entfernen, verwenden Sie die folgenden Codezeilen für[VSTO](/cells/de/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) und[Aspose.Cells](/cells/de/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C#, VB).

### **Entfernen eines Kommentars mit VSTO**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Entfernen eines Kommentars mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
