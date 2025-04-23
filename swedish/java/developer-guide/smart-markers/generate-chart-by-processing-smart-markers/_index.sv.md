---
title: Skapa diagram genom att bearbeta Smart Markers
type: docs
weight: 180
url: /sv/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API:er tillhandahåller klassen WorkbookDesigner för att arbeta med Smart Markers där formateringar och formler placeras i designer-kalkylbladen och sedan bearbetas mot angivna datakällor för att fylla på datan enligt Smart Markers. Det är också möjligt att skapa Excel-diagram genom att bearbeta Smart Markers, vilket kommer att kräva följande steg.

- Skapande av designer-kalkylblad
- Bearbetning av designer-kalkylblad mot angiven datakälla
- Skapande av diagram baserat på ifylld data

{{% /alert %}} 
## **Skapande av Designer-kalkylblad**
Ett designer-kalkylblad är en enkel Excel-fil skapad med Microsoft Excel-programmet eller Aspose.Cells API:er som innehåller visuell formatering, formler och smarta markeringar, där innehållet ska fyllas på vid körning.

{{% alert color="primary" %}} 

Detaljerad information om Smart Markers finns tillgänglig [här](/cells/sv/java/smart-markers/).

{{% /alert %}} 

För enkelhetens skull kommer vi att skapa designer-kalkylbladet med hjälp av Aspose.Cells for Java API:et, och senare bearbeta det mot en dynamiskt skapad datakälla för demonstrationsändamål.

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

Om du sparar det resulterande kalkylbladet vid detta stadium, kommer datan i arbetsbladet att se ut som följer.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Bearbetning av Designer-kalkylblad**
För att kunna bearbeta designer-kalkylbladet måste vi ha en datakälla som motsvarar de smarta markeringar som används i designer-kalkylbladet. Till exempel har vi skapat en Smart Marker-inlägg som **&=$Headers(horizontal)**, som representerar variabeln med namnet Headers medan nyckeln **(horizontal)** antyder att datan ska fyllas i horisontellt.

För att demonstrera detta fall kommer vi skapa datakällan från grunden och bearbeta den mot designer-kalkylbladet som skapats i föregående steg. I praktiska scenarier kan datan redan vara tillgänglig för vidare bearbetning så du kan hoppa över skapandet av datakällan om datan redan finns tillgänglig.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Bearbetning av Smart Markers är ganska enkel enligt följande.

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

Om du sparar kalkylbladet vid detta stadium kommer datan att se ut som följer.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Ovanstående kodsnutt använder den befintliga instansen av klassen Workbook som skapades i det första steget. Om du redan har designer-kalkylbladsfilen på hårddisken eller i minnet kan du skapa en instans av klassen Workbook genom att ladda den befintliga designer-kalkylbladsfilen.

{{% /alert %}} 
## **Skapande av Diagram**
När datan är på plats behöver vi bara skapa ett diagram baserat på datakällan. För att göra exempelv används här metoden Chart.setChartDataRange så att vi inte behöver konfigurera diagrammet ytterligare.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Det slutgiltiga diagrammet ser ut som följer.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
{{< app/cells/assistant language="java" >}}
