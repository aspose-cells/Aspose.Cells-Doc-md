---
title: Gruppierung, Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 30
url: /de/cpp/grouping-ungrouping-rows-and-columns/
---

## **Einführung**
In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliedersymbole** 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt liefern. Oder Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen.
## **Gruppenverwaltung von Zeilen und Spalten**
Aspose.Cells stellt eine Klasse, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) zur Verfügung, die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet eine [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung, die alle Zellen im Arbeitsblatt darstellt.

Die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt an, einige davon werden unten genauer besprochen.
### **Gruppierung von Zeilen & Spalten**
Es ist möglich, Zeilen oder Spalten zu gruppieren, indem Sie die [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) und [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) Methoden der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung aufrufen. Beide Methoden akzeptieren die folgenden Parameter:

- Der erste Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Der letzte Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Gruppeneinstellungen**
Microsoft Excel ermöglicht es Ihnen, Gruppeneinstellungen für die Anzeige zu konfigurieren:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts neben dem Detail.
## **Zeilen & Spalten aufheben**
Um gruppierte Zeilen oder Spalten aufzuheben, rufen Sie die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung mit den Methoden [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) und [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) auf. Beide Methoden akzeptieren zwei Parameter:

- Der erste Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Der letzte Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
