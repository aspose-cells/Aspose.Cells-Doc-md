---
title: Node.jsとC++を使用して、ワークブック内にリンクされたXMLデータをエクスポート
linktitle: ワークブックにリンクされたXML Map内のXMLデータをエクスポート
type: docs
weight: 20
url: /ja/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: ワークブック内のXMLマップにリンクされたXMLデータをエクスポートする方法をAspose.Cells for Node.js via C++を使用して学びます。 
---

## **ブック内のXMLマップにリンクされたXMLデータをエクスポート**

ワークブック内のXMLマップにリンクされたXMLデータをエクスポートするには、[**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-)メソッドを使用してください。以下のサンプルコードは、ワークブックからすべてのXMLマップのXMLデータを一つずつエクスポートします。このコードで使用される[サンプルExcelファイル](5115497.xlsx)と[最初のXMLマップのエクスポート済みXMLデータ](5472487.xml)を確認してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
