---  
title: Node.jsとC++を使用した範囲のカット＆ペースト  
linktitle: 範囲の切り取りと貼り付け  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/cut-and-paste-cells/  
description: Aspose.Cells for Node.js via C++を利用して、シート内のセルをカットして貼り付ける方法を学びます。  
---  

## **セルの切り取りと貼り付け**  

Aspose.Cells for Node.js via C++は、[**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-)コレクションの[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/)メソッドを使ってシート内のセルをカット＆ペーストする機能を提供します。[**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-)は以下のパラメータを受け付けます。  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): 切り取るセルの範囲  
- 行インデックス: セルを挿入する行のインデックス  
- 列インデックス: セルを挿入する列のインデックス  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): 列のシフト方向  

次の例は、ワークシート内でセルを切り取り、貼り付ける方法を示しています。  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 2).setValue(1);
worksheet.getCells().get(1, 2).setValue(2);
worksheet.getCells().get(2, 2).setValue(3);
worksheet.getCells().get(2, 3).setValue(4);
worksheet.getCells().createRange(0, 2, 3, 1).setName("NamedRange");

const cut = worksheet.getCells().createRange("C:C");
worksheet.getCells().insertCutCells(cut, 0, 1, AsposeCells.ShiftType.Right);
workbook.save(path.join(outDir, "CutAndPasteCells.xlsx"));
```  

