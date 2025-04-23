---  
title: الدعم لتوقيع XAdES مع Node.js عبر C++  
linktitle: دعم توقيع XAdES  
type: docs  
weight: 110  
url: /ar/nodejs-cpp/support-for-xades-signature/  
description: يصف هذا المقال دعم توقيع XAdES باستخدام Node.js عبر C++ مع Aspose.Cells.  
keywords: الدعم لـ XAdES Signature Node.js عبر C++، كيفية توقيع إكسل مع توقيع XAdES Node.js عبر C++، كيفية إضافة توقيع XAdES Node.js عبر C++.  
---  

## **مقدمة**  

توفر Aspose.Cells دعمًا لتوقيع دفاتر العمل باستخدام توقيع XAdES. لهذا الغرض، توفر API فصل [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) و تعداد [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype).  

## **كيفية إضافة توقيع XAdES لإكسل**  

يوضح مقتطف الكود التالي استخدام فصل [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) لتوقيع دفتر العمل [المصدر](101089323.xlsx).  

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

