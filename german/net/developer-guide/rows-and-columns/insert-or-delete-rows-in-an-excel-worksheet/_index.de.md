---
title: Ein oder Löschen von Zeilen in einem Excel Arbeitsblatt
type: docs
weight: 20
url: /de/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Dieser Artikel enthält den C# Code zum Einfügen und Löschen von Zeilen in einem Excel Arbeitsblatt.
keywords: C# Zeilen in Excel Arbeitsblatt einfügen oder löschen, C# Zeilen in Excel einfügen oder löschen, C# Zeilen in Excel einfügen, C# Zeilen in Excel löschen, Zeilen in Excel Arbeitsblatt mit C# einfügen oder löschen, Zeilen in Excel mit C# einfügen oder löschen, Zeilen in Excel mit C# einfügen, Zeilen in Excel mit C# löschen
---

{{% alert color="primary" %}}

Beim Erstellen eines neuen Arbeitsblatts oder bei der Arbeit mit einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um Daten zu berücksichtigen. In anderen Fällen könnte es erforderlich sein, Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt zu löschen.

{{% /alert %}}

Aspose.Cells bietet zwei Methoden zum Einfügen und Löschen von Zeilen: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) und [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Diese Methoden sind auf Leistung optimiert und erledigen die Aufgabe sehr schnell.

Um eine bestimmte Anzahl von Zeilen einzufügen oder zu entfernen, empfehlen wir, stets die Methoden [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) und [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) anstelle der Verwendung der Methoden [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) oder [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) in einer Schleife zu verwenden.

Aspose.Cells arbeitet genauso wie Microsoft Excel. Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt des Arbeitsblatts nach unten und nach rechts verschoben. Wenn Zeilen oder Spalten entfernt werden, wird der Inhalt des Arbeitsblatts nach oben oder nach links verschoben. Referenzen in anderen Arbeitsblättern und Zellen werden aktualisiert, wenn Zeilen hinzugefügt oder entfernt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
