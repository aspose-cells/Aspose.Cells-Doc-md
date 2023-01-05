---
title: Aggiungi collegamenti ipertestuali a Cells
type: docs
weight: 60
url: /it/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET consente di eseguire quasi tutte le attività tramite l'applicazione che un utente può eseguire in Microsoft Excel. Questo articolo confronta come aggiungere un collegamento ipertestuale a una cella in un foglio di lavoro utilizzando VSTO e Aspose.Cells for .NET.

{{% /alert %}}

## **Aggiunta di collegamenti ipertestuali a Cells**

Per aggiungere collegamenti ipertestuali alle celle in un foglio di calcolo, procedi come segue:

1. Imposta il foglio di lavoro:
 1. Creare un'istanza di un oggetto Application.
 (solo VSTO.)
 1. Aggiungi una cartella di lavoro.
 1. Prendi il primo foglio.
 1. Aggiungi testo alle celle a cui aggiungerai un collegamento ipertestuale.
1. Aggiungi collegamento ipertestuale.
1. Salva il documento.

 Questi passaggi sono illustrati negli esempi di codice riportati di seguito. I primi esempi mostrano come utilizzare[VSTO](/cells/it/net/add-hyperlinks-to-cells/) con C# o Visual Basic per aggiungere un collegamento ipertestuale a una cella. Gli esempi che seguono mostrano come fare la stessa cosa usando[Aspose.Cells for .NET](/cells/it/net/add-hyperlinks-to-cells/), sempre usando C# o Visual Basic.

Gli esempi di codice generano un file Excel con un collegamento ipertestuale nella cella A1 del primo foglio di lavoro.

![cose da fare:immagine_alt_testo](add-hyperlinks-to-cells_1.png)

**Un collegamento ipertestuale viene aggiunto alla cella A1.**

### **Aggiunta di collegamenti ipertestuali a Cells con VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aggiunta di collegamenti ipertestuali a Cells con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
