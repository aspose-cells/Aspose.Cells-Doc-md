---
title: Implementieren Sie das 1904 Datensystem mit Node.js über C++
description: Aspose.Cells ist eine Node.js Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Es unterstützt die Implementierung des 1904 Datensystems, das es Benutzern ermöglicht, basierend auf dem Datum 1. Januar 1904 zu berechnen und zu formatieren. Dieser Artikel beschreibt, wie man das 1904 Datensystem mit der Aspose.Cells Bibliothek implementiert.
keywords: Aspose.Cells, 1904 Datensystem, Tabellenblatt, Berechnung, Formatierung, Node.js über C++
type: docs
weight: 7000
url: /de/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel unterstützt zwei Datensysteme: das 1900-Datensystem (Standard in Excel für Windows) und das 1904-Datensystem. Das 1904-Datensystem wird normalerweise verwendet, um die Kompatibilität mit Macintosh Excel-Dateien zu gewährleisten und ist das Default-System, wenn Sie Excel für Macintosh verwenden. Sie können das 1904-Datensystem für Excel-Dateien mit Aspose.Cells for Node.js via C++ einstellen. 

{{% /alert %}} 

Um das 1904-Datensystem in Microsoft Excel zu implementieren (zum Beispiel in Microsoft Excel 2003):

1. Wählen Sie im **Extras**-Menü die Option **Optionen** und wählen Sie den Tab **Berechnung**.
1. Wählen Sie die Option **1904-Datensystem** aus.
1. Klicken Sie auf **OK**.

|**Auswählen des 1904-Datensystems in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Sehen Sie sich den folgenden Beispielcode an, wie Sie dies mit Aspose.Cells-APIs erreichen können.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
