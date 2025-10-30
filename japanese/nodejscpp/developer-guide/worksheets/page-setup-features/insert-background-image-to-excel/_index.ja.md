---
title: Node.jsとC++を使ったExcelへ背景画像の挿入方法。
linktitle: Excelに背景画像を挿入する
type: docs
weight: 90
url: /ja/nodejs-cpp/insert-background-image-to-excel/
description: 「Aspose.Cells for Node.js via C++を使用してExcelに背景画像を挿入する方法」
---

{{% alert color="primary" %}} 

特別な要素がシート上のデータを遮らずに背景のヒントを追加する特別な企業図形がある場合、これはワークシートをより魅力的にすることができます。Aspose.Cells APIを使用して、シートの背景画像を追加することができます。

{{% /alert %}} 

## **Microsoft Excelでのシートの背景の設定方法（例：Microsoft Excel 2019）：**

1. **ページレイアウト**メニューから**ページの設定**オプションを見つけ、**背景**オプションをクリックします。

1. **ページレイアウト**メニューから**ページ設定**オプションを見つけ、**背景**オプションをクリックします。
1. シートの背景画像を設定するために画像を選択します。

   シートの背景を設定する

![todo:image_alt_text](insert-background-to-excel.jpg)

## **シートの背景設定とAspose.Cells for Node.js via C++による設定**

以下のコードは、ストリームから画像を使用して背景画像を設定します。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## 関連記事

- [ODSファイルで背景を操作する](/cells/ja/nodejs-cpp/working-with-background-in-ods-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
