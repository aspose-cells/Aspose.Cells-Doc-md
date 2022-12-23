---
title: Pivot-Tabelle formatieren
type: docs
weight: 10
url: /de/net/formatting-pivot-table/
---
## **Aussehen der Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle erklärt, wie Sie eine einfache Pivot-Tabelle erstellen. Dieser Artikel beschreibt, wie Sie das Erscheinungsbild einer Pivot-Tabelle anpassen, indem Sie verschiedene Eigenschaften festlegen:

- Formatoptionen für Pivot-Tabellen
- Formatoptionen für Pivot-Felder
- Formatoptionen für Datenfelder

### **Formatoptionen für Pivot-Tabellen festlegen**

 Das[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Klasse steuert die gesamte Pivot-Tabelle und kann auf verschiedene Weise formatiert werden.

#### **Festlegen des AutoFormat-Typs**

Microsoft Excel bietet eine Reihe verschiedener voreingestellter Berichtsformate. Aspose.Cells unterstützen diese Formatierungsoptionen ebenfalls. Um darauf zuzugreifen:

1.  Satz[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) zu**wahr**.
1.  Weisen Sie eine Formatierungsoption aus der zu[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)Aufzählung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Formatoptionen einstellen**

Das folgende Codebeispiel zeigt, wie die Pivot-Tabelle formatiert wird, um Gesamtsummen für Zeilen und Spalten anzuzeigen, und wie die Feldreihenfolge des Berichts festgelegt wird. Außerdem wird gezeigt, wie eine Kundenzeichenfolge für Nullwerte festgelegt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Aussehen und Verhalten manuell formatieren**

 Um das Aussehen des Pivot-Tabellenberichts manuell zu formatieren, anstatt vordefinierte Berichtsformate zu verwenden, verwenden Sie die[**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) und[**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)Methoden. Erstellen Sie ein Stilobjekt für Ihre gewünschte Formatierung, zum Beispiel:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Formatoptionen für Pivot-Felder festlegen**

 Das[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)Die Klasse stellt ein Feld in einer Pivot-Tabelle dar und kann auf verschiedene Weise formatiert werden. Das folgende Codebeispiel zeigt, wie Sie:

- Greifen Sie auf Zeilenfelder zu.
- Zwischensummen einstellen.
- Automatische Sortierung einstellen.
- Autoshow einstellen.

#### **Festlegen des Zeilen-/Spalten-/Seitenfeldformats**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Format der Datenfelder einstellen**

Das folgende Codebeispiel zeigt, wie Sie Anzeigeformate und das Zahlenformat für Datenfelder festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Pivot-Felder löschen**

 Das[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) hat eine Methode namens[**Klar()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)Damit können Sie Pivot-Felder löschen. Verwenden Sie es, wenn Sie alle Pivot-Felder in den Bereichen löschen möchten, z. B. Seite, Spalte, Zeile oder Daten.
Das folgende Codebeispiel zeigt, wie alle Pivot-Felder in einem Datenbereich gelöscht werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
