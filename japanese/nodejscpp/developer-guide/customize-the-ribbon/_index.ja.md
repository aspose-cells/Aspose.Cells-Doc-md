---
title: Node.jsとC++を使用したリボンXMLのカスタマイズ
linktitle: Excelメニューのカスタマイズ
type: docs
weight: 1500
url: /ja/nodejs-cpp/customizing-the-ribbon-xml/
description: ExcelのリボンXMLをカスタマイズする方法をAspose.Cells for Node.js via C++で学びます。 
---

{{% alert color="primary" %}} 

Microsoft Officeは、2007年以降、アプリケーションウィンドウの上部にリボンを置き換え、メニューやツールバーを置き換えました。リボンはカスタマイズ可能です。 
Aspose.Cells for Node.js via C++を使えば、

- リボンXMLを解析せずに保持できます。
- リボンXMLを解析せずに読み書きできます。
- リボンXMLデータの取得と設定ができます。

リボンXMLを変更する場合は、XMLパーサーまたは他のリボンXMLツールで解析する必要があります。

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
