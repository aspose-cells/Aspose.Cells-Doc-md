---
title: Filtro dati automatico
type: docs
weight: 120
url: /it/net/auto-filter-data/
---
{{% alert color="primary" %}}

Per comprendere quali dati si trovano in un intervallo, spesso è più semplice ordinare e filtrare i dati piuttosto che esaminare colonne di dati non ordinati. L'ordinamento organizza i dati in ordine crescente o decrescente, facilitando la ricerca di valori specifici. Filtrare i dati, permette di mostrare solo determinati valori. Ad esempio, aiuta a concentrarsi su particolari articoli nei registri delle vendite.

Gli utenti di Microsoft Excel possono applicare il filtro automatico alle colonne. Il filtro automatico aggiunge un menu nella parte superiore della colonna, da cui è possibile ordinare i dati della colonna del filtro. Questa funzione è disponibile anche per gli sviluppatori che lavorano con fogli di calcolo Excel, tramite VSTO o Aspose.Cells for .NET.

{{% /alert %}}

## **Filtraggio automatico dei dati**

Per applicare il filtro automatico a una colonna:

1. Crea una cartella di lavoro.
1. Ottieni un foglio di lavoro.
1. Aggiungi dati di esempio.
1. Applica filtro automatico.
1. Colonne di adattamento automatico per rendere attraente il display.
1. Salva il foglio di calcolo.

 Gli esempi di codice in questo articolo mostrano come eseguire questi passaggi utilizzando[VSTO](/cells/it/net/auto-filter-data/) con C# o Visual Basic o usando[Apose.Cells](/cells/it/net/auto-filter-data/), sempre con C# o Visual Basic.

### **Filtro automatico dei dati con VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**Filtro automatico applicato con VSTO** 

![cose da fare:immagine_alt_testo](auto-filter-data_1.png)

### **Dati di filtraggio automatico con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Filtro automatico applicato con Aspose.Cells for .NET** 

![cose da fare:immagine_alt_testo](auto-filter-data_2.png)
