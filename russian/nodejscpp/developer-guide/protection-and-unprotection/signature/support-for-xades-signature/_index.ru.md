---  
title: Поддержка подписи XAdES с помощью Node.js через C++  
linktitle: Поддержка подписи XAdES  
type: docs  
weight: 110  
url: /ru/nodejs-cpp/support-for-xades-signature/  
description: Эта статья описывает поддержку подписи XAdES с помощью Node.js через C++ и Aspose.Cells.  
keywords: Поддержка XAdES Signature Node.js через C++, Как подписать Excel с помощью XAdES Signature Node.js через C++, Как добавить подпись XAdES Node.js через C++.  
---  

## **Введение**  

Aspose.Cells обеспечивает поддержку подписания рабочих книг с помощью XAdES Signature. Для этого API предоставляет класс [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) и перечисление [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype).  

## **Как добавить подпись XAdES для Excel**  

Следующий пример кода демонстрирует использование класса [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) для подписи рабочей книги [source](101089323.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sourceFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const password = "pfxPassword";

const pfx = path.join(sourceDir, "AsposeDemo.pfx");


const signature = new AsposeCells.DigitalSignature(pfx, "aspose", "testXAdES", new Date());
signature.setXAdESType(AsposeCells.XAdESType.XAdES);
const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);

workbook.setDigitalSignature(dsCollection);

workbook.save(outputDir + "XAdESSignatureSupport_out.xlsx");
```  

