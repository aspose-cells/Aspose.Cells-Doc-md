---
title: Ein oder Löschen von Zeilen in einem Excel Arbeitsblatt
type: docs
weight: 20
url: /de/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: Dieser Artikel bietet den Python Code zum Einfügen und Löschen von Zeilen im Excel Arbeitsblatt mit der Aspose.Cells for Python via .NET Bibliothek.
keywords: Python Excel Library, Python Zeilen in Excel Arbeitsblatt einfügen oder löschen, Python Zeilen in Excel einfügen oder löschen, Python Zeilen in Excel einfügen, Python Zeilen in Excel löschen, Zeilen in Excel Arbeitsblatt mit Python einfügen oder löschen, Zeilen in Excel mit Python einfügen oder löschen, Zeilen in Excel mit Python einfügen, Zeilen in Excel mit Python löschen
---

{{% alert color="primary" %}}

Beim Erstellen eines neuen Arbeitsblatts oder bei der Arbeit mit einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um Daten zu berücksichtigen. In anderen Fällen könnte es erforderlich sein, Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt zu löschen.

{{% /alert %}}

Aspose.Cells für Python via .NET bietet zwei Methoden zum Einfügen und Löschen von Zeilen: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) und [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Diese Methoden sind für eine optimale Leistung optimiert und erledigen die Aufgabe sehr schnell.

Um eine bestimmte Anzahl von Zeilen einzufügen oder zu entfernen, empfehlen wir, stets die Methoden [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) und [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) anstelle der Verwendung der Methoden [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) oder [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) in einer Schleife zu verwenden.

Aspose.Cells für Python via .NET arbeitet auf die gleiche Weise wie Microsoft Excel. Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt des Arbeitsblatts nach unten und nach rechts verschoben. Beim Entfernen von Zeilen oder Spalten wird der Arbeitsblattinhalt nach oben oder nach links verschoben. Referenzen in anderen Arbeitsblättern und Zellen werden aktualisiert, wenn Zeilen hinzugefügt oder entfernt werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
