---
title: Formatieren der Pivot Tabelle
type: docs
weight: 10
url: /de/net/formatting-pivot-table/
---

## **Aussehen der Pivot-Tabelle**

Wie man eine Pivot-Tabelle erstellt, erklärt, wie man eine einfache Pivot-Tabelle erstellt. Dieser Artikel beschreibt, wie man das Aussehen einer Pivot-Tabelle anpasst, indem man verschiedene Eigenschaften einstellt:

- Optionen zum Formatieren von Pivot-Tabellen
- Optionen zum Formatieren von Pivot-Feldern
- Optionen zum Formatieren von Datenfeldern

### **Einstellen der Pivot-Tabellenformatoptionen**

Die Klasse [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) steuert die gesamte Pivot-Tabelle und kann auf verschiedene Arten formatiert werden.

#### **Einstellen des AutoFormat-Typs**

Microsoft Excel bietet eine Reihe verschiedener voreingestellter Berichtsformate. Aspose.Cells unterstützt auch diese Formatierungsoptionen. Um darauf zuzugreifen:

1. Setzen Sie [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) auf **true**.
1. Weisen Sie eine Formatierungsoption aus der [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)-Aufzählung zu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Einstellen von Formatoptionen**

Das unten stehende Codebeispiel zeigt, wie die Pivot-Tabelle formatiert wird, um Gesamtsummen für Zeilen und Spalten anzuzeigen, und wie die Feldreihenfolge des Berichts festgelegt wird. Es zeigt auch, wie eine benutzerdefinierte Zeichenfolge für Nullwerte festgelegt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Manuelles Anpassen von Aussehen und Anmutung**

Um das Aussehen des Pivot-Tabellenberichts manuell anzupassen, anstelle von voreingestellten Berichtsformaten, verwenden Sie die Methoden [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) und [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall). Erstellen Sie ein Style-Objekt für Ihre gewünschte Formatierung, zum Beispiel:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Einstellen von Formatoptionen für Pivot-Felder**

Die Klasse [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) stellt ein Feld in einer Pivot-Tabelle dar und kann auf verschiedene Arten formatiert werden. Das unten stehende Codebeispiel zeigt, wie:

- Auf Zeilenfelder zugreifen.
- Untergesamtsummen einstellen.
- Autosortierung einstellen.
- Autoshow einstellen.

#### **Formatieren von Zeilen/Spalten/Seitenfeldern**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Einstellen von Datenfeldformaten**

Das unten stehende Codebeispiel zeigt, wie man Anzeigeformate und Zahlenformat für Datenfelder einstellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Löschen von Pivot-Feldern**

Die Methode [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) der [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)-Klasse ermöglicht es Ihnen, Pivot-Felder zu löschen. Verwenden Sie sie, wenn Sie alle Pivot-Felder in den Bereichen wie Seite, Spalte, Zeile oder Daten löschen möchten.
Das unten stehende Codebeispiel zeigt, wie man alle Pivot-Felder in einem Datenbereich löscht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
