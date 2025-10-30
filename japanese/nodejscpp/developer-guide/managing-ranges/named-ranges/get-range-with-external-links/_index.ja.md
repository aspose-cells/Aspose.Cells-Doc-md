---
title: Node.js を使用して C++ 経由で外部リンク付き範囲を取得する
linktitle: 外部リンクを含む範囲を取得
type: docs
weight: 120
url: /ja/nodejs-cpp/get-range-with-external-links/
description: Aspose.Cells for Node.js via C++ を使用して外部リンク付き範囲を取得する方法を学びます。異なる Excel ファイルから効率的にデータを取得します。
---

## **外部リンク付きの範囲を取得する**

多くの場合、Excel ファイルは外部リンクを使用して他の Excel ファイルからデータにアクセスします。Aspose.Cells for Node.js via C++ は、 [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) メソッドを使用してこれらの外部リンクを取得するオプションを提供します。 [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) メソッドは [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) 型の配列を返します。 [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) クラスは、外部ファイルの名前を返す [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) プロパティを提供します。 [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) クラスは以下のメンバーを公開します。

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): 範囲の終了列
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): 範囲の終了行
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): これが外部参照の場合、外部ファイル名を取得します
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): これはエリアであるかどうかを示します
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): これは外部リンクであるかどうかを示します
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): この参照が含まれるシートを示します
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): エリアの開始列
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): エリアの開始行

以下に示すサンプルコードは、外部リンクを含む範囲を取得するための[**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-)メソッドの使用例です。

## **サンプルコード**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
