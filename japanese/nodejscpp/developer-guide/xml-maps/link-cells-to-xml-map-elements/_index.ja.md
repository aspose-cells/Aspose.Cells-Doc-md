---
title: セルをXMLマップ要素にリンクする（Node.jsとC++）
linktitle: セルをXML Map要素にリンク
type: docs
weight: 50
url: /ja/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **可能な使用シナリオ**

セルをXMLマップ要素にリンクできます。これにはAspose.Cells for Node.js via C++を使用してください。

## **セルをXMLマップ要素にリンクする**

次のサンプルコードは、XML Mapを含む[source excel file](5115471.xlsx)を読み込み、セルA1、B2、C3、D4、E5、F6をそれぞれXML Map要素FIELD1、FIELD2、FIELD4、FIELD5、FIELD7、FIELD8にリンクし、[output excel file](5115467.xlsx)としてブックを保存します。

[output excel file](5115467.xlsx)を開いて、開発者 > ソース ボタンをクリックすると、セルがXMLマップの要素にリンクされ、Microsoft Excelによって強調表示されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
