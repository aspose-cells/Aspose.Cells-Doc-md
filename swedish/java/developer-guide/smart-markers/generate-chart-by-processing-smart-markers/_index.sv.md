---
title: Generera diagram genom att bearbeta smarta markörer
type: docs
weight: 180
url: /sv/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API:er tillhandahåller WorkbookDesigner-klassen för att arbeta med Smart Markers där formateringen och formlerna placeras i designerkalkylbladen och sedan bearbetas mot specificerade datakällor för att fylla upp data enligt Smart Markers. Det är också möjligt att skapa Excel-diagram genom att bearbeta smarta markörer, vilket kräver följande steg.

- Skapande av designerkalkylblad
- Bearbetar designerkalkylblad mot angiven datakälla
- Skapande av diagram baserat på ifyllda data

{{% /alert %}} 
## **Skapande av designerkalkylblad**
Ett designerkalkylblad är en enkel Excel-fil skapad med Microsoft Excel-applikation eller Aspose.Cells API:er som innehåller visuell formatering, formler och smarta markörer, där innehållet ska fyllas i under körning.

{{% alert color="primary" %}} 

 Detaljerad information om Smart Markers finns tillgänglig[här](/cells/sv/java/smart-markers/).

{{% /alert %}} 

För enkelhetens skull kommer vi att skapa designerkalkylarket med hjälp av Aspose.Cells for Java API, och senare bearbeta det mot en dynamiskt skapad datakälla för demonstrationsändamål.

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

Om du sparar det resulterande kalkylarket i detta skede kommer data i kalkylbladet att se ut som följer.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Bearbetar Designer-kalkylblad**
 För att kunna bearbeta designerkalkylarket måste vi ha en datakälla som motsvarar de smarta markörer som används i designerkalkylarket. Till exempel har vi skapat en Smart Marker-post som**&=$Headers(horisontella)** som representerar variabeln med namn Rubriker medan nyckeln**(horisontell)** föreslår att uppgifterna ska fyllas i horisontellt.

För att demonstrera detta användningsfall kommer vi att skapa datakällan från början och bearbeta den mot designerkalkylbladet som skapades i föregående steg. Men i realtidsscenariot kan data redan vara tillgängliga för vidare bearbetning så att du kan hoppa över skapandet av datakällan om data redan är tillgänglig.

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Bearbetning av smarta markörer är ganska enkel som följer.

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

Om du sparar kalkylarket i detta skede kommer uppgifterna att se ut som följer.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Ovan kodavsnitt använder den befintliga instansen av Workbook-klassen som skapades i det första steget. Om du redan har designerkalkylarksfilen på disk eller minne kan du skapa en instans av Workbook-klassen genom att ladda det befintliga designerkalkylarket.

{{% /alert %}} 
## **Skapande av diagram**
När data är på plats behöver vi bara skapa ett diagram baserat på datakällan. För att hålla exemplet enkelt kommer vi att använda metoden Chart.setChartDataRange så att vi inte behöver konfigurera diagrammet ytterligare.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Det slutliga diagrammet ser ut som följer.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
