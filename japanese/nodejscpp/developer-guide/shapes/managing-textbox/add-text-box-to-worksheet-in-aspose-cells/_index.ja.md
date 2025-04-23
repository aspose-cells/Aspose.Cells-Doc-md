---
title: Node.jsを使用してC++経由でワークシートにテキストボックスを追加/挿入する方法
linktitle: ワークシートにテキストボックスを追加
type: docs
weight: 10
url: /ja/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Aspose.Cells for Node.js via C++でワークシートにテキストボックスを追加/挿入する方法
keywords: C++を使用したExcel Aspose Node.jsでのテキストボックスの追加/挿入
---

Excel でワークシートにテキストボックスを追加

Excelプログラム（バージョン07以降）では、テキストボックスを挿入できる場所が2つあります。一つは『挿入-図形』、もう一つは『挿入』のトップメニューの右側です。

### 方法1:

![1](1.png)

### 方法2:

![2](2.png)

作成方法

水平または垂直のテキストボックスを作成できます。

- 対応するオプション（横向きまたは縦向き）を選択してください
- ページ上で左クリックします。
- 左ボタンを押したまま、ページ上で距離をドラッグします。
- 左ボタンを離します。

これでテキストボックスができます。

## Aspose.Cells for Node.js via C++でワークシートにテキストボックスを追加

ワークシートに一括でテキストボックスを挿入する必要がある場合、手動での挿入方法は明らかに失敗です。これに不満がある場合、このドキュメントが役立つでしょう。 [Aspose.Cells](https://products.aspose.com/cells/)は、あなたのコードで簡単に一括挿入を行うAPIを提供します。

次のサンプルコードはテキストボックスを作成します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

結果ファイル（result.xlsx）と類似したファイルを取得します。その中に次のものが見られます：

![](52449.png)

