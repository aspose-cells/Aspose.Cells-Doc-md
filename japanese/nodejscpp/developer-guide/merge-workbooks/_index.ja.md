---
title: Node.jsを使ったC++経由で複数のワークブックを1つのワークブックに結合
linktitle: ワークブック結合ツール
type: docs
weight: 66
url: /ja/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aspose.Cells for Node.js via C++を使って複数のワークブックを1つに結合する方法を学びます。 
---

{{% alert color="primary" %}}

時には、画像、チャート、データなどさまざまな内容が含まれるワークブックを1つに結合する必要があります。Aspose.Cells for Node.js via C++はこの機能をサポートしています。この記事では、コンソールアプリケーションを作成し、Aspose.Cellsを使って少ないコードでワークブックを結合する方法を紹介します。

{{% /alert %}}

## **画像とグラフを使用したワークブックの結合**

この例のコードは、Aspose.Cells for Node.js via C++を使って2つのワークブックを1つに結合します。ソースワークブックを読み込み、[**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-)メソッドを使って結合し、出力ワークブックを保存します。

### **ソースワークブック**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **出力ワークブック**

- [combined.xlsx](5473095.xlsx)

### **スクリーンショット**

以下は、ソースおよび出力ワークブックのスクリーンショットです。

{{% alert color="primary" %}}

ソースワークブックを好きなものを使用できます。これらの画像は、イメージ説明のためのものです。

{{% /alert %}}

**チャートワークブックの最初のワークシート - 積み重ね** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**チャートワークブックの2番目のワークシート - 折れ線** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**画像ワークブックの最初のワークシート - 画像** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**結合されたワークブックの3つのワークシート - 積み重ね、折れ線、画像** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **高度なトピック**
- [複数のワークシートを単一のワークシートに結合する](/cells/ja/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [ファイルの結合](/cells/ja/nodejs-cpp/merge-files/)

