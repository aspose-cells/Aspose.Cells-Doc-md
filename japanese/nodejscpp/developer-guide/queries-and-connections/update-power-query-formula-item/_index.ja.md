---
title: Power QueryのフォーマルアイテムをNode.js経由でC++を使って更新する方法
linktitle: Power Query Formulaアイテムの更新
type: docs
weight: 120
url: /ja/nodejs-cpp/update-power-query-formula-item/
description: Aspose.Cells for Node.js via C++を使用して、Excelファイル内のPower Queryフォーマルアイテムのデータソースを更新する方法を学びます。
---

## **使用シナリオ**

場合によっては、データソースファイルが移動し、Excelファイルがファイルの場所を見つけられないことがあります。その場合、Aspose.Cells APIは、[*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem)クラスを使ってソースファイルの場所を更新するオプションを提供します。

## **Power Query Formula Itemの更新**

Aspose.Cells APIはPower Queryの式アイテムを更新する機能を提供します。以下のコードスニペットは、[**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--)プロパティを使用してExcelファイル内のデータソースファイルの場所を更新する例を示しています。参考用にソースと出力のファイルを添付します。

- [元のファイル 1](106364953.xlsx)
- [元のファイル 2](106364954.xlsx)
- [出力ファイル](106364955.xlsx)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
