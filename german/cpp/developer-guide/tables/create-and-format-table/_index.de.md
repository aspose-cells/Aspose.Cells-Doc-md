---
title: Tabelle erstellen und formatieren
type: docs
weight: 10
url: /de/cpp/create-and-format-table/
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

|**Auswählen des Datenbereichs zum Erstellen des Listenobjekts**|
|:- |
|![todo: Bild_alt_Text](jHcNq4o.png)|
Dadurch wird das Dialogfeld „Liste erstellen“ angezeigt.

|**Dialogfeld „Liste erstellen“.**|
|:- |
|![todo: Bild_alt_Text](kJmukRF.png)|
 Implementieren des List-Objekts für die Daten und Angeben der Gesamtzeile (Select**Daten** , dann**Aufführen** , gefolgt von**Gesamtreihe**).

|**Erstellen eines Listenobjekts**|
|:- |
|![todo: Bild_alt_Text](ECSGVdR.png)|
### **Mit Aspose.Cells API**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält eine[IArbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Die Klasse bietet eine breite Palette von Methoden zum Verwalten eines Arbeitsblatts. Um eine zu erstellen[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) Verwenden Sie in einem Arbeitsblatt die[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) Erhebungsverfahren der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Jede `[IListObject]` ist nämlich ein Objekt der[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) Klasse, die außerdem die[Addieren](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)Methode zum Hinzufügen eines `[IListObject]`-Objekts und zum Angeben eines Zellbereichs für die Liste.

 Gemäß dem angegebenen Zellbereich wird das Objekt `[IListObject]` von Aspose.Cells erstellt. Verwenden Sie Attribute (z[Summen anzeigen](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) und[ListColumns](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)usw.) der Klasse `[IListObject]`, um die Liste zu steuern.

Im folgenden Beispiel haben wir dieselbe `[IListObject]` mit Aspose.Cells API erstellt, die wir mit Microsoft Excel im obigen Abschnitt erstellt haben.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Formatiere eine Tabelle**
Um eine Gruppe verwandter Daten zu verwalten und zu analysieren, ist es möglich, einen Zellbereich in ein Listenobjekt (auch bekannt als Excel-Tabelle) umzuwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die zugehörige Daten enthalten, die unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist für jede Spalte in der Tabelle die Filterung in der Kopfzeile aktiviert, sodass Sie Ihre Listenobjektdaten schnell filtern oder sortieren können. Sie können dem Listenobjekt, das eine Dropdown-Liste mit Aggregatfunktionen für jede Summenzeilenzelle bereitstellt, eine Summenzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) hinzufügen. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).
### **Formatieren eines Listenobjekts**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält eine[IArbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) -Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um eine zu erstellen*Listenobjekt*Verwenden Sie in einem Arbeitsblatt `IListObjectCollection`. Jedes `[IListObject]` ist tatsächlich ein Objekt der `IListObjectCollection`-Klasse, die außerdem das bereitstellt[Addieren](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)Methode zum Hinzufügen eines `[IListObject]`-Objekts und geben Sie den Zellbereich an, den es umfassen soll. Gemäß dem angegebenen Zellbereich a*Listenobjekt* wird im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B.[TableStyleType](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) der Klasse `[IListObject]`, um die Tabelle für Ihre Anforderungen zu formatieren.

Das folgende Beispiel fügt Beispieldaten zu einem Arbeitsblatt hinzu, fügt ein `[IListObject]` hinzu und wendet Standardstile darauf an. `[IListObject]` Stile werden von Microsoft Excel 2007/2010 unterstützt.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
