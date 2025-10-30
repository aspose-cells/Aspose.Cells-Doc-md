---
title: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe mit Node.js via C++ signiert ist
linktitle: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe signiert ist
type: docs
weight: 70
url: /de/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Erfahren Sie, wie Sie überprüfen, ob ein VBA Projekt in einer Arbeitsmappe mit Aspose.Cells for Node.js via C++ signiert ist.
---

{{% alert color="primary" %}}

Sie können über Microsoft Excel mithilfe des Menübefehls **Extras > Digitale Signaturen...** prüfen, ob Ihr VBA-Projekt signiert ist oder nicht. Ebenso können Sie dies programmgesteuert mithilfe der Aspose.Cells-[**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)-Eigenschaft überprüfen.

{{% /alert %}}

## **Überprüfen, ob das VBA-Projekt in einer Arbeitsmappe in Node.js signiert ist**

Der folgende Code lädt die Arbeitsmappe und überprüft, ob ihr VBA-Projekt mit der [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)-Eigenschaft signiert ist. Die Eigenschaft gibt **true** zurück, wenn das Projekt signiert ist, andernfalls **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
