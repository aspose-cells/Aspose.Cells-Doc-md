---
title: Anpassa bandraden XML med Node.js via C++
linktitle: Anpassa Excel meny
type: docs
weight: 1500
url: /sv/nodejs-cpp/customizing-the-ribbon-xml/
description: Lär dig att anpassa bandraden XML i Excel med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office ersatte menyer och verktygsfält med en Ribbon längst upp i programfönstret sedan office 2007. Ribbon är anpassningsbar. 
Aspose.Cells for Node.js via C++ tillåter dig att

- Behåll Ribbon XML utan att analysera det,
- Läs och skriv Ribbon XML utan att analysera det,
- Hämta och ange Ribbon XML-data.

Om du vill ändra Ribbon XML måste du analysera den med en XML-parser eller annat Ribbon XML-verktyg.

{{% /alert %}} 

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
workbook.setRibbonXml(ribbonXml);
```
