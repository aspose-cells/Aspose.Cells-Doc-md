---
title: Nascondere e scoprire i fogli di lavoro in una cartella di lavoro
type: docs
weight: 80
url: /it/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

Quando si presentano cartelle di lavoro ai clienti o si esegue una presentazione, può essere utile nascondere i fogli di lavoro in una cartella di lavoro. Un approccio strutturato alla modellazione di fogli di calcolo suggerisce che i dati, le formule e le visualizzazioni come i grafici siano conservati su fogli separati. Questo approccio mantiene il layout pulito e semplice e semplifica la navigazione nella cartella di lavoro. Quando si presentano i risultati, è possibile nascondere i dati o i fogli formula per evitare distrazioni.

Gli utenti che lavorano in Excel Microsoft possono facilmente nascondere e quindi mostrare (mostrare) i fogli di lavoro. Le stesse funzionalità sono disponibili per gli sviluppatori che programmano con fogli di calcolo Excel. Esistono diversi modi per lavorare con i fogli di calcolo all'interno delle applicazioni software. Un metodo è usare VSTO, un altro è Aspose.Cells for .NET.

{{% /alert %}}

## **Nascondere e scoprire fogli di lavoro**

 Questo articolo mette a confronto[nascondersi](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) e[scoprire](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) fogli di lavoro con[VSTO](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) , utilizzando C# o Visual Basic, per eseguire la stessa attività con[Aspose.Cells](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/), sempre usando C# o Visual Basic. Aspose.Cells ti consente di lavorare senza Microsoft Excel installato.

I passaggi per nascondere un foglio di lavoro sono:

1. Apri un file.
1. Ottieni un foglio di lavoro.
1. Nascondi il foglio di lavoro.
1. Salva il file.

 A[scoprire](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) di nuovo un foglio di lavoro, attiva semplicemente la visibilità per il foglio nascosto.

 Gli esempi di codice riportati di seguito mostrano innanzitutto come nascondere un foglio di lavoro. I primi campioni mostrano il processo con[VSTO](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) , utilizzando C# o Visual Basic, rispetto a using[Aspose.Cells](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/), sempre usando C# o Visual Basics.

 La seconda serie di esempi di codice mostra la riga utilizzata per scoprire il foglio di lavoro[VSTO](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) o[Aspose.Cells](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Nascondere i fogli di lavoro**

Di seguito sono riportati esempi di codice per VSTO e Aspose.Cells che illustrano come nascondere un foglio di lavoro in una cartella di lavoro.

### **Nascondere i fogli di lavoro con VSTO**

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



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Nascondere i fogli di lavoro con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Scoprire i fogli di lavoro**

Di seguito sono riportati esempi di codice per VSTO e Aspose.Cells che illustrano come mostrare un foglio di lavoro in una cartella di lavoro.

### **Scoprire un foglio di lavoro con VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Scoprire un foglio di lavoro con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
