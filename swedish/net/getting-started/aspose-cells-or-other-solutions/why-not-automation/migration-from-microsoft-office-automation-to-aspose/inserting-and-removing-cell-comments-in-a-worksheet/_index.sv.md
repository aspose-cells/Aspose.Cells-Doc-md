---
title: Infoga och ta bort Cell Kommentarer i ett arbetsblad
type: docs
weight: 30
url: /sv/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

I allmänhet används kommentarer för att lägga till ytterligare information till celler i ett kalkylblad. Vi använder dem då och då och vi raderar dem när vi inte behöver dem längre. Kommentarer är användbara om du behöver dokumentera ett visst värde eller för att hjälpa dig komma ihåg vad en formel gör. När du flyttar muspekaren över en cell som har en kommentar, dyker kommentaren upp i en liten ruta.

I den här artikeln jämför vi hur du lägger till och tar bort kommentarer från celler med VSTO och Aspose.Cells för .NET. Aspose.Cells för .NET fungerar med Microsoft Excel-filer oberoende av Office Automation och ger dig kraftfulla verktyg för att skapa och manipulera kalkylblad.

{{% /alert %}}

## **Lägga till och ta bort kommentarer på Cells**

Så här lägger du till kommentarer till celler:

1. Öppna en befintlig Excel-fil.
1. Lägg till en kommentar till en cell.
1. Spara filen.

För att ta bort kommentarerna är processen liknande, med undantag för att kommentaren tas bort.

 Kodexemplen nedan illustrerar först hur man gör[Lägg till en kommentar](/cells/sv/net/inserting-and-removing-cell-comments-in-a-worksheet/)och sedan hur[ta bort en kommentar](/cells/sv/net/inserting-and-removing-cell-comments-in-a-worksheet/) med antingen VSTO eller Aspose.Cells för .NET.

## **Lägger in kommentarer**

 Dessa kodavsnitt visar hur man lägger till en kommentar till en cell först med[VSTO](/cells/sv/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) och sedan med[Aspose.Cells för .NET](/cells/sv/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **Infoga en kommentar med VSTO**

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

### **Infoga en kommentar med Aspose.Cells för .NET**

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

## **Ta bort kommentarer**

 För att ta bort en kommentar från en cell, använd följande kodrader för[VSTO](/cells/sv/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) och[Aspose.Cells](/cells/sv/net/inserting-and-removing-cell-comments-in-a-worksheet/) för .NET (C#, VB).

### **Ta bort en kommentar med VSTO**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Ta bort en kommentar med Aspose.Cells för .NET**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
