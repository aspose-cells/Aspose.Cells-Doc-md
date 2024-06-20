---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.4.2
type: docs
weight: 160
url: /it/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.4.1 a 8.4.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, [classi aggiunte, ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo di creazione grafico migliorato**
La classe com.aspose.cells.charts.Chart ha esposto il metodo setChartDataRange per facilitare il compito di creazione del grafico. Il metodo setChartDataRange accetta due parametri, dove il primo parametro è di tipo stringa che specifica l'area delle celle da cui tracciare le serie di dati. Il secondo parametro è di tipo Boolean che specifica l'orientamento del tracciato, cioè; se tracciare le serie di dati del grafico da un intervallo di valori delle celle per riga o per colonne.

Il seguente frammento di codice mostra come creare un grafico a colonne con poche righe di codice assumendo che i dati della serie del grafico siano presenti sullo stesso foglio di lavoro dalle celle A1 a D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Metodo VbaModuleCollection.add aggiunto**
Aspose.Cells for Java 8.4.2 ha esposto il metodo VbaModuleCollection.add per aggiungere un nuovo modulo VBA all'istanza del Foglio di lavoro. Il metodo VbaModuleCollection.add accetta un parametro di tipo Worksheet per aggiungere un modulo specifico del foglio di lavoro.

Il seguente frammento di codice mostra come utilizzare il metodo VbaModuleCollection.add.

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Metodo sovraccaricato Cells.copyColumns Aggiunto**
Aspose.Cells for Java 8.4.2 ha esposto una versione sovraccaricata del metodo Cells.copyColumns per ripetere le colonne di origine sulla destinazione. Il nuovo metodo esposto accetta in totale 5 parametri, di cui i primi 4 sono gli stessi del comune metodo Cells.copyColumns. Tuttavia, l'ultimo parametro di tipo int specifica il numero di colonne di destinazione su cui devono essere ripetute le colonne di origine.

Il seguente frammento di codice mostra come utilizzare il nuovo metodo esposto Cells.copyColumns.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Enumerazione Campi PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS Aggiunti**
Con il rilascio della v8.4.2, l'API di Aspose.Cells ha aggiunto 2 nuovi campi di enumerazione per PasteType come dettagliato di seguito.

- PasteType.DEFAULT: Funziona in modo simile alla funzionalità "Tutto" di Excel per incollare una serie di celle.
- PasteType.ALL_EXCEPT_BORDERS: Funziona in modo simile alla funzionalità "Tutto tranne i bordi" di Excel per incollare una serie di celle.

Il seguente codice di esempio illustra l'uso del campo PasteType.DEFAULT.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

A partire dal rilascio di Aspose.Cells for Java 8.4.2, il campo di enumerazione PasteType.ALL si comporta in modo diverso rispetto alla funzionalità "Tutto" di Excel per incollare una serie di celle. Ora, il campo PasteType.ALL copia anche le larghezze delle colonne sulla gamma di destinazione, a differenza della funzionalità "Tutto" di Excel. Per emulare il comportamento "Tutto" di Excel, si prega di utilizzare il PasteType.DEFAULT.

{{% /alert %}}
