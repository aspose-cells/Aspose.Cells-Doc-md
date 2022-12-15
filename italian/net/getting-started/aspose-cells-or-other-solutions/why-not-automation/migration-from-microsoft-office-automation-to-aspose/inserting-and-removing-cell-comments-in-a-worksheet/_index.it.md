---
title: Inserimento e rimozione di commenti Cell in un foglio di lavoro
type: docs
weight: 30
url: /it/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

In genere, i commenti vengono utilizzati per aggiungere ulteriori informazioni alle celle in un foglio di lavoro. Li usiamo ogni tanto e li cancelliamo quando non ne abbiamo più bisogno. I commenti sono utili se devi documentare un valore particolare o per aiutarti a ricordare cosa fa una formula. Quando sposti il puntatore del mouse su una cella che contiene un commento, il commento viene visualizzato in una piccola casella.

In questo articolo, confrontiamo come aggiungere e rimuovere commenti dalle celle utilizzando VSTO e Aspose.Cells for .NET. Aspose.Cells for .NET funziona con i file di Microsoft Excel indipendentemente da Office Automation e offre potenti strumenti per la creazione e la manipolazione di fogli di calcolo.

{{% /alert %}}

## **Aggiunta e rimozione di commenti su Cells**

Per aggiungere commenti alle celle:

1. Apri un file Excel esistente.
1. Aggiungi un commento a una cella.
1. Salva il file.

Per rimuovere i commenti, il processo è simile, con l'eccezione che il commento viene rimosso.

 Gli esempi di codice seguenti illustrano innanzitutto come[Aggiungi un commento](/cells/it/net/inserting-and-removing-cell-comments-in-a-worksheet/) e poi come[rimuovere un commento](/cells/it/net/inserting-and-removing-cell-comments-in-a-worksheet/) con VSTO o Aspose.Cells for .NET.

## **Inserimento di commenti**

 Questi frammenti di codice mostrano come aggiungere prima un commento a una cella con[VSTO](/cells/it/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) e poi con[Aspose.Cells for .NET](/cells/it/net/inserting-and-removing-cell-comments-in-a-worksheet/) (Do#, VB).

### **Inserimento di un commento con VSTO**

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

### **Inserimento di un commento con Aspose.Cells for .NET**

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

## **Rimozione di commenti**

 Per rimuovere un commento da una cella, utilizzare le seguenti righe di codice per[VSTO](/cells/it/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) e[Aspose.Cells](/cells/it/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C#, VB).

### **Rimozione di un commento con VSTO**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Rimozione di un commento con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
