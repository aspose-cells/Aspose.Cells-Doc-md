---
title: Aggiungere Bordi alle Celle in un Foglio di Lavoro
type: docs
weight: 50
url: /it/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET ti permette di eseguire quasi qualsiasi attività tramite la tua applicazione che un utente può fare in Microsoft Excel. Aspose.Cells è performante e robusto e ha il vantaggio di funzionare in modo indipendente da Microsoft Automation. Questo articolo mostra come aggiungere bordi alle celle in un foglio di lavoro utilizzando Aspose.Cells for .NET rispetto a VSTO.

{{% /alert %}}

## **Aggiungere Bordi alle Celle**

Per aggiungere bordi alle celle in un foglio di calcolo, seguire i seguenti passaggi:

1. Configura il foglio di lavoro:
   1. Istanziare un oggetto Application.
      (Solo VSTO.)
   1. Aggiungi un foglio di lavoro.
   1. Ottieni il primo foglio.
   1. Aggiungere testo alle celle a cui si aggiungeranno i bordi.
1. Aggiungere i bordi:
   1. Definisci un intervallo.
   1. Applica uno stile di bordo all'intervallo.
      Ripeti per ciascun intervallo e per ciascuno stile di bordo che desideri impostare. Questo esempio applica linee sottili, sottili, medie e spesse.
1. Fine:
   1. Adatta automaticamente la larghezza della colonna in cui si trovano le celle per adattare il testo in modo ordinato.
   1. Salvare il documento.

Questi passaggi sono mostrati nel codice sottostante. I primi esempi di codice mostrano come implementarli utilizzando [VSTO](/cells/it/net/add-borders-to-cells-in-a-worksheet/) sia in C# che in Visual Basic. Dopo gli esempi VSTO ci sono esempi che mostrano come eseguire gli stessi passaggi utilizzando [Aspose.Cells for .NET](/cells/it/net/add-borders-to-cells-in-a-worksheet/), nuovamente usando C# o Visual Basic. Gli esempi di codice Aspose.Cells sono molto più brevi perché Aspose.Cells è ottimizzato per una codifica efficiente.

Il codice genera un file Excel con un certo numero di celle nel primo foglio, ognuna con un bordo diverso:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Celle con bordi applicati.**

### **Aggiunta di bordi utilizzando VSTO**

**C#**

{{< highlight csharp >}}

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aggiunta di bordi utilizzando Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
