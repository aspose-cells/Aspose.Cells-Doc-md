---
title: Avvolgimento Cell Testo
type: docs
weight: 130
url: /it/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

Il testo a capo facilita la lettura: una cella con testo a capo si espande per adattarsi al testo in modo che il testo non venga visualizzato sopra le altre celle.

Con Aspose.Cells for .NET, gli sviluppatori possono eseguire la maggior parte delle attività nelle loro applicazioni che gli utenti possono eseguire con Microsoft Excel, incluso il testo a capo nelle celle. Questo articolo spiega come e confronta l'attività usando VSTO e Aspose.Cells. Aspose.Cells è ottimizzato per una codifica efficiente e funziona senza Microsoft Automation.

{{% /alert %}}

## **Avvolgimento Cell Testo**

Per creare un foglio di lavoro con due celle, una con testo a capo e una senza:

1. Imposta il foglio di lavoro:
 1. Crea una cartella di lavoro.
 1. Accedi al primo foglio di lavoro.
1. Aggiungi testo:
 1. Aggiungi testo alla cella A1.
 1. Aggiungi testo a capo alla cella A5.
1. Salva il foglio di calcolo.

 Gli esempi di codice seguenti mostrano come eseguire questi passaggi utilizzando[VSTO](/cells/it/net/wrapping-cell-text/) con C# o Visual Basic. Esempi di codice che mostrano come eseguire la stessa operazione utilizzando[Aspose.Cells for .NET](/cells/it/net/wrapping-cell-text/), sempre usando C# o Visual Basic segui subito dopo.

L'esecuzione del codice genera un foglio di calcolo con due celle, una con testo che non è stato racchiuso e una con:

|<p>**Output del testo della cella di wrapping con VSTO** </p><p>![cose da fare:immagine_alt_testo](wrapping-cell-text_1.png)</p>|<p>**Emetti il testo della cella di wrapping con Aspose.Cells for .NET** </p><p>![cose da fare:immagine_alt_testo](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **A capo Cell Testo con VSTO**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

    //Access vsto application

    Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

    //Access workbook 

    Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

    //Access worksheet 

    Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

    //Access vsto worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

    //Place some text in cell A1 without wrapping

    Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

    cellA1.Value = "Sample Text Unwrapped";

    //Place some text in cell A5 with wrapping

    Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

    cellA5.Value = "Sample Text Wrapped";

    cellA5.WrapText = true;

    //Save the workbook

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **A capo Cell Testo Usando Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

{

    //Create workbook

    Workbook workbook = new Workbook();

    //Access worksheet

    Worksheet worksheet = workbook.Worksheets[0];

    //Place some text in cell A1 without wrapping

    Cell cellA1 = worksheet.Cells["A1"];

    cellA1.PutValue("Some Text Unwrapped");

    //Place some text in cell A5 wrapping

    Cell cellA5 = worksheet.Cells["A5"];

    cellA5.PutValue("Some Text Wrapped");

    Style style = cellA5.GetStyle();

    style.IsTextWrapped = true;

    cellA5.SetStyle(style);

    //Autofit rows

    worksheet.AutoFitRows();

    //Save the workbook

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
