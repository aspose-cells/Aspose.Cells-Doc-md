---
title: Tabellen von Microsoft Excel Dateien erstellen und verwalten.
linktitle: Tabellen
type: docs
weight: 150
url: /de/python-net/create-and-format-table/
description: Fügen Sie mithilfe der Aspose.Cells Bibliothek Tabellen in Excel Dateien ein, ändern Sie deren Größe, bearbeiten Sie sie, löschen Sie sie und formatieren Sie sie.
---

## **Tabelle erstellen**

Einer der Vorteile von Tabellenkalkulationen besteht darin, dass Sie verschiedene Arten von Listen erstellen können, beispielsweise Telefonlisten, Aufgabenlisten, Listen von Transaktionen, Vermögenswerten oder Verbindlichkeiten. Mehrere Benutzer können zusammenarbeiten, um verschiedene Listen zu verwenden, zu erstellen und zu pflegen.

Aspose.Cells für Python via .NET unterstützt das Erstellen und Verwalten von Listen.

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

### **Verwendung der API von Aspose.Cells für Python via .NET**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe. Um eine [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in einer Arbeitsmappe zu erstellen, verwenden Sie die [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects)-Sammlungseigenschaft der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Jede [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) ist tatsächlich ein Objekt der Klasse [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool), die außerdem die Methode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) zum Hinzufügen eines Listenobjekts und zum Angeben eines Zellenbereichs für die Liste bereitstellt.

Entsprechend dem angegebenen Zellbereich wird das Listenobjekt von Aspose.Cells für Python via .NET erstellt. Verwenden Sie Attribute (zum Beispiel [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals), [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns) usw.) der Klasse [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject), um die Liste zu steuern.

Im untenstehenden Beispiel haben wir dasselbe [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) mit der API von Aspose.Cells für Python via .NET erstellt, wie wir es in der vorherigen Sektion mit Microsoft Excel geschaffen haben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **Formatieren einer Tabelle**

Um eine Gruppe verwandter Daten zu verwalten und zu analysieren, können Sie einen Zellbereich in ein Listenobjekt (auch bekannt als Excel-Tabelle) umwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die verwandte Daten enthalten und unabhängig von anderen Daten verwaltet werden. Standardmäßig hat jede Spalte in der Tabelle im Kopfzeilenbereich die Filterfunktion aktiviert, damit Sie Ihre Listendaten schnell filtern oder sortieren können. Sie können eine Summenzahlreihe (eine spezielle Zeile in einer Liste, die eine Auswahl an Aggregatfunktionen bietet, die bei der Arbeit mit numerischen Daten hilfreich sind) zur Listentabelle hinzufügen, die für jede Summenzeile eine Dropdown-Liste mit Aggregatfunktionen bereitstellt. Aspose.Cells für Python via .NET bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

### **Formatierung eines Listenobjekts**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um eine [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) in einem Arbeitsblatt zu erstellen, verwenden Sie die [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects)-Sammlungseigenschaft der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Jede [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) ist tatsächlich ein Objekt der Klasse [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection), das außerdem die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)-Methode bereitstellt, um ein Listenobjekt hinzuzufügen und den Bereich von Zellen anzugeben, den es umfassen soll. Gemäß dem angegebenen Zellenbereich wird durch Aspose.Cells eine [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) im Arbeitsblatt erstellt. Verwenden Sie Attribute (zum Beispiel [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) der Klasse [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject), um die Tabelle gemäß Ihren Anforderungen zu formatieren.

Das folgende Beispiel fügt Beispieldaten zu einem Arbeitsblatt hinzu, fügt eine [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) hinzu und wendet Standardstile darauf an. [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)-Stile werden von Microsoft Excel 2007/2010 unterstützt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **Erweiterte Themen**
- [Tabelle in ODS konvertieren](/cells/de/python-net/convert-table-to-ods/)
- [Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden](/cells/de/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Tabelle mit Abfrage-Tabellendatenquelle lesen und schreiben](/cells/de/python-net/read-and-write-table-with-query-table-data-source/)
- [Den Kommentar der Tabelle oder des Listenobjekts innerhalb des Arbeitsblatts festlegen](/cells/de/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabellen und Bereiche](/cells/de/python-net/tables-and-ranges/)


{{< app/cells/assistant language="python-net" >}}
