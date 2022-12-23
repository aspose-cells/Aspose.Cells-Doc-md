---
title: Pubblico API Modifiche Aspose.Cells 8.4.2
type: docs
weight: 150
url: /it/net/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.4.1 alla 8.4.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo di creazione grafico migliorato**
La classe Aspose.Cells.Charts.Chart ha esposto il metodo SetChartDataRange per facilitare l'attività di creazione del grafico. Il metodo SetChartDataRange accetta due parametri, dove il primo parametro è di tipo stringa che specifica l'area della cella da cui tracciare la serie di dati. Il secondo parametro è di tipo booleano che specifica l'orientamento della trama, ovvero; se tracciare la serie di dati del grafico da un intervallo di valori di cella per riga o per colonna.

Il seguente frammento di codice mostra come creare un istogramma con poche righe di codice presupponendo che i dati della serie di grafici del grafico siano presenti nello stesso foglio di lavoro dalla cella A1 alla cella D4.

**C#**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Metodo VbaModuleCollection.Add Aggiunto**
Aspose.Cells for .NET 8.4.2 ha esposto il metodo VbaModuleCollection.Add per aggiungere un nuovo modulo VBA all'istanza di Workbook. Il metodo VbaModuleCollection.Add accetta un parametro di tipo Worksheet per aggiungere un modulo specifico del foglio di lavoro.

Il frammento di codice seguente mostra come usare il metodo VbaModuleCollection.Add.

**C#**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Metodo di overload Cells.CopyColumns aggiunto**
Aspose.Cells for .NET 8.4.2 ha esposto una versione di overload del metodo Cells.CopyColumns per ripetere le colonne di origine nella destinazione. Il metodo appena esposto accetta 5 parametri in totale, dove i primi 4 parametri sono gli stessi del metodo comune Cells.CopyColumns. Tuttavia, l'ultimo parametro di tipo int specifica il numero di colonne di destinazione su cui devono essere ripetute le colonne di origine.

Il frammento di codice seguente mostra come usare il metodo Cells.CopyColumns appena esposto.

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Campi di enumerazione PasteType.Default e PasteType.DefaultExceptBorders aggiunti**
Con il rilascio di v8.4.2, Aspose.Cells API ha aggiunto 2 nuovi campi di enumerazione per PasteType come descritto di seguito.

- PasteType.Default: funziona in modo simile alla funzionalità "Tutto" di Excel per incollare un intervallo di celle.
- PasteType.DefaultExceptBorders: funziona in modo simile alla funzionalità "Tutto tranne i bordi" di Excel per incollare un intervallo di celle.

Il codice di esempio seguente illustra l'utilizzo del campo PasteType.Default.

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

A partire dal rilascio di Aspose.Cells for .NET 8.4.2, l'enumerazione archiviata PasteType.All si comporta in modo diverso rispetto alla funzionalità "Tutto" di Excel per incollare un intervallo di celle. Ora, PasteType.All copia anche le larghezze delle colonne nell'intervallo di destinazione anziché nella funzionalità "Tutto" di Excel. Per imitare il comportamento "Tutto" di Excel, utilizzare PasteType.Default.

{{% /alert %}}
