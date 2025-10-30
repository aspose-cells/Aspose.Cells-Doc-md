---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 50
url: /de/python-net/grouping-and-ungrouping-rows-and-columns/
description: In diesem Artikel wird gezeigt, wie man Zeilen und Spalten mit der Aspose.Cells für Python via .NET API gruppieren und die Gruppierung aufheben kann.
keywords: Python Excel Bibliothek, Python Wie man Zeilen und Spalten gruppieren, Python Wie man Zeilen und Spalten aufheben gruppieren, Python Gruppenverwaltung von Zeilen und Spalten, Python Wie man Zusammenfassungszeilen unterhalb von Details setzt, Python Wie man Zusammenfassungsspalten rechts von Details setzt.
---

## **Einführung**

In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliederungssymbole**, 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bereitstellen, oder verwenden Sie die Symbole, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt:

|**Gruppieren von Zeilen und Spalten.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gruppenverwaltung von Zeilen und Spalten**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält einen [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), der den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung, die alle Zellen in der Arbeitsmappe repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einer Arbeitsmappe, einige davon werden unten genauer erläutert.

### **Wie man Zeilen und Spalten gruppieren**

Es ist möglich, Zeilen oder Spalten zu gruppieren, indem man die [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool)- und [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool)-Methoden der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung aufruft. Beide Methoden nehmen folgende Parameter an:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **Gruppeneinstellungen**

Microsoft Excel ermöglicht es Ihnen, Gruppeneinstellungen für die Anzeige zu konfigurieren:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts neben dem Detail.

Entwickler können diese Gruppeneinstellungen mithilfe der [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/)-Eigenschaft der [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse konfigurieren.

### **Wie man Zusammenfassungszeilen unterhalb des Details einstellt**

Es ist möglich zu steuern, ob Zusammenfassungszeilen unterhalb des Details angezeigt werden, indem man die [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline)-Eigenschaft der [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/)-Klasse auf **true** oder **false** setzt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **Wie man Zusammenfassungsspalten rechts neben dem Detail einstellt**

Entwickler können auch steuern, ob Zusammenfassungsspalten rechts neben dem Detail angezeigt werden, indem sie die [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/)-Eigenschaft der [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline)-Klasse auf **true** oder **false** setzen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **Wie man Zeilen und Spalten aufhebt**

Um gruppierte Zeilen oder Spalten aufzuheben, rufen Sie die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlungsmethoden [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) und [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) auf. Beide Methoden nehmen zwei Parameter an:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) hat eine Überladung, die einen dritten booleschen Parameter akzeptiert. Wenn dieser auf **true** gesetzt wird, werden alle gruppierten Informationen entfernt. Andernfalls wird nur die äußere Gruppeninformation entfernt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
