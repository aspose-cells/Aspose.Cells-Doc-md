---
title: 通过Node.js使用C++自定义Ribbon XML
linktitle: 自定义Excel菜单
type: docs
weight: 1500
url: /zh/nodejs-cpp/customizing-the-ribbon-xml/
description: 学习如何使用Aspose.Cells for Node.js via C++自定义Excel中的Ribbon XML。 
---

{{% alert color="primary" %}} 

自2007年以来，Microsoft Office通过在应用程序窗口顶部使用Ribbon替换了菜单和工具栏。Ribbon可定制。 
Aspose.Cells for Node.js via C++允许你

- 保留Ribbon XML而无需解析它，
- 读取和写入Ribbon XML而无需解析它，
- 获取和设置Ribbon XML数据。

如果要更改Ribbon XML，则必须使用XML解析器或其他Ribbon XML工具解析它。

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
