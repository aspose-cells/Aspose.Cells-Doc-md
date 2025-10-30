---
title: Anpassen des Ribbon XML mit Node.js via C++
linktitle: Excel Menü anpassen
type: docs
weight: 1500
url: /de/nodejs-cpp/customizing-the-ribbon-xml/
description: Erfahren Sie, wie Sie das Ribbon XML in Excel mit Aspose.Cells for Node.js via C++ anpassen. 
---

{{% alert color="primary" %}} 

 Microsoft Office hat seit Office 2007 Menüs und Symbolleisten durch ein Ribbon oben im Anwendungsfenster ersetzt. Das Ribbon ist anpassbar. 
Aspose.Cells for Node.js via C++ ermöglicht Ihnen

- Ribbon-XML ohne Analyse beizubehalten,
- Ribbon-XML ohne Analyse zu lesen und zu schreiben,
- Ribbon-XML-Daten zu erhalten und zu setzen.

Wenn Sie das Ribbon-XML ändern möchten, müssen Sie es mit einem XML-Parser oder einem anderen Ribbon-XML-Tool analysieren.

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
