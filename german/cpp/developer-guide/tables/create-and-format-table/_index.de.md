---
title: Tabelle erstellen und formatieren
type: docs
weight: 10
url: /de/cpp/create-and-format-table/
---
##  **Tabelle erstellen**
Einer der Vorteile von Tabellenkalkulationen besteht darin, dass Sie damit verschiedene Arten von Listen erstellen können, beispielsweise Telefonlisten, Aufgabenlisten, Listen mit Transaktionen, Vermögenswerten oder Verbindlichkeiten. Mehrere Benutzer können zusammenarbeiten, um verschiedene Listen zu verwenden, zu erstellen und zu pflegen.

Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.
###  **Vorteile eines Listenobjekts**
Es gibt einige Vorteile, wenn Sie eine Datenliste in ein tatsächliches Listenobjekt konvertieren

- Neue Zeilen und Spalten werden automatisch eingefügt.
- Eine Gesamtzeile am Ende Ihrer Liste kann einfach hinzugefügt werden, um SUMME, DURCHSCHNITT, ANZAHL usw. anzuzeigen.
- Rechts hinzugefügte Spalten werden automatisch in das List-Objekt integriert.
- Auf Zeilen und Spalten basierende Diagramme werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugewiesen sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.
###  **Erstellen eines Listenobjekts mit Microsoft Excel**

|**Auswählen des Datenbereichs zum Erstellen eines Listenobjekts**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Dadurch wird das Dialogfeld „Liste erstellen“ angezeigt.

|**Dialogfeld „Liste erstellen“.**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementieren des Listenobjekts für die Daten und Angeben der Gesamtzeile (wählen Sie *Daten**, dann *Liste**, gefolgt von *Gesamtzeile**).

|**Erstellen eines Listenobjekts**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
###  **Mit Aspose.Cells API**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Die Klasse bietet eine breite Palette von Methoden zum Verwalten eines Arbeitsblatts. Um eine zu erstellen[ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) Verwenden Sie in einem Arbeitsblatt das[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) Sammelmethode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Jede `[ListObject]` ist tatsächlich ein Objekt der[ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) Klasse, die weiterhin Folgendes bereitstellt[Hinzufügen](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)Methode zum Hinzufügen eines `[ListObject]`-Objekts und zum Angeben eines Zellbereichs für die Liste.

 Entsprechend dem angegebenen Zellbereich wird das Objekt `[ListObject]` von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) Und[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)usw.) der Klasse `[ListObject]` zur Steuerung der Liste.

Im folgenden Beispiel haben wir dieselbe `[ListObject]` mit Aspose.Cells API erstellt wie im obigen Abschnitt mit Microsoft Excel.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Formatieren Sie eine Tabelle**
Um eine Gruppe zusammengehöriger Daten zu verwalten und zu analysieren, ist es möglich, einen Zellbereich in ein Listenobjekt (auch als Excel-Tabelle bezeichnet) umzuwandeln. Eine Tabelle besteht aus einer Reihe von Zeilen und Spalten, die zusammengehörige Daten enthalten, die unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist für jede Spalte in der Tabelle die Filterung in der Kopfzeile aktiviert, sodass Sie Ihre Listenobjektdaten schnell filtern oder sortieren können. Sie können eine Summenzeile (eine spezielle Zeile in einer Liste, die eine Auswahl an Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) zum Listenobjekt hinzufügen, das eine Dropdown-Liste mit Aggregatfunktionen für jede Summenzeilenzelle bereitstellt. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).
###  **Formatieren eines Listenobjekts**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Die Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um eine zu erstellen*ListObject*Verwenden Sie in einem Arbeitsblatt `ListObjectCollection`. Jedes `[ListObject]` ist tatsächlich ein Objekt der Klasse `ListObjectCollection`, die darüber hinaus Folgendes bereitstellt[Hinzufügen](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)Methode zum Hinzufügen eines `[ListObject]`-Objekts und geben Sie den Zellbereich an, den es umfassen soll. Entsprechend dem angegebenen Zellbereich a*ListObject* wird im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B.[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) der Klasse `[ListObject]`, um die Tabelle entsprechend Ihren Anforderungen zu formatieren.

Im folgenden Beispiel werden Beispieldaten zu einem Arbeitsblatt hinzugefügt, ein `[ListObject]` hinzugefügt und Standardstile darauf angewendet. `[ListObject]`-Stile werden von Microsoft Excel 2007/2010 unterstützt.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
