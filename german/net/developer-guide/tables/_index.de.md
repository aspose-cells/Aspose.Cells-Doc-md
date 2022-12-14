---
title: Erstellen und verwalten Sie Tabellen von Microsoft Excel-Dateien.
linktitle: Tische
type: docs
weight: 150
url: /de/net/create-and-format-table/
description: Tabellen von Excel-Dateien mithilfe der Bibliothek Aspose.Cells einfügen, ändern, bearbeiten, löschen, formatieren.
---
## **Tabelle erstellen**

Einer der Vorteile von Tabellenkalkulationen besteht darin, dass Sie verschiedene Arten von Listen erstellen können, z. B. Telefonlisten, Aufgabenlisten, Listen mit Transaktionen, Vermögenswerten oder Verbindlichkeiten. Mehrere Benutzer können zusammenarbeiten, um verschiedene Listen zu verwenden, zu erstellen und zu pflegen.

Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.

### **Vorteile eines Listenobjekts**

Es gibt einige Vorteile, wenn Sie eine Datenliste in ein tatsächliches Listenobjekt konvertieren

- Neue Zeilen und Spalten werden automatisch eingefügt.
- Eine Summenzeile am Ende Ihrer Liste kann einfach hinzugefügt werden, um SUMME, MITTELWERT, ANZAHL usw. anzuzeigen.
- Rechts hinzugefügte Spalten werden automatisch in das List-Objekt übernommen.
- Diagramme, die auf Zeilen und Spalten basieren, werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugewiesen sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.

### **Erstellen eines Listenobjekts mit Microsoft Excel**

- Auswählen des Datenbereichs zum Erstellen eines Listenobjekts
- Dadurch wird das Dialogfeld „Liste erstellen“ angezeigt.
-  Implementieren Sie das List-Objekt für die Daten und geben Sie die Gesamtzeile an (Select**Daten** , dann**Aufführen** , gefolgt von**Gesamtreihe**).

### **Mit Aspose.Cells API**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um eine zu erstellen[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) Verwenden Sie in einem Arbeitsblatt die[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) Sammlungseigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Jeder[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ist in der Tat ein Objekt der[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) Klasse, die außerdem die[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)-Methode zum Hinzufügen eines List-Objekts und zum Angeben eines Zellbereichs für die Liste.

Gemäß dem angegebenen Zellbereich wird das List-Objekt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B.[**Summen anzeigen**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) , usw.) der[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Klasse, um die Liste zu steuern.

 In dem unten angegebenen Beispiel haben wir dasselbe erstellt[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Verwenden Sie Aspose.Cells API, wie wir es mit Microsoft Excel im obigen Abschnitt erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formatiere eine Tabelle**

Um eine Gruppe verwandter Daten zu verwalten und zu analysieren, ist es möglich, einen Zellbereich in ein Listenobjekt (auch bekannt als Excel-Tabelle) umzuwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die zugehörige Daten enthalten, die unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist für jede Spalte in der Tabelle die Filterung in der Kopfzeile aktiviert, sodass Sie Ihre Listenobjektdaten schnell filtern oder sortieren können. Sie können eine Summenzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) zu dem Listenobjekt hinzufügen, das eine Dropdown-Liste von Aggregatfunktionen für jede Summenzeilenzelle bereitstellt. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

### **Formatieren eines Listenobjekts**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um eine zu erstellen[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in einem Arbeitsblatt verwenden[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) Sammlungseigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Jeder[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ist in der Tat ein Objekt der[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) Klasse, die außerdem die[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) -Methode, um ein List-Objekt hinzuzufügen und den Zellbereich anzugeben, den es umfassen soll. Gemäß dem angegebenen Zellbereich a[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)wird im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B.[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) des[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Klasse, um die Tabelle für Ihre Anforderung zu formatieren.

 Das folgende Beispiel fügt Beispieldaten zu einem Arbeitsblatt hinzu, fügt a hinzu[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) und wenden Sie Standardstile darauf an.[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Stile werden von Microsoft Excel 2007/2010 unterstützt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Themen vorantreiben**
- [Tabelle in ODS konvertieren](/cells/de/net/convert-table-to-ods/)
- [Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen](/cells/de/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Lese- und Schreibtabelle mit Abfragetabellen-Datenquelle](/cells/de/net/read-and-write-table-with-query-table-data-source/)
- [Legen Sie den Kommentar des Tabellen- oder Listenobjekts im Arbeitsblatt fest](/cells/de/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabellen und Bereiche](/cells/de/net/tables-and-ranges/)

