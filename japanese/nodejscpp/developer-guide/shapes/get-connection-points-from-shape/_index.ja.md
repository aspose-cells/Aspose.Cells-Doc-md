---  
title: Node.js 経由でシェイプの接続ポイントを取得  
linktitle: シェイプから接続ポイントを取得  
type: docs  
weight: 3500  
url: /ja/nodejs-cpp/get-connection-points-from-shape/  
description: Excelのシェイプから接続ポイントを取得する方法をAspose.Cells for Node.js via C++を使用して学びます。  
---  

Aspose.Cellsはスプレッドシート内のシェイプを管理する豊富な機能を提供します。時には、シェイプを整列させたり適切な場所に配置したりするために、シェイプの接続ポイントを取得する必要があります。そのために、すべての接続ポイントが必要です。以下のコードは、[Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--)プロパティを使用してシェイプの接続ポイントのリストを取得する例です。

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const worksheet = newWorkbook.getWorksheets().get(0);

// Add a new textbox to the collection.
const textboxIndex = worksheet.getTextBoxes().add(2, 1, 160, 200);

// Access your text box which is also a shape object from shapes collection
const shape = newWorkbook.getWorksheets().get(0).getShapes().get(0);

// Get all the connection points in this shape
const connectionPoints = shape.getConnectionPoints();

// Display all the shape points
connectionPoints.forEach(pt => {
console.log(`X = ${pt[0]}, Y = ${pt[1]}`);
```  

