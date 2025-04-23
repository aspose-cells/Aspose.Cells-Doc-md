---
title: Node.jsを使ってC++経由でファイルを読み込み自動的に行の高さを調整する。
linktitle: Excel ファイルを読み込む際に自動的に行の高さを調整する
type: docs
weight: 120
url: /ja/nodejs-cpp/autofit-row-height/
description: ファイルの読み込み時に高さがカスタマイズされていない行を収まるようにフィットさせる方法を学びます。Aspose.Cells for Node.js via C++を使用します。
keywords: Node.jsを使ってC++経由でファイルを読み込み、自動的に行の高さを調整します。 
---

## **可能な使用シナリオ**
行の高さはフォントに自動的に合わせて調整されますが、キャッシュされた行の高さがファイルの内容と一致しない場合、MS Excelはファイルの読み込み時に自動的に高さを調整します。一方、Aspose.Cells for Node.js via C++はパフォーマンス向上のため自動調整を行いません。ファイルを読み込む際に行高を自動的に合わせたい場合は、[setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-)パラメータを利用できます。

以下の画像データをご参照ください。キャッシュされた行の高さは11行目で15に設定されていますが、Excelはファイル読み込み時に自動的に行の高さを調整しています。
<br>
<img src="1.png" width=70% />

## **Aspose.Cells for Node.js via C++を使用した行の高さ調整。**
ファイルを直接読み込みPDFに保存すると、そのキャッシュされた行の高さが15のみであるため、データが完全には表示されません。
<br>
<img src="2.png" width=70% />
<br>
[setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-)をtrueに設定してファイルを読み込むと、Aspose.Cellsは行の高さを自動調整します。調整された行高は、テキストの表示要件を効果的に満たします。
<br>
<img src="3.png" width=70% />

## **Node.jsサンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
