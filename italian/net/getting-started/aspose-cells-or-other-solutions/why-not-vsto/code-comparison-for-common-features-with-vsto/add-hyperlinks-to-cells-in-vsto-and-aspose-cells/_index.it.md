---
title: Aggiungi collegamenti ipertestuali a Cells in VSTO e Aspose.Cells
type: docs
weight: 20
url: /it/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
Per aggiungere collegamenti ipertestuali alle celle in un foglio di calcolo, procedi come segue:

1.  Imposta il foglio di lavoro:
 1. Creare un'istanza di un oggetto Application (solo VSTO).
 1. Aggiungi una cartella di lavoro.
 1. Prendi il primo foglio.
 1. Aggiungi testo alle celle a cui aggiungerai un collegamento ipertestuale.
1. Aggiungi collegamento ipertestuale.
1. Salva il documento.

Questi passaggi sono illustrati negli esempi di codice riportati di seguito. I primi esempi mostrano come usare VSTO con C# per aggiungere un collegamento ipertestuale a una cella. Gli esempi che seguono mostrano come fare la stessa cosa usando Aspose.Cells for .NET, sempre usando C#.

Gli esempi di codice generano un file Excel con un collegamento ipertestuale nella cella A1 del primo foglio di lavoro.

![cose da fare:immagine_alt_testo](picture1.png)

Un collegamento ipertestuale viene aggiunto alla cella A1.

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

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

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

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

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Scarica il codice di esempio**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [SourceForge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/scarica)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).cerniera lampo)
