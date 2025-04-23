---
title: Filterobjekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 1060
url: /de/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie die Eigenschaft [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter), wenn Sie Daten aus der Arbeitsmappe filtern. Möchten Sie Daten aus einzelnen Arbeitsblättern filtern, müssen Sie die Methode [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet-com.aspose.cells.Worksheet-) überschreiben. Geben Sie beim Erstellen oder Arbeiten mit [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter) den entsprechenden Wert aus der Aufzählung [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) an.

Die Enumeration [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) hat die folgenden Werte.

- [KEINE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [ALLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [ZELLE_LEER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-BLANK)
- [ZELLE_TEXT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-STRING)
- [ZELLE_NUMERISCH](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-NUMERIC)
- [ZELLE_FEHLER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-ERROR)
- [ZELLE_BOOLEAN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-BOOL)
- [ZELLENWERT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-VALUE)
- [FORMEL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [ZELLE_DATEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-DATA)
- [DIAGRAMM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [ZUSAMMENGEFÜGTEN_BEREICH](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED-AREA)
- [BEDINGTE_FORMATIERUNG](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL-FORMATTING)
- [DATEN_VALIDIERUNG](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA-VALIDATION)
- [PIVOTTABELLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT-TABLE)
- [TABELLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLINKS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SHEET_EINSTELLUNGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET-SETTINGS)
- [SHEET_DATEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET-DATA)
- [BUCH_EINSTELLUNGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK-SETTINGS)
- [EINSTELLUNGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML-MAP)
- [STRUKTUR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [DOKUMENT_EIGENSCHAFTEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT-PROPERTIES)
- [DEFINIERTE_NAMEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STIL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filterobjekte beim Laden der Arbeitsmappe**
Der folgende Beispielcode veranschaulicht, wie Diagramme aus der Arbeitsmappe gefiltert werden. Bitte überprüfen Sie die [Beispiel Excel-Datei](5472489.xlsx), die in diesem Code verwendet wird, und die generierte [Ausgabe-PDF-Datei](5472488.pdf). Wie Sie im Ausgabe-PDF sehen können, wurden alle Diagramme aus der Arbeitsmappe gefiltert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filterobjekte beim Laden des Arbeitsblatts**
Der folgende Beispielcode lädt die [Quelldatei Excel](5472492.xlsx) und filtert die folgenden Daten aus ihren Tabellen mithilfe eines benutzerdefinierten Filters.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert bedingte Formatierungen aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

Sobald die [Quelldatei Excel](5472492.xlsx) mit einem benutzerdefinierten Filter geladen wurde, werden die Bilder aller Tabellenblätter nacheinander aufgenommen. Hier sind die Ausgabebilder zur Ansicht. Wie Sie sehen können, hat das erste Bild keine Diagramme, das zweite Bild keine Formen und das dritte Bild hat keine bedingte Formatierung.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
{{< app/cells/assistant language="java" >}}
