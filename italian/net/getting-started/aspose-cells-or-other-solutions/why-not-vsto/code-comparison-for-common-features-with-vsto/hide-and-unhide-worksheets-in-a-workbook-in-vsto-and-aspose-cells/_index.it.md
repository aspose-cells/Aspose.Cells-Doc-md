---
title: Nascondi e scopri i fogli di lavoro in una cartella di lavoro in VSTO e Aspose.Cells
type: docs
weight: 140
url: /it/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
Questo articolo confronta l'occultamento e la visualizzazione dei fogli di lavoro con VSTO, usando C# o Visual Basic, con l'esecuzione della stessa attività con Aspose.Cells, sempre usando C# o Visual Basic. Aspose.Cells consente di lavorare senza Microsoft Excel installato.

I passaggi per nascondere un foglio di lavoro sono:

1. Apri un file.
1. Ottieni un foglio di lavoro.
1. Nascondi il foglio di lavoro.
1. Salva il file.
 Per scoprire di nuovo un foglio di lavoro, attiva semplicemente la visibilità per il foglio nascosto.

Gli esempi di codice riportati di seguito mostrano innanzitutto come nascondere un foglio di lavoro. I primi esempi mostrano il processo con VSTO, usando C#, rispetto all'uso di Aspose.Cells, sempre usando C#.

La seconda serie di esempi di codice mostra la riga utilizzata per scoprire il foglio di lavoro in VSTO o Aspose.Cells.
## **Nascondere i fogli di lavoro**
Di seguito sono riportati esempi di codice per VSTO e Aspose.Cells che illustrano come nascondere un foglio di lavoro in una cartella di lavoro.
### **VSTO**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

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

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **Foglio di lavoro nascosto**
Di seguito sono riportati esempi di codice per VSTO e Aspose.Cells che illustrano come mostrare un foglio di lavoro in una cartella di lavoro.
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [SourceForge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/scarica)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).cerniera lampo)
