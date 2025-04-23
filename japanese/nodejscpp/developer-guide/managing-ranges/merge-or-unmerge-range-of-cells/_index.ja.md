---
title: Node.jsとC++を使ったセル範囲のマージまたは解除
linktitle: セル範囲の結合または解除
type: docs
weight: 190
url: /ja/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Node.jsとC++のコードを使って、Excelのセル範囲をマージまたは解除します。
keywords: Node.jsを使った範囲内のセルのマージと解除、Excelでセルのマージと解除、Node.jsを使った範囲のセルのマージと解除}
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してセルの範囲を結合または分割できます。 Aspose.Cellsはこの目的のための[**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)および[**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--)メソッドを提供します。この記事では、セルの範囲を単一のセルに結合する方法について説明します。

{{% /alert %}}

## **例**

以下のサンプルコードは、最初に範囲（A1:D4）を作成し、その範囲内のセルを[**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)メソッドを使って1つのセルにマージします。同様に、範囲を作成し、[**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--)メソッドを呼び出すことでセルを分割できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
