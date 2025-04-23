---
title: Добавить линию подписи в лист с помощью Node.js через C++
linktitle: Добавить строку подписи на листе
type: docs
weight: 200
url: /ru/nodejs-cpp/add-signature-line/
description: Этот раздел описывает, как добавлять линию подписи в лист с помощью Node.js и Aspose.Cells for Node.js via C++.
keywords: Добавить линию подписи в лист Node.js через C++, как добавить линию подписи в лист Node.js через C++, как добавить линию подписи в лист Node.js через C++.
---

## **Введение**

Aspose.Cells предоставляет свойство [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) для добавления строки подписи листа.

## **Как добавить строку подписи на рабочем листе**

Следующий пример кода демонстрирует, как использовать свойство [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) для добавления линии подписи в лист. На снимке экрана показан эффект работы кода на пример файла Excel.

![todo:image_alt_text](add-signature-line.png)

## **Образец кода**

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
