---
title: Kontrollera om VBA projektet i en arbetsbok är signerat med Node.js via C++
linktitle: Kontrollera om VBA projektet i en arbetsbok är signerat
type: docs
weight: 70
url: /sv/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Lär dig hur man kontrollerar om ett VBA projekt i en arbetsbok är signerat med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Du kan kontrollera om ditt VBA-projekt är signerat eller inte med Microsoft Excel via kommandot **Verktyg > Digitala signaturer...**. På liknande sätt kan du kontrollera det programmatiskt med hjälp av egenskapen [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) i Aspose.Cells.

{{% /alert %}}

## **Kontrollera om VBA-projektet i en arbetsbok är signerat i Node.js**

Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med hjälp av [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)-egenskapen. Egenskapen returnerar **true** om projektet är signerat, annars returnerar den **false**.

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
