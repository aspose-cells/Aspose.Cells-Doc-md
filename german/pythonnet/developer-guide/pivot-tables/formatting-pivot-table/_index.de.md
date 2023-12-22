---
title: Pivot-Tabelle formatieren
type: docs
weight: 10
url: /de/net/formatting-pivot-table/
description: So formatieren Sie eine Pivot-Tabelle mit Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **Aussehen der Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle: Hier erfahren Sie, wie Sie eine einfache Pivot-Tabelle erstellen. In diesem Artikel wird beschrieben, wie Sie das Erscheinungsbild einer Pivot-Tabelle anpassen, indem Sie verschiedene Eigenschaften festlegen:

- Formatoptionen für Pivot-Tabellen
- Formatoptionen für Pivot-Felder
- Optionen für das Datenfeldformat

###  **Formatoptionen für Pivot-Tabellen festlegen**

 Der[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)Die Klasse steuert die gesamte Pivot-Tabelle und kann auf verschiedene Arten formatiert werden.

####  **Festlegen des AutoFormat-Typs**

Microsoft Excel bietet eine Reihe verschiedener voreingestellter Berichtsformate. Aspose.Cells for Python via .NET unterstützen diese Formatierungsoptionen ebenfalls. Um darauf zuzugreifen:

1.  Satz[**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)zu *wahr**.
1.  Weisen Sie eine Formatierungsoption zu[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)Aufzählung.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Festlegen von Formatoptionen**

Das folgende Codebeispiel zeigt, wie Sie die Pivot-Tabelle formatieren, um Gesamtsummen für Zeilen und Spalten anzuzeigen, und wie Sie die Feldreihenfolge des Berichts festlegen. Außerdem wird gezeigt, wie eine Kundenzeichenfolge für Nullwerte festgelegt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Erscheinungsbild manuell formatieren**

Um das Aussehen des Pivot-Tabellenberichts manuell zu formatieren, verwenden Sie statt voreingestellter Berichtsformate die[**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) Und[**PivotTable.format(Zeile, Spalte, Stil)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)Methoden. Erstellen Sie ein Stilobjekt für Ihre gewünschte Formatierung, zum Beispiel:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Formatoptionen für Pivot-Felder festlegen**

 Der[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)Die Klasse stellt ein Feld in einer Pivot-Tabelle dar und kann auf verschiedene Arten formatiert werden. Das folgende Codebeispiel zeigt, wie Sie:

- Auf Zeilenfelder zugreifen.
- Zwischensummen festlegen.
- Automatische Sortierung einstellen.
- Autoshow einstellen.

####  **Festlegen des Zeilen-/Spalten-/Seitenfeldformats**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Festlegen des Datenfeldformats**

Das folgende Codebeispiel zeigt, wie Anzeigeformate und Zahlenformate für Datenfelder festgelegt werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Pivotfelder löschen**

 Der[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) hat eine Methode namens[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)Damit können Sie Pivotfelder löschen. Verwenden Sie es, wenn Sie alle Pivot-Felder in den Bereichen löschen möchten, zum Beispiel Seite, Spalte, Zeile oder Daten.
Das folgende Codebeispiel zeigt, wie alle Pivotfelder in einem Datenbereich gelöscht werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
