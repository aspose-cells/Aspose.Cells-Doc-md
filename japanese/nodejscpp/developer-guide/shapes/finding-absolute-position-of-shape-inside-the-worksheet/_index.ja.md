---
title: Node.jsを使用してC++経由でワークシート内のシェイプの絶対位置を見つける方法
linktitle: ワークシート内の形状の絶対位置を検索
type: docs
weight: 8000
url: /ja/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++を使用してワークシート内のシェイプの絶対位置を見つける方法を学びます。 
---

{{% alert color="primary" %}}

時には、ワークシート内のシェイプの絶対位置を知る必要があります。Aspose.Cells for Node.js via C++は、この目的のために[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--)および[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--)プロパティを提供します。これらのプロパティは、ワークシート内でのシェイプの絶対位置をピクセル単位で返します。

{{% /alert %}}

次のサンプルコードは、ワークシート内の最初の形状の絶対位置をピクセル単位で表示します。サンプルコードは、次のコンソール出力を表示します:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Displays the absolute position of the shape
console.log(`Absolute Position of this Shape is (${shape.getLeftToCorner()} , ${shape.getTopToCorner()})`);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
