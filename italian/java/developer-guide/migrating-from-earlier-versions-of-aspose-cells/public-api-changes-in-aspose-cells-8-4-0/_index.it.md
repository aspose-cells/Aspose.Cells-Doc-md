---
title: Modifiche dell API pubblica in Aspose.Cells 8.4.0
type: docs
weight: 140
url: /it/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.3.2 alla 8.4.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte, ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-0/) e [classi rimosse, ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-0/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare il codice VBA/Macro nei fogli di calcolo**
Per fornire la funzionalità di [Manipolazione del codice VBA/Macro](/cells/it/java/modifying-vba-or-macro-code-using-aspose-cells/), il Aspose.Cells for Java 8.4.0 ha esposto una serie di nuove classi e proprietà nel package com.aspose.cells.Vba. Alcuni dei dettagli importanti di queste nuove classi sono i seguenti.

- La classe VbaProject può essere utilizzata per recuperare il progetto VBA da un dato foglio di calcolo.
- La classe VbaModuleCollection rappresenta la raccolta di moduli VBA che fanno parte di un dato progetto VbaProject.
- La classe VbaModule rappresenta un singolo modulo dalla VbaModuleCollection.

Il seguente snippet di codice mostra come modificare dinamicamente i segmenti di codice VBA.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Possibilità di rimuovere una tabella pivot**
Aspose.Cells for Java 8.4.0 ha esposto due metodi per la PivotTableCollection per fornire la funzionalità di rimozione della tabella pivot da un foglio di calcolo. I dettagli dei suddetti metodi sono i seguenti.

- Il metodo PivotTableCollection.remove accetta un oggetto di tipo PivotTable e lo rimuove dalla collezione.
- Il metodo PivotTableCollection.removeAt accetta un valore intero basato su un indice zero e rimuove il particolare PivotTable dalla collezione.

Il seguente snippet di codice mostra come rimuovere la tabella pivot utilizzando entrambi i metodi sopra menzionati.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Supporto per Layout di Tabelle Pivot Diversi**
Aspose.Cells for Java 8.4.0 fornisce il supporto per diversi layout predefiniti per le tabelle pivot. Per fornire questa funzionalità, le API di Aspose.Cells hanno esposto tre metodi per la classe PivotTable come dettagliato di seguito.

- Il metodo PivotTable.showInCompactForm rende la tabella pivot in un layout Compatto.
- Il metodo PivotTable.showInOutlineForm rende la tabella pivot in un layout ad Albero.
- Il metodo PivotTable.showInTabularForm rende la tabella pivot in un layout Tabulare.

{{% alert color="primary" %}} 

È importante chiamare i metodi PivotTable.refreshData & PivotTable.calculateData dopo aver impostato uno qualsiasi dei layout sopra menzionati. 

{{% /alert %}} 

Il seguente codice di esempio imposta layout diversi per una tabella pivot e memorizza il risultato su disco.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Classe TxtLoadStyleStrategy e Proprietà TxtLoadOptions.LoadStyleStrategy Aggiunta**
Aspose.Cells for Java 8.4.0 ha esposto la classe TxtLoadStyleStrategy e la proprietà TxtLoadOptions.LoadStyleStrategy per specificare la strategia per formattare i valori analizzati durante la conversione da valore stringa a numero o data.
### **Aggiunto Metodo DataBar.ToImage**
Con il rilascio della v8.4.0, l'API di Aspose.Cells ha fornito il metodo DataBar.toImage per salvare la DataBar formattata condizionalmente in formato immagine. Il metodo {DataBar.toImage}} accetta due parametri come dettagliato di seguito.

- Il primo parametro è di tipo com.aspose.cells.Cell su cui è stata applicata la formattazione condizionale.
- Il secondo parametro è di tipo com.aspose.cells.rendering.ImageOrPrintOptions per impostare diversi parametri dell'immagine risultante.

Il seguente codice di esempio dimostra l'uso del metodo DataBar.toImage per rendere la DataBar in formato immagine.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Aggiunta Proprietà Border.ThemeColor**
Le API di Aspose.Cells consentono di estrarre dati correlati ai temi dai fogli di calcolo. Con il rilascio del Aspose.Cells for Java 8.4.0, l'API ha esposto la proprietà Border.ThemeColor che può essere utilizzata per recuperare gli attributi del colore di tema dei bordi delle celle.
### **Aggiunta Proprietà DrawObject.ImageBytes**
Aspose.Cells for Java 8.4.0 ha esposto la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine da Grafico o Forma.
### **Aggiunta Proprietà HtmlSaveOptions.ExportBogusRowData**
Aspose.Cells for Java 8.4.0 ha fornito la proprietà {HtmlSaveOptions.ExportBogusRowData. La proprietà di tipo Boolean determina se l'API inserirà dati di fila fittizi in basso durante l'esportazione del foglio di calcolo in formato HTML. 

{{% alert color="primary" %}} 

Il valore predefinito è true.

{{% /alert %}} 

Il seguente codice di esempio illustra l'uso della proprietà sopra citata.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Aggiunta Proprietà HtmlSaveOptions.CellCssPrefix**
La nuova proprietà aggiunta HtmlSaveOptions.CellCssPrefix consente di impostare il prefisso per i file CSS durante l'esportazione dei fogli di calcolo in formato HTML.

{{% alert color="primary" %}} 

Il valore predefinito è "" (stringa vuota).

{{% /alert %}}
## **API obsolete**
### **Metodi Cells.getCellByIndex & Row.getCellByIndex obsoleti**
Usa il metodo getEnumerator per iterare tutte le celle.
### **Proprietà Image obsoleta di DrawObject**
Utilizzare la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine invece.
{{< app/cells/assistant language="java" >}}
