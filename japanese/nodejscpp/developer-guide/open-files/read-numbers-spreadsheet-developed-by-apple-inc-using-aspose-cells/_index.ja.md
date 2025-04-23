---
title: Apple Inc. によって作成された Numbers スプレッドシートを Aspose.Cells for Node.js via C++ を使用して読み取る
linktitle: Apple Inc. が開発したNumbersスプレッドシートの読み取り
type: docs
weight: 140
url: /ja/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Apple Inc.が開発したNumbersスプレッドシートをAspose.Cells for Node.js via C++を使用して読む方法を学びます。 
---

## **可能な使用シナリオ**

NumbersはApple Inc.が開発したスプレッドシートアプリケーションです。Aspose.CellsはNumbersスプレッドシートの読み取りが可能ですが、書き込みには対応していません。Data、Style、Formulasの読み取りが可能です。

## **Apple Inc. が開発した数値スプレッドシートを読む Aspose.Cells for Node.js via C++**

以下のサンプルコードは、[サンプルNumbersスプレッドシート](sampleNumbersByAppleInc.numbers)を読み込み、[出力PDF形式](outputNumbersByAppleInc.pdf)に変換します。正常に読み込むには、[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)クラスを使用し、そのコンストラクタに[**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat)をパラメータとして指定する必要があります。両方をダウンロードしてください。どんなNumbersスプレッドシートでもコードを試すことができます。また、コードのコメントも読んでください。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

