---
title: セルのテキストと条件付きアイコンセットをNode.js経由でC++で追加
linktitle: セルのテキストに条件付きアイコンセットを追加する
type: docs
weight: 160
url: /ja/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/
description: Aspose.Cells for Node.js via C++を使用して、条件付きアイコンをセルのテキスト横に追加する方法を学びます。アイコンを通じてデータの意味を強化します。
---

{{% alert color="primary" %}} 

時には、セルのテキスト横に条件付きアイコンを追加して、読者にとってデータをより意味深く見せたいことがあります。条件付き書式のアイコントリタイプの一部を使用したいものの、セルには適用したくない場合、この機能はAspose.Cells for Node.js via C++でサポートされています。

{{% /alert %}} 

次のコード例は、セルテキストに条件付きアイコンセットを追加する方法を示しています。



```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet (default worksheet) in the workbook
const worksheet = workbook.getWorksheets().get(0);
// Get the cells
const cells = worksheet.getCells();
// Set the columns widths (A, B and C)
worksheet.getCells().setColumnWidth(0, 24);
worksheet.getCells().setColumnWidth(1, 24);
worksheet.getCells().setColumnWidth(2, 24);

// Input date into the cells
cells.get("A1").putValue("KPIs");
cells.get("A2").putValue(19551794);
cells.get("A3").putValue(11.8070745566204);
cells.get("A4").putValue(11.858589818569);
cells.get("B1").putValue("UA Contract Size Group 4");
cells.get("B2").putValue(19551794);
cells.get("B3").putValue(11.8070745566204);
cells.get("B4").putValue(11.858589818569);
cells.get("C1").putValue("UA Contract Size Group 3");
cells.get("C2").putValue(8150131.66666667);
cells.get("C3").putValue(10.3168384396244);
cells.get("C4").putValue(11.3326931937091);

// Get the conditional icon's image data and add pictures
const iconTypes = [
{ type: AsposeCells.IconSetType.TrafficLights31, row: 1, column: 1 },
{ type: AsposeCells.IconSetType.Arrows3, row: 1, column: 2 },
{ type: AsposeCells.IconSetType.Symbols3, row: 2, column: 1 },
{ type: AsposeCells.IconSetType.Stars3, row: 2, column: 2 },
{ type: AsposeCells.IconSetType.Boxes5, row: 3, column: 1 },
{ type: AsposeCells.IconSetType.Flags3, row: 3, column: 2 }
];

iconTypes.forEach(icon => {
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(icon.type, icon.type === AsposeCells.IconSetType.Flags3 ? 1 : 0);
const stream = new Uint8Array(imagedata);
worksheet.getPictures().add(icon.row, icon.column, stream);
```
