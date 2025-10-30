---
title: Node.jsを使用してC++経由で範囲内のデータを検索・置換
linktitle: 範囲内のデータを検索および置換する
type: docs
weight: 170
url: /ja/nodejs-cpp/search-and-replace-data-in-a-range/
description: このこの記事では、Node.jsを使用してC++コード経由でExcelの範囲内のデータを検索・置換する方法を示します。
keywords: Node.jsを使ったExcel内のデータ検索と置換、Node.jsでExcel内のデータ検索、Node.jsによる範囲内のデータ検索と置換、範囲内のデータ検索、Node.jsによる範囲内のデータ検索、Node.jsで範囲内のデータ検索、Node.jsによるExcel内のデータ検索、Node.jsで範囲内のデータ検索、Node.jsを使ったExcel内のデータの検索と置換、範囲内のデータ検索と置換をNode.jsで実行、Node.jsを使った範囲内のデータ検索と置換
---

{{% alert color="primary" %}}

場合によっては、範囲の外にあるセルの値を無視して特定のデータを検索・置換する必要があります。Aspose.Cells for Node.js via C++は、検索を特定の範囲に限定することを可能にします。この記事ではその方法を解説します。

{{% /alert %}}

Aspose.Cells for Node.js via C++は、検索時に範囲を指定するための [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) メソッドを提供します。以下のコード例は、範囲内のデータを検索して置換します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

const area = AsposeCells.CellArea.createCellArea("E9", "H15");

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);

workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
