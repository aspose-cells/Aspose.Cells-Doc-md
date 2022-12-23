---
title: Aggiunta di nuovi fogli di lavoro alla cartella di lavoro e attivazione di un foglio
type: docs
weight: 10
url: /it/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

Quando si lavora con un file modello, a volte è necessario aggiungere altri fogli di lavoro alla cartella di lavoro per raccogliere i dati. Le nuove celle verranno riempite con dati in posizioni e posizioni specificate in ogni foglio di lavoro.

Allo stesso modo, potrebbe essere necessario che un foglio di lavoro specifico sia attivo e visualizzato per primo quando il file viene aperto in Microsoft Excel. Un "foglio attivo" è il foglio su cui stai lavorando in una cartella di lavoro. Il nome sulla scheda del foglio attivo è in grassetto per impostazione predefinita.

 L'aggiunta di fogli di lavoro e l'impostazione del foglio attivo sono attività comuni e semplici che gli sviluppatori devono sapere come eseguire. In questo articolo, svolgiamo queste attività utilizzando[VSTO](/cells/it/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) e[Aspose.Cells for .NET](/cells/it/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Aggiunta di fogli di lavoro e attivazione di un foglio**
Ai fini di questo suggerimento per la migrazione:

1. Aggiungi nuovi fogli di lavoro a un file Excel Microsoft esistente.
1. Inserisci i dati nelle celle di ogni nuovo foglio di lavoro.
1. Attiva un foglio nella cartella di lavoro.
1. Salva come file Excel Microsoft.

Di seguito sono riportati frammenti di codice paralleli per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB), che mostrano come eseguire queste attività.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

utilizzando Microsoft.VisualStudio.Tools.Applications.Runtime;

utilizzando Excel = Microsoft.Office.Interop.Excel;

utilizzando Office = Microsoft.Office.Core;

usando System.Reflection;

.......

//Crea un'istanza dell'oggetto Application.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specifica il percorso del file excel del modello.

string myPath = @"d:\test\My_Book1.xls";

//Apri il file excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.Mancante, Valore.Mancante);

//Dichiara un oggetto foglio di lavoro.

Excel.Foglio di lavoro nuovoFoglio di lavoro;

//Aggiungi 5 nuovi fogli di lavoro alla cartella di lavoro e inserisci alcuni dati

//nelle celle.

 per (int i = 1; i< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**V.B**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

utilizzando il numero Aspose.Cells;

.......

//Crea un'istanza di licenza e imposta il file di licenza

//attraverso il suo percorso

Aspose.Cells.License licenza = new Aspose.Cells.License();

licenza.SetLicense("Aspose.Cells.lic");

//Specifica il percorso del file excel del modello.

string myPath =@"d:\test\My_Book1.xls";

//Crea un'istanza di una nuova cartella di lavoro.

//Apri il file excel.

Cartella di lavoro cartella di lavoro = new Cartella di lavoro(myPath);

//Dichiara un oggetto foglio di lavoro.

Foglio di lavoro nuovoFoglio di lavoro;

//Aggiungi 5 nuovi fogli di lavoro alla cartella di lavoro e inserisci alcuni dati

//nelle celle.

 per (int i = 0; i< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**V.B**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
