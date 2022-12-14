---
title: Pubblico API Modifiche Aspose.Cells 8.4.0
type: docs
weight: 130
url: /it/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.3.2 alla 8.4.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-0/) e[classi rimosse ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-0/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare il codice VBA/Macro nei fogli di calcolo**
 Al fine di fornire la funzionalità di[Manipolazione codice VBA/Macro](/cells/it/net/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for .NET 8.4.0 ha esposto una serie di nuove classi e proprietà nello spazio dei nomi Aspose.Cells.Vba. Alcuni dei dettagli importanti di queste nuove classi sono i seguenti.

- La classe VbaProject può essere utilizzata per recuperare il progetto VBA da un determinato foglio di calcolo.
- La classe VbaModuleCollection rappresenta la raccolta di moduli VBA che fanno parte di un dato VbaProject.
- La classe VbaModule rappresenta un singolo modulo di VbaModuleCollection.

Il seguente frammento di codice mostra come modificare dinamicamente i segmenti di codice VBA.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Possibilità di rimuovere la tabella pivot**
Aspose.Cells for .NET 8.4.0 ha esposto due metodi per PivotTableCollection per fornire la funzione di rimozione della tabella pivot da un determinato foglio di calcolo. I dettagli delle suddette modalità sono i seguenti.

- Il metodo PivotTableCollection.Remove accetta un oggetto della tabella pivot e lo rimuove dalla raccolta.
- Il metodo PivotTableCollection.RemoveAt accetta un valore intero basato su indice zero e rimuove la specifica tabella pivot dalla raccolta.

Il seguente frammento di codice mostra come rimuovere la tabella pivot utilizzando entrambi i metodi sopra menzionati.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Supporto per diversi layout di tabelle pivot**
Aspose.Cells for .NET 8.4.0 fornisce il supporto per diversi layout predefiniti per le tabelle pivot. Per fornire questa funzionalità, le API Aspose.Cells hanno esposto tre metodi per la classe PivotTable come descritto di seguito.

- Il metodo PivotTable.ShowInCompactForm esegue il rendering della tabella pivot in un layout compatto.
- Il metodo PivotTable.ShowInOutlineForm esegue il rendering della tabella pivot nel layout Struttura.
- Il metodo PivotTable.ShowInTabularForm esegue il rendering della tabella pivot in layout tabulare.

{{% alert color="primary" %}} 

È importante chiamare PivotTable.RefreshData e PivotTable.CalculateData dopo aver impostato uno dei layout sopra menzionati.

{{% /alert %}} 

Il codice di esempio seguente imposta layout diversi per una tabella pivot e archivia il risultato su disco.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Classe TxtLoadStyleStrategy e proprietà TxtLoadOptions.LoadStyleStrategy aggiunta**
Aspose.Cells for .NET 8.4.0 ha esposto la classe TxtLoadStyleStrategy e la proprietà TxtLoadOptions.LoadStyleStrategy per specificare la strategia per formattare i valori analizzati durante la conversione del valore stringa in numero o data/ora.
### **Metodo DataBar.ToImage aggiunto**
Con il rilascio della v8.4.0, il Aspose.Cells API ha fornito il metodo DataBar.ToImage per salvare i DataBar formattati in modo condizionale in formato immagine. Il metodo {DataBar.ToImage}} accetta due parametri come descritto di seguito.

- Il primo parametro è di tipo Aspose.Cells.Cell su cui è stata applicata la formattazione condizionale.
- Il secondo parametro è di tipo Aspose.Cells.Rendering.ImageOrPrintOptions per impostare diversi parametri dell'immagine risultante.

Il codice di esempio seguente illustra l'utilizzo del metodo DataBar.ToImage per eseguire il rendering di DataBar in formato immagine.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Proprietà Border.ThemeColor aggiunto**
Aspose.Cells Le API consentono di estrarre i dati di formattazione relativi al tema dai fogli di calcolo. Con il rilascio di Aspose.Cells for .NET 8.4.0, API ha esposto la proprietà Border.ThemeColor che può essere utilizzata per recuperare gli attributi del colore del tema dei bordi Cell.
### **Proprietà DrawObject.ImageBytes aggiunto**
Aspose.Cells for .NET 8.4.0 ha esposto la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine da Chart o Shape.
### **Proprietà HtmlSaveOptions.ExportBogusRowData aggiunta**
Aspose.Cells for .NET 8.4.0 ha fornito la proprietà {HtmlSaveOptions.ExportBogusRowData}}. La proprietà del tipo booleano determina se API inietterà dati fasulli della riga inferiore durante l'esportazione del foglio di calcolo in formato HTML.

{{% alert color="primary" %}} 

Il valore predefinito è vero.

{{% /alert %}} 

Il seguente codice di esempio illustra l'utilizzo della suddetta proprietà.

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Proprietà HtmlSaveOptions.CellCssPrefix aggiunta**
La proprietà appena aggiunta HtmlSaveOptions.CellCssPrefix consente di impostare il prefisso per i file CSS durante l'esportazione di fogli di calcolo in formato HTML.

{{% alert color="primary" %}} 

Il valore predefinito è "" (stringa vuota).

{{% /alert %}}
## **API obsolete**
### **Metodi Cells.GetCellByIndex e Row.GetCellByIndex Obsoleti**
Usare invece il metodo GetEnumerator per iterare tutte le celle.
### **Proprietà DrawObject.Image Obsoleto**
Usare invece la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine.
