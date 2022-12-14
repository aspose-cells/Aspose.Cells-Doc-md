---
title: Zeilen und Spalten gruppieren, Gruppierung aufheben
type: docs
weight: 30
url: /de/cpp/grouping-ungrouping-rows-and-columns/
---
## **Einführung**
In einer Microsoft Excel-Datei können Sie eine Gliederung der Daten erstellen, um Detailebenen mit einem einzigen Mausklick ein- und auszublenden.

 Drücke den**Gliederungssymbole**, 1,2,3, + und -, um schnell nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt enthalten, oder Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen.
## **Gruppenverwaltung von Zeilen und Spalten**
 Aspose.Cells bietet eine Klasse,[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[IArbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse bietet eine[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt, einige davon werden im Folgenden ausführlicher besprochen.
### **Gruppieren von Zeilen und Spalten**
 Es ist möglich, Zeilen oder Spalten zu gruppieren, indem Sie die aufrufen[GroupRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) und[GruppierenSpalten](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) Methoden der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Sammlung. Beide Methoden nehmen die folgenden Parameter:

- Der erste Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Der letzte Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist ausgeblendet, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach der Gruppierung ausgeblendet werden sollen oder nicht.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Gruppeneinstellungen**
Microsoft Mit Excel können Sie Gruppeneinstellungen für die Anzeige konfigurieren:

- Zusammenfassungszeilen unter Detail.
- Zusammenfassungsspalten rechts vom Detail.
## **Gruppierung von Zeilen und Spalten aufheben**
 Um die Gruppierung gruppierter Zeilen oder Spalten aufzuheben, rufen Sie die auf[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung[Gruppierung aufheben](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) und[Gruppierung von Spalten aufheben](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)Methoden. Beide Methoden nehmen zwei Parameter:

- Der erste Zeilen- oder Spaltenindex, die erste Zeile/Spalte, deren Gruppierung aufgehoben werden soll.
- Der letzte Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, deren Gruppierung aufgehoben werden soll.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
