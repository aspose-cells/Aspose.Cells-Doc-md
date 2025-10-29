---
title: إضافة سطر توقيع إلى ورقة العمل باستخدام Node.js عبر C++
linktitle: إضافة خط التوقيع إلى ورقة العمل
type: docs
weight: 200
url: /ar/nodejs-cpp/add-signature-line/
description: يصف هذا المقال كيفية إضافة سطر توقيع إلى ورقة العمل باستخدام رمز Node.js مع Aspose.Cells for Node.js via C++.
keywords: إضافة سطر توقيع إلى ورقة العمل باستخدام Node.js عبر C++، كيفية إضافة سطر التوقيع إلى ورقة العمل باستخدام Node.js عبر C++، كيف تضيف سطر التوقيع إلى ورقة العمل باستخدام Node.js عبر C++.
---

## **مقدمة**

تقدم Aspose.Cells خاصية [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) لإضافة خط التوقيع في ورقة العمل.

## **كيفية إضافة خط توقيع إلى الورقة**

يعرض رمز النموذج التالي كيفية استخدام خاصية [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) لإضافة سطر توقيع لورقة العمل. تظهر لقطة الشاشة تأثير رمز النموذج على ملف Excel بعد التنفيذ.

![todo:image_alt_text](add-signature-line.png)

## **الكود المثالي**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
