---
title: Filtern Sie Objekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 1060
url: /de/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Mögliche Nutzungsszenarien**
 Bitte verwende[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) -Eigenschaft beim Filtern von Daten aus der Arbeitsmappe. Wenn Sie jedoch Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie überschreiben[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) Methode. Bitte geben Sie den entsprechenden Wert aus der an[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) Aufzählung beim Erstellen oder Arbeiten mit[Ladefilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 Das[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)Enumeration hat die folgenden Werte.

- [KEINER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [ALLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [ZELLE_LEER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMEL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [DIAGRAMM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [BEDINGTE FORMATIERUNG](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [DATENVALIDIERUNG](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [PIVOT_TABLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TISCH](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLINKS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [BLATT_EINSTELLUNGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [BLATT_DATEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BUCH_EINSTELLUNGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [DIE EINSTELLUNGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [STRUKTUR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [DOKUMENTEIGENSCHAFTEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STIL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filtern Sie Objekte beim Laden der Arbeitsmappe**
 Der folgende Beispielcode veranschaulicht, wie Diagramme aus der Arbeitsmappe gefiltert werden. Bitte überprüfen Sie die[Excel-Beispieldatei](5472489.xlsx) in diesem Code verwendet und die[PDF ausgeben](5472488.pdf)dadurch erzeugt. Wie Sie im Ausgabe-PDF sehen können, wurden alle Diagramme aus der Arbeitsmappe herausgefiltert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Objekte beim Laden des Arbeitsblatts filtern**
 Der folgende Beispielcode lädt die[Excel-Quelldatei](5472492.xlsx) und filtert die folgenden Daten aus seinen Arbeitsblättern mit einem benutzerdefinierten Filter.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert die bedingte Formatierung aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

 Einmal lädt es die[Excel-Quelldatei](5472492.xlsx) Mit einem benutzerdefinierten Filter werden die Bilder aller Arbeitsblätter einzeln aufgenommen. Hier sind die Ausgabebilder für Ihre Referenz. Wie Sie sehen, hat das erste Bild keine Diagramme, das zweite Bild keine Formen und das dritte Bild keine bedingte Formatierung.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
