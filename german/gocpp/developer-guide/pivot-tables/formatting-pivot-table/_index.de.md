---
title: Pivot Tabelle formatieren mit Golang via C++
linktitle: Formatieren der Pivot Tabelle
type: docs
weight: 10
url: /de/go-cpp/formatting-pivot-table/
description: Lernen Sie, wie Sie das Erscheinungsbild von Pivot Tabellen mit Aspose.Cells for C++ anpassen.
---

## **Aussehen der Pivot-Tabelle**

Wie man eine Pivot-Tabelle erstellt, erklärt, wie man eine einfache Pivot-Tabelle erstellt. Dieser Artikel beschreibt, wie man das Aussehen einer Pivot-Tabelle anpasst, indem man verschiedene Eigenschaften einstellt:

- Optionen zum Formatieren von Pivot-Tabellen
- Optionen zum Formatieren von Pivot-Feldern
- Optionen zum Formatieren von Datenfeldern

### **Einstellen der Pivot-Tabellenformatoptionen**

Die Klasse [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) steuert die gesamte Pivot-Tabelle und kann auf verschiedene Arten formatiert werden.

#### **Einstellen des AutoFormat-Typs**

Microsoft Excel bietet eine Reihe vordefinierter Berichtformate. Aspose.Cells unterstützt diese Formatierungsoptionen ebenfalls. Um darauf zuzugreifen:

1. Setzen Sie [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) auf **true**.
1. Weisen Sie eine Formatierungsoption aus der [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/)-Aufzählung zu.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Einstellen von Formatoptionen**

Das unten stehende Codebeispiel zeigt, wie man die Pivot-Tabelle formatiert, um Summen für Zeilen und Spalten anzuzeigen, und die Reihenfolge der Felder im Bericht festlegt. Außerdem zeigt es, wie man einen benutzerdefinierten String für Nullwerte setzt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Manuelles Anpassen von Aussehen und Anmutung**

Um zu steuern, wie der Pivot-Tabellenbericht manuell aussieht, anstatt vordefinierte Berichtformate zu verwenden, nutzen Sie die Methoden [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) und [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Erstellen Sie ein Style-Objekt für Ihr gewünschtes Format, beispielsweise:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Einstellen von Formatoptionen für Pivot-Felder**

Die Klasse [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) stellt ein Feld in einer Pivot-Tabelle dar und kann auf verschiedene Arten formatiert werden. Das unten stehende Codebeispiel zeigt, wie:

- Auf Zeilenfelder zugreifen.
- Untergesamtsummen einstellen.
- Autosortierung einstellen.
- Autoshow einstellen.

#### **Formatieren von Zeilen/Spalten/Seitenfeldern**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Formatierungsoptionen für Datenfelder einstellen**

Das unten stehende Codebeispiel zeigt, wie man Anzeigeformate und Zahlenformat für Datenfelder einstellt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Löschen von Pivot-Feldern**

Die Methode [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) der [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/)-Klasse ermöglicht es Ihnen, Pivot-Felder zu löschen. Verwenden Sie sie, wenn Sie alle Pivot-Felder in den Bereichen wie Seite, Spalte, Zeile oder Daten löschen möchten.
Das unten stehende Codebeispiel zeigt, wie man alle Pivot-Felder in einem Datenbereich löscht.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
