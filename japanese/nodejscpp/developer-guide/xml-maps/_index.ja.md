---
title: Node.jsを使用してXMLをExcelワークブックにインポートする方法
linktitle: XMLマップ
type: docs
weight: 210
url: /ja/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: XMLファイルからのデータをExcelにインポートするにはAspose.Cells for Node.js via C++を使用します。
---

{{% alert color="primary" %}}

Aspose.Cellsは[**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-)メソッドを使用してワークブック内にXMLマップをインポートすることができます。Microsoft ExcelでXMLマップをインポートする手順は次のとおりです：

- **開発**タブを選択
- XMLセクションで**インポート**をクリックし、必要な手順に従います。

インポートを完了するためにXMLデータを提供する必要があります。テストに使用できる[サンプルXMLデータ](5115037.txt)を以下に示します。

{{% /alert %}}

## **Microsoft Excelを使用してXML Mapをインポート**

以下のスクリーンショットは、Microsoft Excelを使用してXML Mapをインポートする方法を示しています。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells for Node.js via C++を使用したXMLマップのインポート**

次のサンプルコードは、[**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-)の使用法を示しています。このスクリーンショットに示すように、[出力Excelファイル](5115036.xlsx)が生成されます。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **高度なトピック**
- [XmlMapCollection.add()メソッドを使用してワークブック内にXMLマップを追加する](/cells/ja/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [ブック内のXMLマップにリンクされたXMLデータをエクスポート](/cells/ja/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XMLマップのルート要素名を検出する](/cells/ja/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [セルをXMLマップ要素にリンクする](/cells/ja/nodejs-cpp/link-cells-to-xml-map-elements/)

