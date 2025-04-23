---
title: Gruppierung, Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 30
url: /de/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Einführung**

In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliedersymbole** 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt liefern. Oder Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen.

## **Gruppenverwaltung von Zeilen und Spalten**

Aspose.Cells bietet die Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse stellt eine [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung bereit, die alle Zellen im Arbeitsblatt darstellt.

Die [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt, von denen einige im Folgenden näher erläutert werden.

### **Gruppierung von Zeilen & Spalten**

Es ist möglich, Zeilen oder Spalten zu gruppieren, indem die Methoden [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) und [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung aufgerufen werden. Beide Methoden akzeptieren die folgenden Parameter:

- Der erste Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Der letzte Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Gruppeneinstellungen**

Microsoft Excel ermöglicht es Ihnen, Gruppeneinstellungen für die Anzeige zu konfigurieren:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts neben dem Detail.

## **Zeilen & Spalten aufheben**

Um gruppierte Zeilen oder Spalten wieder aufzuheben, rufen Sie die Methoden [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) und [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung auf. Beide Methoden nehmen zwei Parameter entgegen:

- Der erste Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Der letzte Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
