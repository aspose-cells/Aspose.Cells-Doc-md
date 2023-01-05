---
title: Creazione di un intervallo denominato
type: docs
weight: 70
url: /it/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET consente agli sviluppatori di eseguire la maggior parte delle attività che gli utenti possono eseguire in Microsoft Excel tramite le loro applicazioni. Questo articolo spiega come applicare un intervallo denominato a livello di codice.

Un intervallo denominato è una funzionalità di Excel che consente di assegnare un nome a una cella o a un intervallo di celle in un foglio di calcolo di Excel. È quindi possibile utilizzare il nome nelle formule per fare riferimento alla cella (o all'intervallo). Intervalli con nomi sensati rendono le formule più facili da capire.

Un intervallo denominato deve essere univoco all'interno del suo ambito, quindi non utilizzare lo stesso nome per diversi intervalli in un foglio di lavoro. I nomi di intervallo descrittivi aiutano a evitarlo: ad esempio, OrderSubTotal è più descrittivo di SubTotal e ha anche meno probabilità di essere duplicato su un foglio.

{{% /alert %}}

## **Creazione di un intervallo denominato**

Per creare un intervallo denominato:

1. Imposta il foglio di lavoro:
 1. Creare un'istanza di un oggetto Application.
 (solo VSTO.)
 1. Aggiungi una cartella di lavoro.
 1. Prendi il primo foglio.
1. Crea un intervallo denominato:
 1. Definire un intervallo.
 1. Assegna un nome all'intervallo.
1. Salva il file.

 Gli esempi di codice seguenti mostrano come eseguire questi passaggi utilizzando[VSTO](/cells/it/net/creating-a-named-range/) con C# o Visual Basic. Gli esempi di codice che seguono mostrano come eseguire la stessa operazione utilizzando[Aspose.Cells for .NET](/cells/it/net/creating-a-named-range/), sempre con C# o Visual Basic.
### **Creazione di un intervallo denominato con VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

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

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Creazione di un intervallo denominato con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

utilizzando il numero Aspose.Cells;

.......


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

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
