---
title: Gruppieren, Gruppieren von Zeilen und Spalten aufheben
type: docs
weight: 30
url: /de/cpp/grouping-ungrouping-rows-and-columns/
---
##  **Einführung**
In einer Excel-Datei Microsoft können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Detailebenen ein- und auszublenden.

Klicken Sie auf die *Umrisssymbole**, 1,2,3, + und -, um schnell nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bereitstellen, oder Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder anzuzeigen Überschrift.
##  **Gruppenverwaltung von Zeilen und Spalten**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet eine[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Die Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden ausführlicher erläutert.
###  **Gruppieren von Zeilen und Spalten**
 Es ist möglich, Zeilen oder Spalten zu gruppieren, indem Sie aufrufen[GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) Und[Gruppenspalten](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) Methoden der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung. Beide Methoden verwenden die folgenden Parameter:

- Der erste Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Der letzte Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist ausgeblendet, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach der Gruppierung ausgeblendet werden sollen oder nicht.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Gruppeneinstellungen**
Microsoft In Excel können Sie Gruppeneinstellungen für die Anzeige konfigurieren:

- Zusammenfassungszeilen unten im Detail.
- Zusammenfassungsspalten rechts neben den Details.
##  **Gruppierung von Zeilen und Spalten aufheben**
 Um die Gruppierung gruppierter Zeilen oder Spalten aufzuheben, rufen Sie auf[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung[Gruppierung von Zeilen aufheben](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) Und[Gruppierung von Spalten aufheben](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)Methoden. Beide Methoden benötigen zwei Parameter:

- Der erste Zeilen- oder Spaltenindex, die erste Zeile/Spalte, deren Gruppierung aufgehoben werden soll.
- Der letzte Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, deren Gruppierung aufgehoben werden soll.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
