---
title: Zellenindex erhalten
type: docs
weight: 600
url: /de/nodejs-cpp/get-cells-index/
description: Erfahren Sie, wie Sie Zeilen oder Spalten mithilfe des Namens von Zeile, Spalte oder Zellen erhalten. Konvertieren Sie den Namen der Zelle in den nullbasierten Zeilen und Spaltenindex.
keywords: Zeilen und Spaltenindex nach dem Namen der Zelle erhalten, Spaltenindex nach dem Namen der Spalte erhalten, Zeilenindex nach dem Namen der Zeile erhalten, Index nach dem Namen der Zelle erhalten. 
---

{{% alert color="primary" %}}
Die Standardansicht von Excel ist das A1-Stil-Bezugssystem. Jede Spalte ist als A, B, C...definiert und die Zellen sind als A1, B2, C3... usw. bezeichnet.
Sie möchten vielleicht wissen, welche Zeile und Spalte diese Zelle ist.

{{% /alert %}}


## **Mögliche Verwendungsszenarien**
Wenn Sie nur eine bestimmte Daten auf dem Arbeitsblatt mit Zeilen- und Spaltenindex manipulieren müssen, müssen Sie die Spalten- und Zeilenindizes dieser bestimmten Zelle kennen. 
Aspose.Cells for Node.js via C++ bietet diese Funktion, um Zeilen- und Spaltenindex anhand des Namens der Zeile, Spalte und Zelle zu erhalten. 
Aspose.Cells for Node.js via C++ stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Hinweis: Die Indizierung ist in Aspose.Cells for Node.js via C++ nullbasiert, aber die ID der Zeile ist einsbasiert in MS Excel.

## **Zellindizes mit Aspose.Cells for Node.js via C++ abrufen**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Finden Sie die spezifische Zelle im ersten Arbeitsblatt.
1. Holen Sie sich den Zeilenindex und Spaltenindex nach dem Namen der Zelle.
1. Holen Sie sich den Spaltenindex nach dem Namen der Spalte.
1. Holen Sie sich den Zeilenindex nach dem Namen der Zeile.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
