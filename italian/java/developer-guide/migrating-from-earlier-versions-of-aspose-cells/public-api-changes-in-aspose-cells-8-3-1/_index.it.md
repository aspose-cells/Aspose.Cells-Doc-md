---
title: Modifiche all'API pubblica in Aspose.Cells 8.3.1
type: docs
weight: 120
url: /it/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.3.0 alla 8.3.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà DataLabels.ShowCellRange Aggiunta**
Il getter/setter per la proprietà ShowCellRange è stato aggiunto alla classe DataLabels per imitare la funzionalità di Excel di formattazione delle etichette dati del grafico in fase di esecuzione. Si prega di notare che Excel fornisce questa funzione attraverso i seguenti passaggi.

1. Seleziona Etichette dati della serie e fai clic con il pulsante destro del mouse per aprire il menu a comparsa.
1.  Clicca il**Formato etichette dati...** e lo mostrerà**Opzioni etichetta**.
1.  Selezionare o deselezionare la casella di controllo**L'etichetta contiene - Valore da Cells**.

 Il codice di esempio riportato di seguito accede alle etichette dei dati della serie di grafici e quindi imposta il metodo DataLabels.setShowCellRange() su true per imitare la funzionalità di Excel di**L'etichetta contiene - Valore da Cells**.

**Giava**

{{< highlight "csharp" >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Visualizzazione dell'intervallo Cell come etichette dati](/cells/it/java/showing-cell-range-as-the-data-labels/) per maggiori informazioni.

{{% /alert %}} 

### **Metodi Cell.getTable e ListObject.putCellValue Aggiunto**
I metodi Cell.getTable & ListObject.putCellValue sono stati aggiunti con Aspose.Cells for Java 8.3.1 per facilitare agli utenti l'accesso al ListObject da una cella e l'aggiunta di valori al suo interno utilizzando gli offset di riga e colonna. Il codice di esempio seguente carica il foglio di calcolo di origine e aggiunge i valori all'interno della tabella.

**Giava**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Accesso alla tabella da Cell e aggiunta di valori al suo interno utilizzando gli offset di righe e colonne](/cells/it/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) per maggiori informazioni.

{{% /alert %}} 

### **Metodi OdsSaveOptions.isStrictSchema11 e OdsSaveOptions.setStrictSchema11 Aggiunto**
I metodi isStrictSchema11 e setStrictSchema11 sono stati aggiunti alla classe OdsSaveOptions per consentire agli sviluppatori di salvare il foglio di calcolo in formato conforme alla specifica ODF v1.2. Il valore predefinito della proprietà setStrictSchema11 è false, significa che dalla versione 8.3.1 delle API Aspose.Cells i file ODS verranno salvati come formato ODF versione 1.2 per impostazione predefinita.

Il frammento di codice fornito di seguito salva il file ODS in formato ODF 1.2.

**Giava**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Salva il file ODS nelle specifiche ODF 1.1 e 1.2](/cells/it/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) per maggiori informazioni.

{{% /alert %}} 

### **Metodo SparklineCollection.add Aggiunto**
 Aspose.Cells Le API hanno esposto il metodo SparklineCollection.add(String dataRange, int row, int column) per specificare l'intervallo di dati e la posizione del gruppo Sparkline. Si noti che Excel fornisce la stessa funzionalità attraverso i seguenti passaggi.

1. Seleziona la cella contenente il tuo Sparkline.
1.  Selezionare**Modifica i dati dalla sparkline** sezione all'interno del**Disegno** scheda
1.  Scegliere**Modifica la posizione e i dati del gruppo**.
1. Specificare**Intervallo di dati** & **Posizione**.

 Il seguente codice di esempio carica il foglio di calcolo di origine, accede al primo gruppo sparkline e aggiunge nuovi intervalli di dati e posizioni per il gruppo sparkline.

**Giava**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Copia sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline](/cells/it/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) per maggiori informazioni.

{{% /alert %}}
