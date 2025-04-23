---
title: Node.jsを使用したC++経由でワークシートから画像を抽出する方法（ImageOrPrintOptions使用）
linktitle: ImageOrPrintOptionsを使用してワークシートからイメージを抽出する
type: docs
weight: 140
url: /ja/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Excelワークシートから画像を抽出し、Aspose.Cells for Node.js via C++を使って保存する方法を学びます。
---

{{% alert color="primary" %}} 

Microsoft Excelのユーザーはスプレッドシートに画像を追加できます。Aspose.Cells for Node.js via C++を使えば、Microsoft Excelファイルから画像を読み取り、ローカルドライブに保存できます。この記事でその方法を解説します。

{{% /alert %}} 

以下のサンプルコードは、Excelファイルから画像を抽出して保存する方法を示しています。



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
