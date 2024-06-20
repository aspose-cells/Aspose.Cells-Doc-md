---
title: Modifiche dell API pubblica in Aspose.Cells 8.4.0
type: docs
weight: 130
url: /it/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.3.2 alla 8.4.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ecc. e classi rimosse, ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare il codice VBA/Macro nei fogli di calcolo**
Per fornire la funzionalità di Manipolazione del Codice VBA/Macro, il Aspose.Cells for .NET 8.4.0 ha esposto una serie di nuove classi e proprietà nello spazio dei nomi Aspose.Cells.Vba. Alcuni dei dettagli importanti di queste nuove classi sono i seguenti.

- La classe VbaProject può essere utilizzata per recuperare il progetto VBA da un dato foglio di calcolo.
- La classe VbaModuleCollection rappresenta la raccolta di moduli VBA che fanno parte di un dato progetto VbaProject.
- La classe VbaModule rappresenta un singolo modulo dalla VbaModuleCollection.

Il seguente snippet di codice mostra come modificare dinamicamente i segmenti di codice VBA.

**C#**

{{< highlight csharp >}}

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


### **Possibilità di rimuovere una tabella pivot**
Aspose.Cells for .NET 8.4.0 ha esposto due metodi per la PivotTableCollection per fornire la funzionalità di rimozione della tabella pivot da un dato foglio di calcolo. I dettagli dei suddetti metodi sono i seguenti.

- Il metodo PivotTableCollection.Remove accetta un oggetto PivotTable e lo rimuove dalla collezione.
- Il metodo PivotTableCollection.RemoveAt accetta un valore intero basato su un indice zero e rimuove la particolare PivotTable dalla collezione.

Il seguente snippet di codice mostra come rimuovere la tabella pivot utilizzando entrambi i metodi sopra menzionati.

**C#**

{{< highlight csharp >}}

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


### **Supporto per Layout di Tabelle Pivot Diversi**
Aspose.Cells for .NET 8.4.0 fornisce il supporto per diversi layout predefiniti per le Tabelle Pivot. Per fornire questa funzionalità, le API Aspose.Cells hanno esposto tre metodi per la classe PivotTable come dettagliato di seguito.

- Il metodo PivotTable.ShowInCompactForm rende la Tabella Pivot nel layout Compatto.
- Il metodo PivotTable.ShowInOutlineForm rende la Tabella Pivot nel layout ad Albero.
- Il metodo PivotTable.ShowInTabularForm rende la Tabella Pivot nel layout Tabellare.

{{% alert color="primary" %}} 

È importante chiamare PivotTable.RefreshData & PivotTable.CalculateData dopo aver impostato uno qualsiasi dei layout sopra menzionati.

{{% /alert %}} 

Il seguente codice di esempio imposta layout diversi per una tabella pivot e memorizza il risultato su disco.

**C#**

{{< highlight csharp >}}

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


### **Classe TxtLoadStyleStrategy e Proprietà TxtLoadOptions.LoadStyleStrategy Aggiunta**
Aspose.Cells for .NET 8.4.0 ha esposto la classe TxtLoadStyleStrategy e la proprietà TxtLoadOptions.LoadStyleStrategy per specificare la strategia di formattazione dei valori analizzati durante la conversione del valore stringa in numero o data.
### **Aggiunto Metodo DataBar.ToImage**
Con il rilascio di v8.4.0, l'API Aspose.Cells ha fornito il metodo DataBar.ToImage per salvare le DataBar formattate condizionalmente in formato immagine. Il metodo {DataBar.ToImage}} accetta due parametri come dettagliato di seguito.

- Il primo parametro è di tipo Aspose.Cells.Cell su cui è stata applicata la formattazione condizionale.
- Il secondo parametro è di tipo Aspose.Cells.Rendering.ImageOrPrintOptions per impostare diverse impostazioni dell'immagine risultante.

Il seguente codice di esempio dimostra l'uso del metodo DataBar.ToImage per rendere la DataBar in formato immagine.

**C#**

{{< highlight csharp >}}

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

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Aggiunta Proprietà Border.ThemeColor**
Le API Aspose.Cells consentono di estrarre dati di formattazione correlati al tema dai fogli di calcolo. Con il rilascio di Aspose.Cells for .NET 8.4.0, l'API ha esposto la proprietà Border.ThemeColor che può essere utilizzata per recuperare gli attributi di colore del tema dei bordi delle celle.
### **Aggiunta Proprietà DrawObject.ImageBytes**
Aspose.Cells for .NET 8.4.0 ha esposto la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine da Grafico o Forma.
### **Aggiunta Proprietà HtmlSaveOptions.ExportBogusRowData**
Aspose.Cells for .NET 8.4.0 ha fornito la proprietà {HtmlSaveOptions.ExportBogusRowData}}. La proprietà di tipo Boolean determina se l'API inietterà dati di riga inferiore fasulli durante l'esportazione del foglio di calcolo in formato HTML.

{{% alert color="primary" %}} 

Il valore predefinito è true.

{{% /alert %}} 

Il seguente codice di esempio illustra l'uso della proprietà sopra citata.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Aggiunta Proprietà HtmlSaveOptions.CellCssPrefix**
La nuova proprietà aggiunta HtmlSaveOptions.CellCssPrefix consente di impostare il prefisso per i file CSS durante l'esportazione dei fogli di calcolo in formato HTML.

{{% alert color="primary" %}} 

Il valore predefinito è "" (stringa vuota).

{{% /alert %}}
## **API obsolete**
### **Metodi Cells.GetCellByIndex & Row.GetCellByIndex obsoleti**
Utilizzare il metodo GetEnumerator per iterare su tutte le celle invece.
### **Proprietà Image obsoleta di DrawObject**
Utilizzare la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine invece.
