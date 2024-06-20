---
title: Diagramm durch Verarbeitung von Smart Markers generieren
type: docs
weight: 180
url: /de/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs bieten die Klasse WorkbookDesigner zum Arbeiten mit Smart Markers, in der die Formatierung und Formeln in den Designer-Arbeitsblättern platziert und dann gegen die angegebenen Datenquellen verarbeitet werden, um die Daten gemäß den Smart Markers zu füllen. Es ist auch möglich, Excel-Diagramme durch Verarbeitung von Smart Markern zu erstellen, was die folgenden Schritte erfordert.

- Erstellung der Designer-Arbeitsmappe
- Verarbeitung des Designer-Arbeitsblatts gegen die angegebene Datenquelle
- Erstellung eines Diagramms basierend auf den befüllten Daten

{{% /alert %}} 
## **Erstellung des Designer-Arbeitsblatts**
Ein Designer-Arbeitsblatt ist eine einfache Excel-Datei, die mit der Microsoft Excel-Anwendung oder Aspose.Cells APIs erstellt wurde und die visuelle Formatierung, Formeln und Smart Marker enthält, deren Inhalt zur Laufzeit bevölkert werden soll.

{{% alert color="primary" %}} 

Detaillierte Informationen zu Smart Markers sind [hier](/cells/de/java/smart-markers/) verfügbar.

{{% /alert %}} 

Zur Vereinfachung erstellen wir das Designer-Arbeitsblatt mit der Aspose.Cells for Java API und verarbeiten es später gegen eine dynamisch erstellte Datenquelle für Demonstrationszwecke.

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

Wenn Sie die resultierende Tabelle in diesem Stadium speichern, wird der Inhalt auf dem Arbeitsblatt wie folgt aussehen.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Verarbeitung des Designer-Arbeitsblatts**
Um das Designer-Arbeitsblatt zu verarbeiten, benötigen wir eine Datenquelle, die den Smart Markern im Designer-Arbeitsblatt entspricht. Wir haben beispielsweise einen Smart Marker-Eintrag als **&=$Headers(horizontal)** erstellt, der die Variable namens Headers repräsentiert, während der Schlüssel **(horizontal)** darauf hindeutet, dass die Daten horizontal bevölkert werden sollen.

Um diesen Anwendungsfall zu demonstrieren, erstellen wir die Datenquelle von Grund auf und verarbeiten sie gegen das Designer-Arbeitsblatt, das im vorherigen Schritt erstellt wurde. In einem realen Szenario könnten die Daten jedoch bereits verfügbar sein, weshalb Sie die Erstellung der Datenquelle überspringen können, wenn die Daten bereits vorhanden sind.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Die Verarbeitung von Smart Markers ist relativ einfach, wie folgt.

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

Wenn Sie die Tabelle in diesem Stadium speichern, wird der Inhalt wie folgt aussehen.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Der obige Codeausschnitt verwendet die vorhandene Instanz der Workbook-Klasse, die im ersten Schritt erstellt wurde. Wenn die Designer-Arbeitsblattdatei bereits auf dem Datenträger oder im Speicher vorhanden ist, können Sie eine Instanz der Workbook-Klasse erstellen, indem Sie das vorhandene Designer-Arbeitsblatt laden.

{{% /alert %}} 
## **Erstellung des Diagramms**
Sobald die Daten vorhanden sind, müssen wir nur noch ein Diagramm basierend auf der Datenquelle erstellen. Um das Beispiel einfach zu halten, verwenden wir die Methode Chart.setChartDataRange, sodass wir das Diagramm nicht weiter konfigurieren müssen.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Das endgültige Diagramm sieht wie folgt aus.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
