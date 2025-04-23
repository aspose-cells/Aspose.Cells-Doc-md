---
title: Modifiche all API pubblica in Aspose.Cells 8.3.1
type: docs
weight: 120
url: /it/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.3.0 a 8.3.1 che potrebbero interessare a sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà ShowCellRange di DataLabels aggiunta**
Il getter/setter per la proprietà ShowCellRange è stato aggiunto alla classe DataLabels per mimare la funzionalità di formattazione dei dati del grafico in Excel in tempo reale. Si noti che Excel fornisce questa funzione attraverso i seguenti passaggi. 

1. Seleziona le Etichette dati della serie e fai clic con il pulsante destro per aprire il menu a comparsa.
1. Fare clic su **Formato etichette dati...** e verrà visualizzato **Opzioni etichetta**.
1. Selezionare o deselezionare la casella di controllo **L'etichetta contiene - Valore delle celle**.

Il codice di esempio seguente accede alle etichette dei dati della serie del grafico e quindi imposta il metodo DataLabels.setShowCellRange() su true per imitare la funzione di Excel di **L'etichetta contiene - Valore dalle celle**.

**Java**

{{< highlight csharp >}}

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

Si prega di controllare l'articolo [Mostrare Intervallo di Celle come Etichette Dati](/cells/it/java/showing-cell-range-as-the-data-labels/) per ulteriori informazioni.

{{% /alert %}} 

### **Aggiunti i metodi Cell.getTable & ListObject.putCellValue**
I metodi Cell.getTable & ListObject.putCellValue sono stati aggiunti con Aspose.Cells for Java 8.3.1 per consentire agli utenti di accedere all'oggetto ListObject da una cella e aggiungere valori al suo interno utilizzando gli spostamenti delle righe e delle colonne. Il seguente codice di esempio carica il foglio di calcolo di origine e aggiunge valori all'interno della tabella.

**Java**

{{< highlight csharp >}}

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

Si prega di controllare l'articolo [Accesso Tabella da Cella e Aggiunta di Valori al suo Interno utilizzando gli Spostamenti delle Righe e delle Colonne](/cells/it/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) per ulteriori informazioni.

{{% /alert %}} 

### **Aggiunti i metodi OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11**
I metodi isStrictSchema11 & setStrictSchema11 sono stati aggiunti alla classe OdsSaveOptions per consentire agli sviluppatori di salvare il foglio di calcolo in formato conforme alla specifica ODF v1.2. Il valore predefinito della proprietà setStrictSchema11 è false, significa che dalla versione 8.3.1 delle API di Aspose.Cells i file ODS verranno salvati come formato ODF versione 1.2 per impostazione predefinita.

Il frammento di codice fornito di seguito salva il file ODS nel formato ODF 1.2.

**Java**

{{< highlight csharp >}}

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

Si prega di controllare l'articolo [Salvare il file ODS nelle Specifiche ODF 1.1 e 1.2](/cells/it/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) per ulteriori informazioni.

{{% /alert %}} 

### **Metodo Aggiunto SparklineCollection.add**
Le API di Aspose.Cells hanno esposto il metodo SparklineCollection.add(String dataRange, int row, int column) per specificare il Raggio dei Dati e la Posizione del Gruppo Sparkline. Si prega di notare che Excel fornisce la stessa funzionalità tramite i seguenti passaggi. 

1. Selezionare la cella contenente la tua Linea di tendenza.
1. Selezionare **Modifica dati dalla linea di tendenza** nella sezione **Progettazione**.
1. Scegliere **Modifica posizione del gruppo e dati**.
1. Specificare **Intervallo dati** e **Posizione**.

Il seguente codice di esempio carica il foglio di calcolo sorgente, accede al primo gruppo di Linee di tendenza e aggiunge nuovi intervalli e posizioni dati per il gruppo di Linee di tendenza. 

**Java**

{{< highlight csharp >}}

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

Si prega di controllare l'articolo [Copia Sparkline Specificando Raggio dei Dati e Posizione del Gruppo Sparkline](/cells/it/java/copiare-sparkline-specificando-raggio-dei-dati-e-posizione-del-gruppo-sparkline/) per ulteriori informazioni.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
