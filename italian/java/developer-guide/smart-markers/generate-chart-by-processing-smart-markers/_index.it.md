---
title: Genera grafico elaborando marcatori intelligenti
type: docs
weight: 180
url: /it/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells Le API forniscono la classe WorkbookDesigner per lavorare con i marcatori intelligenti in cui la formattazione e le formule vengono inserite nei fogli di calcolo del designer e quindi elaborate rispetto a origini dati specificate per riempire i dati in base ai marcatori intelligenti. È anche possibile creare grafici Excel elaborando gli Smart Marker, che richiederanno i seguenti passaggi.

- Creazione del foglio di calcolo del designer
- Elaborazione del foglio di calcolo del progettista rispetto all'origine dati specificata
- Creazione di grafici basati su dati popolati

{{% /alert %}} 
## **Creazione del foglio di calcolo del progettista**
Un foglio di calcolo per designer è un semplice file Excel creato con l'applicazione Excel Microsoft o le API Aspose.Cells contenente la formattazione visiva, le formule e gli indicatori intelligenti, in cui i contenuti devono essere popolati in fase di esecuzione.

{{% alert color="primary" %}} 

 Sono disponibili informazioni dettagliate sugli Smart Marker[qui](/cells/it/java/smart-markers/).

{{% /alert %}} 

Per semplicità, creeremo il foglio di calcolo del progettista utilizzando Aspose.Cells for Java API e successivamente lo elaboreremo rispetto a un'origine dati creata dinamicamente a scopo dimostrativo.

**Java**

{{< highlight "csharp" >}}

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

Se si salva il foglio di lavoro risultante in questa fase, i dati nel foglio di lavoro appariranno come segue.

![cose da fare:immagine_alt_testo](generate-chart-by-processing-smart-markers_1.png)
## **Elaborazione del foglio di calcolo del progettista**
 Per elaborare il foglio di calcolo del designer, dobbiamo disporre di un'origine dati che corrisponda agli indicatori intelligenti utilizzati nel foglio di calcolo del designer. Ad esempio, abbiamo creato una voce Smart Marker come**&=$Intestazioni(orizzontale)** che rappresenta la variabile per nome Headers mentre la chiave**(orizzontale)** suggerisce che i dati dovrebbero essere popolati orizzontalmente.

Per dimostrare questo caso d'uso, creeremo l'origine dati da zero e la elaboreremo rispetto al foglio di calcolo del designer creato nel passaggio precedente. Tuttavia, nello scenario in tempo reale, i dati potrebbero essere già disponibili per un'ulteriore elaborazione, pertanto è possibile ignorare la creazione dell'origine dati se i dati sono già disponibili.

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

L'elaborazione degli Smart Marker è abbastanza semplice come segue.

**Java**

{{< highlight "csharp" >}}

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

Se salvi il foglio di calcolo in questa fase, i dati appariranno come segue.

![cose da fare:immagine_alt_testo](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Il frammento di codice precedente utilizza l'istanza esistente della classe Workbook creata nel primo passaggio. Se hai già il file del foglio di calcolo del progettista su disco o memoria, puoi creare un'istanza della classe Workbook caricando il foglio di calcolo del progettista esistente.

{{% /alert %}} 
## **Creazione del grafico**
Una volta che i dati sono a posto, tutto ciò che dobbiamo fare è creare un grafico basato sull'origine dati. Per semplificare l'esempio, utilizzeremo il metodo Chart.setChartDataRange in modo da non dover configurare ulteriormente il grafico.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Il grafico finale appare come segue.

![cose da fare:immagine_alt_testo](generate-chart-by-processing-smart-markers_3.png)
