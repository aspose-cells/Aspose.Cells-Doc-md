---
title: Formatieren der Pivot Tabelle
type: docs
weight: 10
url: /de/nodejs-cpp/formatting-pivot-table/
description: Wie man Pivot Tabellen mit Aspose.Cells for Node.js via C++ formatiert.
keywords: Pivot Tabelle formatieren
---

## **Aussehen der Pivot-Tabelle**

Wie man eine Pivot-Tabelle erstellt, erklärt, wie man eine einfache Pivot-Tabelle erstellt. Dieser Artikel beschreibt, wie man das Aussehen einer Pivot-Tabelle anpasst, indem man verschiedene Eigenschaften einstellt:

- Optionen zum Formatieren von Pivot-Tabellen
- Optionen zum Formatieren von Pivot-Feldern
- Optionen zum Formatieren von Datenfeldern

### **Wie man die Formatierungsoptionen für Pivot-Tabellen festlegt**

Die Klasse [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/) steuert die gesamte Pivot-Tabelle und kann auf verschiedene Arten formatiert werden.

#### **Wie man den AutoFormat-Typ festlegt**

Microsoft Excel bietet eine Reihe vordefinierter Berichtformate. Aspose.Cells for Node.js via C++ unterstützt diese Formatierungsoptionen ebenfalls. Um darauf zuzugreifen:

1. Setzen Sie [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) auf **true**.
1. Weisen Sie eine Formatierungsoption aus der [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/)-Aufzählung zu.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **Wie man Formatierungsoptionen festlegt**

Das unten stehende Codebeispiel zeigt, wie die Pivot-Tabelle formatiert wird, um Gesamtsummen für Zeilen und Spalten anzuzeigen, und wie die Feldreihenfolge des Berichts festgelegt wird. Es zeigt auch, wie eine benutzerdefinierte Zeichenfolge für Nullwerte festgelegt wird.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **Manuelles Anpassen von Aussehen und Anmutung**

Um das Erscheinungsbild des Pivot-Tabellenberichts manuell anzupassen, anstatt voreingestellte Berichtsformate zu verwenden, verwenden Sie die Methoden [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) und [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-). Erstellen Sie ein Style-Objekt für Ihre gewünschte Formatierung, zum Beispiel:

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **So setzen Sie Pivot-Feldformatoptionen**

Die Klasse [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/) stellt ein Feld in einer Pivot-Tabelle dar und kann auf verschiedene Arten formatiert werden. Das unten stehende Codebeispiel zeigt, wie:

- Auf Zeilenfelder zugreifen.
- Untergesamtsummen einstellen.
- Autosortierung einstellen.
- Autoshow einstellen.

#### **So setzen Sie Zeilen-/Spalten-/Seitenfeldformatoptionen**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **So setzen Sie Datenfeldformatoptionen**

Das unten stehende Codebeispiel zeigt, wie man Anzeigeformate und Zahlenformat für Datenfelder einstellt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **So löschen Sie Pivot-Felder**

Die Methode [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) der [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/)-Klasse ermöglicht es Ihnen, Pivot-Felder zu löschen. Verwenden Sie sie, wenn Sie alle Pivot-Felder in den Bereichen wie Seite, Spalte, Zeile oder Daten löschen möchten.
Das unten stehende Codebeispiel zeigt, wie man alle Pivot-Felder in einem Datenbereich löscht.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
