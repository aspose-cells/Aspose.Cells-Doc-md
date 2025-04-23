---
title: Nascondi e mostra fogli di lavoro in un file di lavoro
type: docs
weight: 80
url: /it/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

Quando si presentano file di lavoro ai clienti, o si fa una presentazione, può essere utile nascondere i fogli di lavoro in un file di lavoro. Un approccio strutturato alla modellazione dei fogli di calcolo suggerisce che i dati, le formule e le visualizzazioni come i grafici siano mantenuti su fogli separati. Questo approccio mantiene pulito e semplice il layout e rende il file di lavoro più facile da navigare. Quando si presentano risultati, potresti voler nascondere i fogli di dati o di formule dalla vista per evitare distrazioni.

Gli utenti che lavorano in Microsoft Excel, possono facilmente nascondere e quindi mostrare (mostrare) i fogli di lavoro. Le stesse funzionalità sono disponibili per gli sviluppatori che programmano con fogli di calcolo di Excel. Ci sono diversi modi di lavorare con fogli di calcolo all'interno delle applicazioni software. Un metodo è utilizzare VSTO, un altro è Aspose.Cells for .NET.

{{% /alert %}}

## **Nascondere e mostrare fogli di lavoro**

Questo articolo confronta la [nascosta](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) e l'[impostazione a vista](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) dei fogli di lavoro con [VSTO](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/), utilizzando C# o Visual Basic, per eseguire lo stesso compito con [Aspose.Cells](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/), di nuovo utilizzando C# o Visual Basic. Aspose.Cells ti consente di lavorare senza avere installato Microsoft Excel.

I passaggi per nascondere un foglio di lavoro sono:

1. Apri un file.
1. Ottieni un foglio di lavoro.
1. Nascondi il foglio di lavoro.
1. Salvare il file.

Per [mostrare](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) di nuovo un foglio di lavoro, attiva semplicemente la visibilità per il foglio nascosto.

I campioni di codice di seguito mostrano prima come nascondere un foglio di lavoro. I primi campioni mostrano il processo con [VSTO](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/), utilizzando sia C# sia Visual Basic, rispetto all'utilizzo di [Aspose.Cells](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/), ancora utilizzando sia C# sia Visual Basics.

Il secondo insieme di campioni di codice mostra la riga utilizzata per mostrare di nuovo il foglio di lavoro in [VSTO](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/) o [Aspose.Cells](/cells/it/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Nascondere i fogli di lavoro**

Di seguito sono riportati esempi di codice per VSTO e Aspose.Cells che illustrano come nascondere un foglio di lavoro in un workbook.

### **Nascondere i fogli di lavoro con VSTO**

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

{{< highlight csharp >}}



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

## **Mostrare fogli di lavoro nascosti**

Di seguito sono riportati esempi di codice per VSTO e Aspose.Cells che illustrano come mostrare di nuovo un foglio di lavoro in un workbook.

### **Mostrare di nuovo un foglio di lavoro con VSTO**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Mostrare di nuovo un foglio di lavoro con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
