---
title: Node.jsとC++を使用してワークシートのゼロ値の表示を非表示にする
linktitle: ワークシートでゼロ値を非表示にする
type: docs
weight: 50
url: /ja/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: この記事では、Node.jsライブラリをC++経由で使用してExcelスプレッドシートのゼロ値をプログラム的に非表示にするサンプルコードを示します。
keywords: C++を使用してNode.jsのExcelワークシートのゼロ値を非表示にする
---

{{% alert color="primary" %}} 

時折、スプレッドシートでゼロ値を非表示にする必要があります。これは個人の好みである場合もありますし、書式設定の基準である場合もあります。

{{% /alert %}} 

Microsoft Excel でワークシートでゼロ値を非表示にするには:

1. **ツール** メニューから **オプション** を選択し、次に **表示** タブを選択します。
1. **ゼロ値** オプションを選択解除します。
1. **OK** をクリックします。

以下のサンプルコードは、Aspose.Cells for Node.js via C++を使用してゼロを非表示にする方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
