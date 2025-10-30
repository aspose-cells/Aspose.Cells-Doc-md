---
title: Worksheet mit Node.js via C++ auf Passwortschutz prüfen
linktitle: Erkennen, ob Arbeitsblatt passwortgeschützt ist
type: docs
weight: 360
url: /de/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Lernen Sie, wie Sie erkennen, ob ein Arbeitsblatt mit Aspose.Cells for Node.js via C++ passwortgeschützt ist. 
keywords: Arbeitsblatt Passwortschutz erkennen Node.js via C++, Arbeitsblatt auf Passwortschutz prüfen Node.js via C++, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

Es ist möglich, Arbeitsmappen und Arbeitsblätter separat zu schützen. Ein Spreadsheet kann ein oder mehrere passwortgeschützte Arbeitsblätter enthalten, die gesamte Mappe selbst kann jedoch geschützt oder ungeschützt sein. Die APIs von Aspose.Cells bieten die Möglichkeit zu erkennen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. Dieser Artikel zeigt die Verwendung der API Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells for Node.js via C++ hat die [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)-Eigenschaft bereitgestellt, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist. Die boolesche [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)-Eigenschaft gibt **true** zurück, wenn [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) passwortgeschützt ist, und **false**, wenn nicht.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
