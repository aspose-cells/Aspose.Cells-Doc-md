---
title: Tabelle erstellen und formatieren
type: docs
weight: 10
url: /de/go-cpp/create-and-format-table/
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

|**Datenauswahl zum Erstellen eines Listenobjekts**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Dies zeigt das Dialogfeld 'Liste erstellen' an.

|**Liste erstellen Dialogfeld**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementierung des Listenobjekts für die Daten und Angabe der Gesamtzeile (Wählen Sie **Daten**, dann **Liste** und anschließend **Gesamtzeile**).

|**Erstellen eines Listenobjekts**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|

### **Verwendung der Aspose.Cells-API**

Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung eines Arbeitsblatts. Um ein [ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) in einem Arbeitsblatt zu erstellen, verwenden Sie die [GetListObjects](https://reference.aspose.com/cells/go-cpp/worksheet/getlistobjects/) Methode der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse. Jedes `[ListObject]` ist tatsächlich ein Objekt der Klasse [ListObjectCollection](https://reference.aspose.com/cells/go-cpp/listobjectcollection/), die wiederum die [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add_int_int_int_int_bool/) Methode zum Hinzufügen eines `[ListObject]` Objekts sowie zur Angabe eines Zellbereichs für die Liste bereitstellt.

Gemäß dem angegebenen Zellbereich wird das `[ListObject]` Objekt von Aspose.Cells erstellt. Verwenden Sie Attribute (zum Beispiel [SetShowTotals](https://reference.aspose.com/cells/go-cpp/listobject/setshowtotals/) und [GetListColumns](https://reference.aspose.com/cells/go-cpp/listobject/getlistcolumns/) usw.) der `[ListObject]` Klasse, um die Liste zu steuern.

Im untenstehenden Beispiel haben wir dieselbe `[ListObject]` unter Verwendung der Aspose.Cells-API erstellt, wie wir sie im obigen Abschnitt mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingListObjects.go" >}}

## **Formatieren einer Tabelle**

Um eine Gruppe von verwandten Daten zu verwalten und zu analysieren, ist es möglich, einen Zellenbereich in ein Listenobjekt umzuwandeln (auch als Excel-Tabelle bekannt). Eine Tabelle ist eine Reihe von Zeilen und Spalten, die verwandte Daten enthalten und unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist in jeder Spalte der Tabelle in der Kopfzeile die Filterung aktiviert, sodass Sie Ihre Listenobjektdaten schnell filtern oder sortieren können. Sie können eine Gesamtzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die nützlich sind, um mit numerischen Daten zu arbeiten) zu dem Listenobjekt hinzufügen, die eine Dropdown-Liste von Aggregatfunktionen für jede Zellenzeile in der Gesamtzeile bereitstellt. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

### **Formatierung eines Listenobjekts**

Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung von Arbeitsblättern. Um ein *ListObject* in einem Arbeitsblatt zu erstellen, verwenden Sie `ListObjectCollection`. Jedes `[ListObject]` ist tatsächlich ein Objekt der Klasse `ListObjectCollection`, das die [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add/) Methode zum Hinzufügen eines `[ListObject]` Objekts sowie zur Angabe des Zellbereichs, den es umfassen soll, bereitstellt. Gemäß dem angegebenen Zellbereich wird ein *ListObject* in das Arbeitsblatt durch Aspose.Cells erstellt. Verwenden Sie Attribute (zum Beispiel [SetTableStyleType](https://reference.aspose.com/cells/go-cpp/listobject/settablestyletype/)) der `[ListObject]` Klasse, um die Tabelle entsprechend Ihren Anforderungen zu formatieren.

Das folgende Beispiel fügt Beispieldaten zu einer Arbeitsmappe hinzu, fügt ein `[ListObject]` hinzu und wendet Standardstile darauf an. `[ListObject]`-Stile werden von Microsoft Excel 2007/2010 unterstützt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatTable.go" >}}
