---  
title: Node.jsを使ったC++経由での、ドイツ語ロケール対応の名前付き範囲式のサポート  
linktitle: 名前付き範囲式におけるドイツ語ロケールのサポート  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Aspose.Cells for Node.js via C++を使ったドイツ語ロケール対応の名前付き範囲式のサポート方法を学びましょう。  
---  

英語の数式は名前付き領域に書き込まれます。このExcelファイルは、システムがドイツ語ロケールに設定されている環境で開くことができ、英語の数式はドイツ語に翻訳されます。以下の例はこの機能を示しています。ただし、Excelがドイツ語でインストールされている必要があり、システムロケールもドイツ語に設定されている必要があります。  

この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");

const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNamedRangeTest.xlsm");
const outputFilePath = path.join(dataDir, "sampleOutputNamedRangeTest.xlsm");

const wb = new AsposeCells.Workbook();
wb.save(sourceFilePath);

const name = "HasFormula";
const value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))";

const wbSource = new AsposeCells.Workbook(sourceFilePath);
const wsCol = wbSource.getWorksheets();

const nameIndex = wsCol.getNames().add(name);
const namedRange = wsCol.getNames().get(nameIndex);
namedRange.setRefersTo(value);

wbSource.save(outputFilePath);
```  

