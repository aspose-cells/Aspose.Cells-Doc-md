---
title: Ruotare il Testo della Cella
type: docs
weight: 100
url: /it/net/rotating-cell-text/
---

{{% alert color="primary" %}}

A volte, l'intestazione di una colonna è molto più ampia dei dati nelle celle sottostanti. Questo può causare spazi vuoti non necessari nella pagina. Una soluzione è ruotare il testo verticalmente in modo che occupi meno spazio orizzontale. In Microsoft Excel, ruotare il testo è semplice. Per fortuna, è possibile ruotare il testo anche in modo programmatico, in modo che gli sviluppatori possano ruotare le etichette nei fogli di calcolo che creano all'interno delle loro applicazioni.

Questo articolo esamina come ruotare il testo nelle celle utilizzando [Aspose.Cells for .NET](/cells/it/net/rotating-cell-text/) rispetto a fare la stessa cosa con [VSTO](/cells/it/net/rotating-cell-text/).

{{% /alert %}}

## **Ruotare il Testo nelle Celle**

Per ruotare il testo in una cella di un foglio di lavoro, eseguire i seguenti passaggi:

1. Creare un libro e ottenere un foglio di lavoro.
1. Aggiungere del testo campione.
1. Formattare il testo: ruotare, aggiungere il colore di sfondo.
1. Salvare il file.

Gli esempi di codice che seguono mostrano come eseguire questi passaggi prima in [VSTO](/cells/it/net/rotating-cell-text/), utilizzando C# o Visual Basic, e poi in [Aspose.Cells](/cells/it/net/rotating-cell-text/), nuovamente utilizzando C# o Visual Basic.

Gli esempi di codice in questo articolo forniscono l'output mostrato di seguito.
**Una cella con testo ruotato.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **Ruotare il testo con VSTO**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2] = "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Ruotare il testo con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 // Instantiate a new Workbook.

 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
