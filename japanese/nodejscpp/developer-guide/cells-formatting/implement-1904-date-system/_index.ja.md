---
title: Node.js経由のC++を使用して1904日付システムを実装
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのNode.jsライブラリです。1904日付システムの実装をサポートし、ユーザーが1904年1月1日の日付システムに基づいて計算およびフォーマットを行えるようにします。この記事では、Aspose.Cellsライブラリを使用した1904日付システムの実装方法を説明します。
keywords: Aspose.Cells、1904日付システム、スプレッドシート、計算、フォーマット、Node.js経由のC++
type: docs
weight: 7000
url: /ja/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excelは2つの日時システムをサポートしています：1900日付システム（Windows用Excelで標準実装されている日付システム）と1904日付システムです。1904日付システムはMacintosh Excelファイルとの互換性を保つために使用されることが多く、Mac用Excelを使用している場合のデフォルトシステムです。Aspose.Cells for Node.js via C++を使用してExcelファイルに対して1904日付システムを設定できます。 

{{% /alert %}} 

Microsoft Excelで1904日付システムを実装する方法（例：Microsoft Excel 2003）：

1. **ツール**メニューから**オプション**を選択し、**計算**タブを選択します。
1. **1904年日付システム**オプションを選択します。
1. **OK** をクリックします。

|**Microsoft Excelで1904年日付システムを選択**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Aspose.CellsのAPIを使用してこの機能を実現するサンプルコードを以下に示します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
