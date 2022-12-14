---
title: Einfügen oder Löschen von Zeilen in einem Excel-Arbeitsblatt
type: docs
weight: 20
url: /de/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Dieser Artikel enthält den Code C# zum Einfügen und Löschen von Zeilen in einem Excel-Arbeitsblatt
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

Wenn Sie ein neues Arbeitsblatt erstellen oder mit einem vorhandenen Arbeitsblatt arbeiten, müssen Sie möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um Daten aufzunehmen. Zu anderen Zeiten müssen Sie möglicherweise Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt löschen.

{{% /alert %}}

 Aspose.Cells bietet zwei Methoden zum Einfügen und Löschen von Zeilen:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) und[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Diese Methoden sind auf Leistung optimiert und erledigen die Arbeit sehr schnell.

 Um mehrere Zeilen einzufügen oder zu entfernen, empfehlen wir, immer die zu verwenden[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) und[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) Methoden, anstatt die zu verwenden[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) oder[**Zeile löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)Methoden in einer Schleife.

Aspose.Cells funktioniert genauso wie Microsoft Excel. Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt des Arbeitsblatts nach unten und nach rechts verschoben. Wenn Zeilen oder Spalten entfernt werden, wird der Inhalt des Arbeitsblatts nach oben oder nach links verschoben. Alle Verweise in anderen Arbeitsblättern und Zellen werden aktualisiert, wenn Zeilen hinzugefügt oder entfernt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
