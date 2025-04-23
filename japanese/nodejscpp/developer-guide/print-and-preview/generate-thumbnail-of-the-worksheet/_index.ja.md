---
title: Node.jsを通じてワークシートのサムネイル画像を生成する
linktitle: ワークシートのサムネイルを生成
type: docs
weight: 110
url: /ja/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Aspose.Cells for Node.js via C++を使用してワークシートからサムネイル画像を生成する方法を学びます。ドキュメントやプレゼンテーションでプレビュー用の小さな画像を作成します。
---

{{% alert color="primary" %}} 

ワークシートからサムネイルを作成することは便利です。サムネイルは、ワークシートのプレビューを提供するためにWordドキュメントやPowerPointプレゼンテーションに貼り付けることができる小さなイメージです。それは、オリジナルのドキュメントをダウンロードするためのリンクを含むウェブページに追加することができ、その他の用途もたくさんあります。

{{% /alert %}} 

Aspose.Cells for Node.js via C++はワークシートを画像ファイルに出力できるため、サムネイルの作成も容易です。以下のサンプルコードは、ワークシートを画像ファイルに出力する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
