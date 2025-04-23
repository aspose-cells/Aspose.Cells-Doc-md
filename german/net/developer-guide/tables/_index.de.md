---
title: Tabellen von Microsoft Excel Dateien erstellen und verwalten.
linktitle: Tabellen
type: docs
weight: 150
url: /de/net/create-and-format-table/
description: Fügen Sie mithilfe der Aspose.Cells Bibliothek Tabellen in Excel Dateien ein, ändern Sie deren Größe, bearbeiten Sie sie, löschen Sie sie und formatieren Sie sie.
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

- Auswahl des Datumsbereichs zur Erstellung eines Listenobjekts
- Dies zeigt den Dialog zum Erstellen einer Liste an.
- Implementieren Sie das Listenobjekt für die Daten und geben Sie die Gesamtzeile an (Wählen Sie **Daten**, dann **Liste**, gefolgt von **Gesamtzeile**).

### **Verwendung der Aspose.Cells-API**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht.

Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe. Um eine [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in einer Arbeitsmappe zu erstellen, verwenden Sie die [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)-Sammlungseigenschaft der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Jede [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ist tatsächlich ein Objekt der Klasse [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), die außerdem die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) zum Hinzufügen eines Listenobjekts und zum Angeben eines Zellenbereichs für die Liste bereitstellt.

Gemäß dem angegebenen Zellenbereich wird das Listenobjekt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B. [**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) usw.) der Klasse [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject), um die Liste zu steuern.

In dem unten gegebenen Beispiel haben wir dasselbe [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) erstellt, indem wir die Aspose.Cells-API verwendet haben, wie wir es im obigen Abschnitt mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formatieren einer Tabelle**

Um eine Gruppe von verwandten Daten zu verwalten und zu analysieren, ist es möglich, einen Bereich von Zellen in ein Listenobjekt (auch bekannt als Excel-Tabelle) umzuwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die verwandte Daten enthalten und unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist in jeder Spalte der Tabelle in der Kopfzeile die Filterung aktiviert, sodass Sie Ihre Listenaufzugsdaten schnell filtern oder sortieren können. Sie können eine Gesamtzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) zu dem Listenobjekt hinzufügen, um eine Dropdown-Liste von Aggregatfunktionen für jede Zellen in der Gesamtzeile bereitzustellen. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

### **Formatierung eines Listenobjekts**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um eine [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in einem Arbeitsblatt zu erstellen, verwenden Sie die [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)-Sammlungseigenschaft der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Jede [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ist tatsächlich ein Objekt der Klasse [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), das außerdem die [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)-Methode bereitstellt, um ein Listenobjekt hinzuzufügen und den Bereich von Zellen anzugeben, den es umfassen soll. Gemäß dem angegebenen Zellenbereich wird durch Aspose.Cells eine [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) im Arbeitsblatt erstellt. Verwenden Sie Attribute (zum Beispiel [**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)) der Klasse [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject), um die Tabelle gemäß Ihren Anforderungen zu formatieren.

Das folgende Beispiel fügt Beispieldaten zu einem Arbeitsblatt hinzu, fügt eine [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) hinzu und wendet Standardstile darauf an. [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)-Stile werden von Microsoft Excel 2007/2010 unterstützt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Erweiterte Themen**
- [Tabelle in ODS konvertieren](/cells/de/net/convert-table-to-ods/)
- [Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden](/cells/de/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Tabelle mit Abfrage-Tabellendatenquelle lesen und schreiben](/cells/de/net/read-and-write-table-with-query-table-data-source/)
- [Den Kommentar der Tabelle oder des Listenobjekts innerhalb des Arbeitsblatts festlegen](/cells/de/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabellen und Bereiche](/cells/de/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
