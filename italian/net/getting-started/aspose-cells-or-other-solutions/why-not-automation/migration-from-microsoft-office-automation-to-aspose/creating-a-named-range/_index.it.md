---
title: Creazione di un intervallo denominato
type: docs
weight: 70
url: /it/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET consente agli sviluppatori di svolgere la maggior parte delle attività che gli utenti possono svolgere in Microsoft Excel tramite le loro applicazioni. Questo articolo spiega come applicare un intervallo denominato tramite programmazione.

Un intervallo denominato è una funzione di Excel che consente di assegnare un nome a una cella o a un intervallo di celle in un foglio di calcolo di Excel. È quindi possibile utilizzare il nome nelle formule per fare riferimento alla cella (o all'intervallo). Gli intervalli denominati in modo sensato rendono più semplici da comprendere le formule.

Un intervallo denominato deve essere univoco all'interno del suo ambito, quindi non utilizzare lo stesso nome per diversi intervalli in un foglio di calcolo. I nomi degli intervalli descrittivi aiutano ad evitare ciò: ad esempio, OrderSubTotal è più descrittivo di SubTotal e anche meno probabile che venga duplicato in un foglio.

{{% /alert %}}

## **Creazione di un intervallo denominato**

Per creare un intervallo denominato:

1. Configura il foglio di lavoro:
   1. Istanziare un oggetto Application.
      (Solo VSTO.)
   1. Aggiungi un foglio di lavoro.
   1. Ottieni il primo foglio.
1. Crea un intervallo nominato:
   1. Definisci un intervallo.
   1. Dà un nome all'intervallo.
1. Salvare il file.

Gli esempi di codice qui sotto mostrano come eseguire questi passaggi utilizzando [VSTO](/cells/it/net/creating-a-named-range/) con C# o Visual Basic. Gli esempi di codice che seguono mostrano come fare la stessa cosa utilizzando [Aspose.Cells for .NET](/cells/it/net/creating-a-named-range/), di nuovo con C# o Visual Basic.
### **Creazione di un intervallo nominato con VSTO**

**C#**

{{< highlight csharp >}}

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

### **Creazione di un intervallo nominato con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
