---
title: Node.jsとC++を使用してワークブックの読み込み時に定義名フィルタを適用
linktitle: ワークブックを読み込む際に定義名をフィルタリングする
type: docs
weight: 50
url: /ja/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsは、ワークブック内の定義名をフィルタまたは削除することを可能にします。読み込み時に定義名をロードするには[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/)を使用し、削除するには[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/)を使用してください。ただし、定義名を削除すると、ワークブック内の数式が壊れる可能性があります。

## **ワークブックを読み込む際に定義名をフィルタリングする**

以下のサンプルコードは、定義名を含むセル（=SUM(MyName1, MyName2)）があるセルC1に数式を含むサンプルExcelファイル（61767860.xlsx）を読み込みます。読み込み時に[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/)を使用して定義名を削除しているため、出力Excelファイル（61767861.xlsx）のセルC1の数式は壊れ、「#NAME?」と表示されます。以下のスクリーンショットは、サンプルExcelファイルに対するコードの効果を示しています。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
