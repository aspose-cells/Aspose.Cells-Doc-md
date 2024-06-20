---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.4.2
type: docs
weight: 150
url: /it/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.4.1 a 8.4.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-2/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo di creazione grafico migliorato**
La classe Aspose.Cells.Charts.Chart ha esposto il metodo SetChartDataRange per facilitare il compito di creazione di grafici. Il metodo SetChartDataRange accetta due parametri, il primo dei quali è di tipo stringa che specifica l'area cellulare da cui tracciare le serie di dati. Il secondo parametro è di tipo Booleano che specifica l'orientamento del tracciamento, cioè; se tracciare le serie di dati del grafico da un intervallo di valori delle celle per riga o per colonne.

Il seguente frammento di codice mostra come creare un grafico a colonne con poche righe di codice assumendo che i dati della serie del grafico siano presenti sullo stesso foglio di lavoro dalle celle A1 a D4.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Metodo Aggiunto VbaModuleCollection.Add**
Aspose.Cells for .NET 8.4.2 ha esposto il metodo VbaModuleCollection.Add per aggiungere un nuovo modulo VBA all'istanza di Workbook. Il metodo VbaModuleCollection.Add accetta un parametro di tipo Worksheet per aggiungere un modulo specifico per il foglio di lavoro.

Il seguente frammento di codice mostra come utilizzare il metodo VbaModuleCollection.Add.

**C#**

{{< highlight csharp >}}

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


### **Metodo Sovraccaricato Cells.CopyColumns Aggiunto**
Aspose.Cells for .NET 8.4.2 ha esposto una versione sovraccaricata del metodo Cells.CopyColumns per ripetere le colonne di origine sulla destinazione. Il nuovo metodo esposto accetta in totale 5 parametri, dove i primi 4 parametri sono gli stessi del comune metodo Cells.CopyColumns. Tuttavia, l'ultimo parametro di tipo int specifica il numero di colonne di destinazione su cui le colonne di origine devono essere ripetute.

Il seguente frammento di codice mostra come utilizzare il nuovo metodo esposto Cells.CopyColumns.

**C#**

{{< highlight csharp >}}

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


### **Campi di Enumerazione PasteType.Default & PasteType.DefaultExceptBorders Aggiunti**
Con il rilascio della v8.4.2, l'API di Aspose.Cells ha aggiunto 2 nuovi campi di enumerazione per PasteType come dettagliato di seguito.

- PasteType.Default: Funziona in modo simile alla funzionalità "Tutto" di Excel per incollare un intervallo di celle.
- PasteType.DefaultExceptBorders: Funziona in modo simile alla funzionalità "Tutto tranne i bordi" di Excel per incollare un intervallo di celle.

Il seguente codice di esempio dimostra l'utilizzo del campo PasteType.Default.

**C#**

{{< highlight csharp >}}

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

A partire dal rilascio di Aspose.Cells for .NET 8.4.2, il campo di enumerazione PasteType.All si comporta in modo diverso rispetto alla funzionalità "Tutto" di Excel per incollare un intervallo di celle. Ora, il PasteType.All copia anche le larghezze delle colonne nell'intervallo di destinazione contrariamente alla funzionalità "Tutto" di Excel. Per emulare il comportamento "Tutto" di Excel, si prega di utilizzare il PasteType.Default.

{{% /alert %}}
