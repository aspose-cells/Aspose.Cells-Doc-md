---
title: Bereich von Zellen mit Node.js über C++ zusammenführen oder aufheben
linktitle: Bereich von Zellen zusammenführen oder trennen
type: docs
weight: 190
url: /de/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Zellen in einem Bereich in Excel mit Node.js über C++ zusammenführen und aufheben.
keywords: Node.js Zellen in einem Bereich zusammenführen und aufheben, Node.js Zellen in einem Bereich zusammenführen und aufheben, Zellen in Bereich mit Node.js zusammenführen und aufheben, Zellen in Bereich mit Node.js zusammenführen und aufheben, Zellen in Excel mit Node.js zusammenführen und aufheben, Zellen in Excel mit Node.js zusammenführen und aufheben, Node.js Zellen in Excel zusammenführen und aufheben, Zellen in Excel zusammenführen, Zellen in Excel aufheben, Zellen in Bereich mit Node.js zusammenführen
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um einen Bereich von Zellen zusammenzuführen oder aufzuteilen. Aspose.Cells bietet die Methoden [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) und [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) für diesen Zweck. Dieser Artikel erklärt, wie Sie einen Bereich von Zellen in eine einzige Zelle zusammenführen können.

{{% /alert %}}

## **Beispiel**

Der folgende Beispielcode erstellt zuerst einen Bereich - A1:D4 - und führt dann die Zellen im Bereich mit der [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)-Methode zusammen. Ebenso können Sie Zellen aufteilen, indem Sie einen Bereich erstellen und die [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--)-Methode aufrufen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
