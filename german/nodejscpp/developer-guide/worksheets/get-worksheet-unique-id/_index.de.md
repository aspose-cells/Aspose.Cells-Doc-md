---
title: Erhalten Sie die eindeutige Arbeitsblatt ID mit Node.js über C++
linktitle: Arbeitsblatt eindeutige ID abrufen
type: docs
weight: 190
url: /de/nodejs-cpp/get-worksheet-unique-id/
description: Dieser Artikel zeigt, wie man die eindeutige Excel Arbeitsblatt ID programmatisch mit Node.js Bibliothek und C++ API erhält.
keywords: Eindeutige ID Excel Arbeitsblatt Node.js über C++, eindeutige ID Arbeitsblatt Node.js über C++
---

## **Arbeitsblatt eindeutige ID abrufen**

Aspose.Cells for Node.js via C++ ermöglicht die Ermittlung der eindeutigen ID eines Arbeitsblatts anhand der [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)-Eigenschaft. Das folgende Codebeispiel zeigt die Verwendung der [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)-Eigenschaft, um die eindeutige ID eines Arbeitsblatts auszugeben. Hierbei wird diese [Beispieldatei](105480213.xlsx) verwendet.

### Quellcode

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
