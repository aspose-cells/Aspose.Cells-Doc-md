---
title: Add Signature line to the worksheet with Node.js via C++
linktitle: Add Signature line to the worksheet
type: docs
weight: 200
url: /nodejs-cpp/add-signature-line/
description: This article describes how to add a signature line to the worksheet using Node.js code with Aspose.Cells for Node.js via C++.
keywords: Add Signature line to the worksheet Node.js via C++, How to Add Signature line to the worksheet Node.js via C++, How to add the signature line to the worksheet Node.js via C++.
---

## **Introduction**

Aspose.Cells provides the [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) property to add the signature line of the worksheet.

## **How to Add Signature Line to Worksheet**

The following sample code demonstrates how to make use of [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) property to add the signature line of the worksheet. The screenshot shows the effect of the sample code on the sample Excel file after execution.

![todo:image_alt_text](add-signature-line.png)

## **Sample Code**

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

const certificatePath = path.join(dataDir, "rsa2048.pfx");
const certificate = new AsposeCells.Pkcs.X509Certificate2(certificatePath, "123456");
const signature = new AsposeCells.DigitalSignature(certificate, "test Microsoft Office signature line", new Date());
signature.setId(signatureLine.getId());
signature.setProviderId(signatureLine.getProviderId());

const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);
wb.setDigitalSignature(dsCollection);
wb.save(path.join(dataDir, "signatureLine.xlsx"));
```
