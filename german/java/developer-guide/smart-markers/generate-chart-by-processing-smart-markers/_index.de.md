---
title: Erstellen Sie ein Diagramm, indem Sie Smart-Marker verarbeiten
type: docs
weight: 180
url: /de/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells-APIs stellen die WorkbookDesigner-Klasse bereit, um mit Smart Markers zu arbeiten, wobei die Formatierung und Formeln in den Designer-Tabellen platziert und dann mit angegebenen Datenquellen verarbeitet werden, um die Daten gemäß den Smart Markers aufzufüllen. Es ist auch möglich, Excel-Diagramme durch die Verarbeitung von Smart Markern zu erstellen, was die folgenden Schritte erfordert.

- Erstellung von Designer-Tabellenkalkulationen
- Verarbeitung des Designer-Arbeitsblatts anhand der angegebenen Datenquelle
- Erstellung von Diagrammen basierend auf ausgefüllten Daten

{{% /alert %}} 
## **Erstellung einer Designer-Tabelle**
Eine Designer-Tabelle ist eine einfache Excel-Datei, die mit der Excel-Anwendung Microsoft oder den APIs Aspose.Cells erstellt wurde und die visuelle Formatierung, Formeln und intelligente Markierungen enthält, in die der Inhalt zur Laufzeit eingefügt werden soll.

{{% alert color="primary" %}} 

 Detaillierte Informationen zu Smart Markern sind verfügbar[Hier](/cells/de/java/smart-markers/).

{{% /alert %}} 

Der Einfachheit halber erstellen wir das Designer-Arbeitsblatt mit Aspose.Cells for Java API und verarbeiten es später zu Demonstrationszwecken gegen eine dynamisch erstellte Datenquelle.

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

Wenn Sie die resultierende Tabelle zu diesem Zeitpunkt speichern, sehen die Daten im Arbeitsblatt wie folgt aus.

![todo: Bild_alt_Text](generate-chart-by-processing-smart-markers_1.png)
## **Designer-Tabelle verarbeiten**
 Um die Designer-Tabelle zu verarbeiten, benötigen wir eine Datenquelle, die den in der Designer-Tabelle verwendeten Smart Markern entspricht. Zum Beispiel haben wir einen Smart-Marker-Eintrag als erstellt**&=$Kopfzeilen(horizontal)** das die Variable nach Namen Headers darstellt, während der Schlüssel**(horizontal)** schlägt vor, dass die Daten horizontal ausgefüllt werden sollten.

Um diesen Anwendungsfall zu demonstrieren, erstellen wir die Datenquelle von Grund auf neu und verarbeiten sie mit der im vorherigen Schritt erstellten Designer-Tabelle. In einem Echtzeitszenario könnten Daten jedoch bereits für die weitere Verarbeitung verfügbar sein, sodass Sie die Erstellung einer Datenquelle überspringen können, wenn bereits Daten verfügbar sind.

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Die Verarbeitung von Smart Markern ist ganz einfach wie folgt.

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

Wenn Sie die Tabelle zu diesem Zeitpunkt speichern, sehen die Daten wie folgt aus.

![todo: Bild_alt_Text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Der obige Codeausschnitt verwendet die vorhandene Instanz der Workbook-Klasse, die im ersten Schritt erstellt wurde. Wenn Sie die Designer-Tabellendatei bereits auf der Festplatte oder im Speicher haben, können Sie eine Instanz der Workbook-Klasse erstellen, indem Sie die vorhandene Designer-Tabelle laden.

{{% /alert %}} 
## **Erstellung von Diagrammen**
Sobald die Daten vorhanden sind, müssen wir nur noch ein Diagramm basierend auf der Datenquelle erstellen. Um das Beispiel einfach zu halten, verwenden wir die Methode Chart.setChartDataRange, damit wir das Diagramm nicht weiter konfigurieren müssen.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Das endgültige Diagramm sieht wie folgt aus.

![todo: Bild_alt_Text](generate-chart-by-processing-smart-markers_3.png)
