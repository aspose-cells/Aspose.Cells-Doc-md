---
title: Wrapping Cell Testo in VSTO e Aspose.Cells
type: docs
weight: 250
url: /it/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---
Per creare un foglio di lavoro con due celle, una con testo a capo e una senza:

1.  Imposta il foglio di lavoro:
 1. Crea una cartella di lavoro.
 1. Accedi al primo foglio di lavoro.
1.  Aggiungi testo:
 1. Aggiungi testo alla cella A1.
 1. Aggiungi testo a capo alla cella A5.
1. Salva il foglio di calcolo.
 Gli esempi di codice seguenti mostrano come eseguire questi passaggi usando VSTO con C#. Gli esempi di codice che mostrano come eseguire la stessa operazione utilizzando Aspose.Cells for .NET, sempre utilizzando C# seguono immediatamente dopo.

L'esecuzione del codice genera un foglio di calcolo con due celle, una con testo che non è stato racchiuso e una con:

## **Output utilizzando VSTO Excel**

![cose da fare:immagine_alt_testo](picture1.png)

## **Uscita utilizzando Aspose.Cells for .NET**

![cose da fare:immagine_alt_testo](picture2.png)

## **VSTO**

{{< highlight "csharp" >}}

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

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 private static void WrappingCellText()

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

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Scarica il codice di esempio**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [SourceForge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/scarica)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).cerniera lampo)
