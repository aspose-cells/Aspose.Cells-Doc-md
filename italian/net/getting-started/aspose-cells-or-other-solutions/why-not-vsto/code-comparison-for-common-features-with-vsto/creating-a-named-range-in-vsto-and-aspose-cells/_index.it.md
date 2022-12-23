---
title: Creazione di un intervallo denominato in VSTO e Aspose.Cells
type: docs
weight: 90
url: /it/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
Per creare un intervallo denominato:

1.  Imposta il foglio di lavoro:
 1. Creare un'istanza di un oggetto Application (solo VSTO).
 1. Aggiungi una cartella di lavoro.
 1. Prendi il primo foglio.
1.  Crea un intervallo denominato:
 1. Definire un intervallo.
 1. Assegna un nome all'intervallo.
 1. Salva il file.

Gli esempi di codice seguenti mostrano come eseguire questi passaggi utilizzando VSTO con C#. Gli esempi di codice che seguono mostrano come eseguire la stessa operazione utilizzando Aspose.Cells for .NET, sempre con C#.
## **VSTO**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

	cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 //Creazione di un'istanza di un oggetto Workbook

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro();

//Accesso al primo foglio di lavoro nel file Excel

Foglio di lavoro foglio di lavoro = workbook.Worksheets[0];

//Creazione di un intervallo denominato

Intervallo intervallo = foglio di lavoro.Cells.CreateRange("A1", "B4");

//Impostazione del nome dell'intervallo denominato

range.Name = "Test_Range";

 for (int riga = 0; riga< range.RowCount; row++)

{

	for (int column = 0; column < range.ColumnCount; column++)

	{

		range[row, column].PutValue("Test");

	}

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [SourceForge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/scarica)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).cerniera lampo)
