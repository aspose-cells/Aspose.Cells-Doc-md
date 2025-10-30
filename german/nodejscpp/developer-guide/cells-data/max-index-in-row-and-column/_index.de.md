---
title: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte erhalten
type: docs
weight: 600
url: /de/nodejs-cpp/get-max-index-in-row-and-column/
description: Lernen Sie, wie man den Maximalen Spaltenindex in einer Zeile und den Maximalen Zeilenindex in einer Spalte über die API Aspose.Cells for Node.js via C++ erhält.
keywords: Den Maximalen Spaltenindex in einer Zeile in Node.js via C++, den Maximalen Zeilenindex in einer Spalte in Node.js via C++, den Maximalen Daten Spaltenindex in einer Zeile in Node.js via C++, den Maximalen Daten Zeilenindex in einer Spalte in Node.js via C++.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einige Daten in den Zeilen oder Spalten manipulieren müssen, müssen Sie den Datenbereich der Zeilen und Spalten kennen. Aspose.Cells for Node.js via C++ bietet diese Funktion. Um den maximalen Spaltenindex in einer Zeile zu erhalten, können Sie die [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) und [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--) Methoden verwenden und dann die [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) Methode, um den maximalen Spaltenindex und den maximalen Daten-Spaltenindex zu erhalten. Um den maximalen Zeilenindex und den maximalen Zeilen-Datenindex in einer Spalte zu erhalten, müssen Sie einen Bereich in der Spalte erstellen, diesen Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich die [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) Methode auf die Zelle aufrufen.

Aspose.Cells for Node.js via C++ stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Maximalen Spaltenindex in einer Zeile und Maximalen Zeilenindex in einer Spalte ermitteln**
Dieses Beispiel zeigt, wie Sie:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Die Zeile abrufen, für die der maximale Spaltenindex und der maximale Daten-Spaltenindex benötigt werden.
1. Rufen Sie die [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) Methode auf der Zelle auf.
1. Basierend auf der Spalte einen Bereich erstellen.
1. Iterator abrufen und den Bereich durchlaufen.
1. Rufen Sie die [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) Methode auf der Zelle auf.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
