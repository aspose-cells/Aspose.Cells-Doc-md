---
title: Personalizzazione dell XML del ribbon con Node.js tramite C++
linktitle: Personalizzare il Menu di Excel
type: docs
weight: 1500
url: /it/nodejs-cpp/customizing-the-ribbon-xml/
description: Impara come personalizzare l XML del Ribbon in Excel usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office ha sostituito i menu e le barre degli strumenti con un Ribbon nella parte superiore della finestra dell'applicazione a partire dall'ufficio 2007. Il Ribbon è personalizzabile. 
Aspose.Cells for Node.js via C++ ti permette di

- Mantenere il Ribbon XML senza analizzarlo,
- Leggere e scrivere Ribbon XML senza analizzarlo,
- Ottenere e impostare i dati del Ribbon XML.

Se si desidera modificare il Ribbon XML, è necessario analizzarlo con un analizzatore XML o altro strumento Ribbon XML.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
