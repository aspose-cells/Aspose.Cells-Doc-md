---
title: Node.jsとC++を使用してXMLマップのルート要素名を見つける方法
linktitle: XML Mapのルート要素名を検索する
type: docs
weight: 30
url: /ja/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: ExcelでXMLマップのルート要素名を見つける方法をAspose.Cells for Node.js via C++を用いて学びます。
---

## **可能な使用シナリオ**

*Xml Mapのルート要素名*はAspose.Cells for Node.js via C++を使用して[**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--)プロパティで見つけることができます。以下のスクリーンショットは、Microsoft Excel内のXMLマップのルート要素名を示しています。

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **サンプルコード**

以下のサンプルコードは[サンプルExcelファイル](55541789.xlsx)をロードし、最初のXMLマップにアクセスしてその[**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--)プロパティを出力します。結果のコンソール出力も合わせてご覧ください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **コンソール出力**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
