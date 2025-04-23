---
title: Genera un grafico elaborando i marcatori intelligenti
type: docs
weight: 180
url: /it/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Le API di Aspose.Cells forniscono la classe WorkbookDesigner per lavorare con Smart Markers dove la formattazione e le formule sono posizionate nei fogli del designer e poi elaborate contro le fonti di dati specificate per riempire i dati in base agli Smart Markers. È anche possibile creare grafici Excel elaborando Smart Markers, il che richiederà i seguenti passaggi.

- Creazione del foglio di calcolo del designer
- Elaborazione del foglio elettronico del designer contro la fonte di dati specificata
- Creazione del grafico in base ai dati popolati

{{% /alert %}} 
## **Creazione del foglio elettronico del designer**
Un foglio elettronico del designer è un semplice file Excel creato con l'applicazione Microsoft Excel o le API di Aspose.Cells contenente la formattazione visuale, le formule e gli smart markers, dove i contenuti devono essere popolati al momento dell'esecuzione.

{{% alert color="primary" %}} 

Sono disponibili informazioni dettagliate sugli Smart Markers [qui](/cells/it/java/smart-markers/).

{{% /alert %}} 

Per semplicità, creeremo il foglio elettronico del designer utilizzando l'API Aspose.Cells for Java e in seguito lo elaboreremo contro una fonte di dati creata dinamicamente a scopo dimostrativo.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

Se si salva il foglio elettronico risultante a questo punto, i dati nel foglio di lavoro appariranno come segue.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Elaborazione del foglio elettronico del designer**
Per elaborare il foglio elettronico del designer, è necessario disporre di una fonte di dati che corrisponda agli Smart Markers utilizzati nel foglio elettronico del designer. Ad esempio, abbiamo creato un'entry Smart Marker come **&=$Headers(horizontal)**, che rappresenta la variabile per nome Headers mentre la chiave **(horizontal)** suggerisce che i dati dovrebbero essere popolati in orizzontale.

Per dimostrare questo caso d'uso, creeremo la fonte di dati da zero e la elaboreremo contro il foglio elettronico del designer creato nel passo precedente. Tuttavia, in uno scenario in tempo reale, i dati potrebbero già essere disponibili per ulteriore elaborazione e quindi è possibile saltare la creazione della fonte di dati se i dati sono già disponibili.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

L'elaborazione degli Smart Markers è piuttosto semplice come segue.

**Java**

{{< highlight csharp >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

Se si salva il foglio elettronico a questo punto, i dati appariranno come segue.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Il frammento di codice sopra utilizza l'istanza esistente della classe Workbook creata nel primo passaggio. Se si dispone già del file di foglio di calcolo del designer su disco o in memoria, è possibile creare un'istanza della classe Workbook caricando il foglio di calcolo del designer esistente.

{{% /alert %}} 
## **Creazione del grafico**
Una volta che i dati sono in posizione, tutto ciò che dobbiamo fare è creare un grafico basato sulla fonte di dati. Per mantenere l'esempio semplice, utilizzeremo il metodo Chart.setChartDataRange in modo da non dover configurare ulteriormente il grafico.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Il grafico finale appare come segue.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
{{< app/cells/assistant language="java" >}}
