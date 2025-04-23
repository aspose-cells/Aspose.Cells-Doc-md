---
title: Node.jsを使用してC++経由でワークシートに署名行を追加
linktitle: ワークシートに署名行を追加
type: docs
weight: 200
url: /ja/nodejs-cpp/add-signature-line/
description: この記事は、Aspose.Cells for Node.js via C++を用いたNode.jsコードでワークシートに署名線を追加する方法について説明します。
keywords: Node.jsを用いてC++経由でワークシートに署名線を追加する方法、どのように署名線を追加するか、署名線をExcelファイルに追加する方法。
---

## **紹介**

Aspose.Cellsは、ワークシートの署名行を追加するための[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)プロパティを提供します。

## **ワークシートに署名行を追加する方法**

以下のサンプルコードは、[**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)プロパティを使用してワークシートの署名線を追加する方法を示しています。実行後のサンプルExcelファイルに対するコードの効果をスクリーンショットで確認できます。

![todo:image_alt_text](add-signature-line.png)

## **サンプルコード**

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
