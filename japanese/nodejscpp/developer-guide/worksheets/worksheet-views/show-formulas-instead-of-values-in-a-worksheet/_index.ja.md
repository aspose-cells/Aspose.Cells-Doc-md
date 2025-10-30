---
title: Node.jsをC++経由で使用し、ワークシートで値の代わりに数式を表示する方法についての解説記事
linktitle: ワークシートで値の代わりに数式を表示する
type: docs
weight: 20
url: /ja/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: このサンプルコードは、C++を介してNode.js APIを使用し、Excelのワークシートやスプレッドシートで値の代わりに数式をプログラム的に表示する方法を示しています。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**数式の表示**オプションをリボンの**数式**タブから選択することで、計算結果ではなく数式を表示できます。数式を表示している場合、Excelはワークシートに数式を表示します。これと同じことを行うにはAspose.Cells for Node.js via C++の方法を使用します。

{{% /alert %}}

Aspose.Cellsは[**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--)プロパティを提供しています。これを**true**に設定すると、Microsoft Excelに数式を表示させることができます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
