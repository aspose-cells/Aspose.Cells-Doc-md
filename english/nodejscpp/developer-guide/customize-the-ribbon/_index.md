---
title: Customizing the Ribbon XML with Node.js via C++
linktitle: Customize Excel Menu
type: docs
weight: 1500
url: /nodejs-cpp/customizing-the-ribbon-xml/
description: Learn how to customize the Ribbon XML in Excel using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office replaced menus and toolbars with a Ribbon at the top of the application window since office 2007. The Ribbon is customizable. 
Aspose.Cells for Node.js via C++ allows you to

- Keep Ribbon XML without parsing it,
- Read and write Ribbon XML without parsing it,
- Get and set Ribbon XML data.

If you want to change the Ribbon XML, you have to parse it with an XML parser or other Ribbon XML tool.

{{% /alert %}} 

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonFilePath = path.join(dataDir, "CustomUI.xml");
const ribbonXml = fs.readFileSync(ribbonFilePath, "utf8");
workbook.setRibbonXml(ribbonXml);
```
