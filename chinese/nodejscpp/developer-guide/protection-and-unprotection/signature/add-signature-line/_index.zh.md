---
title: 使用Node.js通过C++在工作表中添加签名线
linktitle: 向工作表添加签名行
type: docs
weight: 200
url: /zh/nodejs-cpp/add-signature-line/
description: 这篇文章介绍了如何使用Aspose.Cells for Node.js via C++和Node.js在工作表中添加签名线。
keywords: 使用Node.js通过C++在工作表中添加签名线，如何在工作表中添加签名线，如何使用Node.js在工作表中添加签名线
---

## **介绍**

Aspose.Cells 提供了 [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) 属性来添加工作表的签名行。

## **如何向工作表添加签名行**

 以下示例代码演示了如何使用[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)属性为工作表添加签名线。截图显示了执行后示例代码对示例Excel文件的效果。

![todo:image_alt_text](add-signature-line.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiating a Workbook object
const wb = new AsposeCells.Workbook();

const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("Aspose.Cells");
signatureLine.setTitle("signed by Aspose.Cells");
wb.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

const certificatePath = path.join(dataDir, "AsposeDemo.pfx");
const signature = new AsposeCells.DigitalSignature(certificatePath, "aspose", "test Microsoft Office signature line", new Date());


const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);
wb.setDigitalSignature(dsCollection);
wb.save(path.join(dataDir, "signatureLine.xlsx"));
```
