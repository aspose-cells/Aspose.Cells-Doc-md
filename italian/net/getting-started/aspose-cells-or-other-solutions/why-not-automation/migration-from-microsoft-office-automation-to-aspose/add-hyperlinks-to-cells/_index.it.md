---
title: Aggiungi collegamenti ipertestuali alle celle
type: docs
weight: 60
url: /it/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET consente di eseguire quasi tutte le attività tramite la tua applicazione che un utente può eseguire in Microsoft Excel. Questo articolo confronta come aggiungere un collegamento ipertestuale a una cella in un foglio di lavoro utilizzando VSTO e Aspose.Cells for .NET.

{{% /alert %}}

## **Aggiunta di collegamenti ipertestuali alle celle**

Per aggiungere collegamenti ipertestuali alle celle in un foglio di calcolo, segui i seguenti passaggi:

1. Configura il foglio di lavoro:
   1. Istanziare un oggetto Application.
      (Solo VSTO.)
   1. Aggiungi un foglio di lavoro.
   1. Ottieni il primo foglio.
   1. Aggiungere testo alle celle a cui si aggiungerà un collegamento ipertestuale.
1. Aggiungere un collegamento ipertestuale.
1. Salvare il documento.

Questi passaggi sono mostrati negli esempi di codice di seguito. Il primo esempio mostra come utilizzare [VSTO](/cells/it/net/aggiungere-collegamenti-ipertestuali-alle-celle/) con C# o Visual Basic per aggiungere un collegamento ipertestuale a una cella. Gli esempi successivi mostrano come fare la stessa cosa utilizzando [Aspose.Cells for .NET](/cells/it/net/aggiungere-collegamenti-ipertestuali-alle-celle/), di nuovo utilizzando C# o Visual Basic.

Gli esempi di codice generano un file Excel con un collegamento ipertestuale nella cella A1 del primo foglio di lavoro.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**Un collegamento ipertestuale viene aggiunto alla cella A1.**

### **Aggiunta collegamenti ipertestuali alle celle con VSTO**

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

### **Aggiunta collegamenti ipertestuali alle celle con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
