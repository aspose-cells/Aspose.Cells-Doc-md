---
title: Pubblico API Modifiche Aspose.Cells 8.4.2
type: docs
weight: 160
url: /it/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.4.1 alla 8.4.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo di creazione grafico migliorato**
La classe com.aspose.cells.charts.Chart ha esposto il metodo setChartDataRange per facilitare l'attività di creazione del grafico. Il metodo setChartDataRange accetta due parametri, dove il primo parametro è di tipo stringa che specifica l'area della cella da cui tracciare la serie di dati. Il secondo parametro è di tipo booleano che specifica l'orientamento della trama, ovvero; se tracciare la serie di dati del grafico da un intervallo di valori di cella per riga o per colonna.

Il seguente frammento di codice mostra come creare un istogramma con poche righe di codice presupponendo che i dati della serie di grafici del grafico siano presenti nello stesso foglio di lavoro dalla cella A1 alla cella D4.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Metodo VbaModuleCollection.add Aggiunto**
Aspose.Cells for Java 8.4.2 ha esposto il metodo VbaModuleCollection.add per aggiungere un nuovo modulo VBA all'istanza di Workbook. Il metodo VbaModuleCollection.add accetta un parametro di tipo Foglio di lavoro per aggiungere un modulo specifico del foglio di lavoro.

Il seguente frammento di codice mostra come usare il metodo VbaModuleCollection.add.

**Java**

{{< highlight "csharp" >}}

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

### **Metodo di overload Cells.copyColumns Aggiunto**
Aspose.Cells for Java 8.4.2 ha esposto una versione sovraccaricata del metodo Cells.copyColumns per ripetere le colonne di origine nella destinazione. Il metodo appena esposto accetta 5 parametri in totale, dove i primi 4 parametri sono gli stessi del metodo comune Cells.copyColumns. Tuttavia, l'ultimo parametro di tipo int specifica il numero di colonne di destinazione su cui devono essere ripetute le colonne di origine.

Il frammento di codice seguente mostra come utilizzare il metodo Cells.copyColumns appena esposto.

**Java**

{{< highlight "csharp" >}}

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

### **Campi di enumerazione PasteType.DEFAULT e PasteType.ALL_EXCEPT_BORDERS aggiunti**
Con il rilascio di v8.4.2, Aspose.Cells API ha aggiunto 2 nuovi campi di enumerazione per PasteType come descritto di seguito.

- PasteType.DEFAULT: funziona in modo simile alla funzionalità "Tutto" di Excel per incollare un intervallo di celle.
- IncollaTipo.ALL_TRANNE_BORDI: funziona in modo simile alla funzionalità "Tutti tranne i bordi" di Excel per incollare un intervallo di celle.

Il codice di esempio seguente illustra l'utilizzo del campo PasteType.DEFAULT.

**Java**

{{< highlight "csharp" >}}

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

A partire dal rilascio di Aspose.Cells for Java 8.4.2, l'enumerazione archiviata PasteType.ALL si comporta in modo diverso rispetto alla funzionalità "Tutto" di Excel per incollare un intervallo di celle. Ora, PasteType.ALL copia anche le larghezze delle colonne nell'intervallo di destinazione anziché nella funzionalità "Tutto" di Excel. Per imitare il comportamento "Tutto" di Excel, utilizzare PasteType.DEFAULT.

{{% /alert %}}
