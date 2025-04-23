---
title: Erstellen und verwalten Tabellen von Microsoft Excel Dateien mit Node.js über C++
linktitle: Tabellen
type: docs
weight: 150
url: /de/nodejs-cpp/create-and-format-table/
description: Tabellen in Excel Dateien mit Aspose.Cells for Node.js via C++ einfügen, skalieren, bearbeiten, löschen und formatieren.
---

## **Tabelle erstellen**

Einer der Vorteile von Tabellenkalkulationen besteht darin, dass Sie verschiedene Arten von Listen erstellen können, beispielsweise Telefonlisten, Aufgabenlisten, Listen von Transaktionen, Vermögenswerten oder Verbindlichkeiten. Mehrere Benutzer können zusammenarbeiten, um verschiedene Listen zu verwenden, zu erstellen und zu pflegen.

Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.

### **Vorteile eines Listenobjekts**

Es gibt einige Vorteile, wenn Sie eine Liste von Daten in ein tatsächliches Listenobjekt konvertieren.

- Neue Zeilen und Spalten werden automatisch einbezogen.
- Am unteren Rand Ihrer Liste kann ganz einfach eine Gesamtzeile hinzugefügt werden, um SUMME, DURCHSCHNITT, ANZAHL usw. anzuzeigen.
- Hinzugefügte Spalten rechts werden automatisch in das Listenobjekt aufgenommen.
- Diagramme, die auf Zeilen und Spalten basieren, werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugeordnet sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.

### **Erstellen eines Listenobjekts mit Microsoft Excel**

- Auswahl des Datenbereichs für die Erstellung eines List-Objekts
- Dies zeigt den Dialog zum Erstellen einer Liste an.
- Implementieren Sie das List-Objekt für die Daten und geben Sie die Gesamtzeile an (Wählen Sie **Daten**, dann **Liste**, gefolgt von **Gesamtzeile**).

### **Verwendung der Aspose.Cells-API**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um ein [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) in einem Arbeitsblatt zu erstellen, verwenden Sie die [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--)-Sammlungseigenschaft der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse. Jedes [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) ist in Wirklichkeit ein Objekt der [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/)-Klasse, die weiterhin die [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-)-Methode zum Hinzufügen eines List-Objekts und zur Angabe eines Zellbereichs für die Liste bereitstellt.

Gemäß dem angegebenen Zellbereich wird das List-Objekt von Aspose.Cells erstellt. Verwenden Sie Attribute (zum Beispiel [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--) usw.) der [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)-Klasse, um die Liste zu steuern.

Im untenstehenden Beispiel haben wir dasselbe [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) mit der Aspose.Cells-API erstellt, wie wir im vorherigen Abschnitt mit Microsoft Excel erstellt haben.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Formatieren einer Tabelle**

Um eine Gruppe von verwandten Daten zu verwalten und zu analysieren, ist es möglich, einen Bereich von Zellen in ein Listenobjekt (auch bekannt als Excel-Tabelle) umzuwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die verwandte Daten enthalten und unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist in jeder Spalte der Tabelle in der Kopfzeile die Filterung aktiviert, sodass Sie Ihre Listenaufzugsdaten schnell filtern oder sortieren können. Sie können eine Gesamtzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) zu dem Listenobjekt hinzufügen, um eine Dropdown-Liste von Aggregatfunktionen für jede Zellen in der Gesamtzeile bereitzustellen. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

### **Formatierung eines Listenobjekts**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um ein [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) in einem Arbeitsblatt zu erstellen, verwenden Sie die [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--)-Sammlungseigenschaft der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse. Jedes [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) ist in Wirklichkeit ein Objekt der [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/)-Klasse, die die [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-)-Methode zum Hinzufügen eines List-Objekts und zur Angabe des Zellbereichs bereitstellt. Gemäß dem spezifizierten Zellbereich wird in dem Arbeitsblatt durch Aspose.Cells ein [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) erstellt. Verwenden Sie Attribute (zum Beispiel [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) der [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)-Klasse, um die Tabelle entsprechend Ihren Anforderungen zu formatieren.

Das folgende Beispiel fügt einem Arbeitsblatt Beispieldaten hinzu, fügt ein [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) hinzu und wendet Standardstile darauf an. [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)-Stile werden von Microsoft Excel 2007/2010 unterstützt.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Erweiterte Themen**
- [Tabelle in ODS konvertieren](/cells/de/nodejs-cpp/convert-table-to-ods/)
- [Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden](/cells/de/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Tabelle mit Abfrage-Tabellendatenquelle lesen und schreiben](/cells/de/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Den Kommentar der Tabelle oder des Listenobjekts innerhalb des Arbeitsblatts festlegen](/cells/de/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabellen und Bereiche](/cells/de/nodejs-cpp/tables-and-ranges/)

