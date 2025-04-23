---
title: Node.js経由でC++を使用してWAVファイルをOle Objectとして挿入
linktitle: OLEオブジェクトとしてWAVファイルを挿入
type: docs
weight: 70
url: /ja/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/
description: ExcelワークシートにWAVファイルをOLEオブジェクトとして挿入する方法をAspose.Cells for Node.js via C++で学びます。 
---

{{% alert color="primary" %}} 

Aspose.Cellsは、ExcelワークシートにさまざまなタイプのOLEオブジェクトを追加する機能を提供します。次のコード例では、簡単なAPIを使用してWAVファイルをOLEオブジェクトとして追加する方法を示します。 

{{% /alert %}} 


```javascript
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "image2.jpg");

imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "chord.wav");
fs.writeFileSync(filePath, Buffer.from('RIFF____WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00data____', 'binary'));

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);
const intIndex = 0;

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

const sheet = workbook.getWorksheets().get(0);

// Add Ole Object
sheet.getOleObjects().add(14, 3, 200, 220, imageData);
workbook.getWorksheets().get(0).getOleObjects().get(intIndex).setFileFormatType(AsposeCells.FileFormatType.Unknown);
workbook.getWorksheets().get(0).getOleObjects().get(intIndex).setObjectData(objectData);
workbook.getWorksheets().get(0).getOleObjects().get(intIndex).setObjectSourceFullName(filePath);

// Save the excel file
workbook.save(path.join(dataDir, "testWAV.out.xlsx"));
```
