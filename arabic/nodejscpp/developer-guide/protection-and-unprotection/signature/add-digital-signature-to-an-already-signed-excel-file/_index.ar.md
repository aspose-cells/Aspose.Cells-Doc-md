---
title: إضافة توقيع رقمي إلى ملف Excel موقع بالفعل باستخدام Node.js عبر C++
linktitle: إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل
type: docs
weight: 20
url: /ar/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: يصف هذا المقال كيفية إضافة توقيع رقمي إلى ملف Excel موقع بالفعل باستخدام Node.js مع Aspose.Cells for Node.js via C++.
keywords: إضافة توقيع رقمي إلى ملف Excel موقع مسبقًا، كيفية إضافة توقيع رقمي إلى مستند Excel موقع بالفعل باستخدام Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يقدم Aspose.Cells for Node.js via C++ أسلوب [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) الذي يمكنك استخدامه لإضافة توقيع رقمي إلى ملف Excel موقع سابقًا.

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إضافة توقيع رقمي إلى مستند Excel موقّع بالفعل، إذا كان المستند الأصلي مستندًا تم إنشاؤه بواسطة Aspose.Cells، فإنه يعمل بشكل جيد. لكن إذا تم إنشاؤه بواسطة محركات أخرى (مثل Microsoft Excel، إلخ)، فإن Aspose.Cells لا يمكنه الاحتفاظ بنفس الملف بعد التحميل وإعادة الحفظ، مما يجعل التوقيع الأصلي غير صالح.

{{% /alert %}}

## **كيفية إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا**

يعرض رمز النموذج التالي كيفية استخدام أسلوب [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) لإضافة توقيع رقمي إلى ملف Excel موقّع مسبقًا. يرجى التحقق من [ملف Excel النموذجي](50528280.xlsx) المستخدم في هذا الكود. هذا الملف موقع رقميًا مسبقًا. يرجى التحقق من [ملف Excel الناتج](50528281.xlsx) الذي تم إنشاؤه بواسطة الكود. لقد استخدمنا شهادة عرضية باسم [AsposeDemo.pfx](50528279.pfx) بكلمة مرور **aspose** في هذا الكود، وتظهر لقطة الشاشة تأثير رمز النموذج على ملف Excel النموذجي بعد التنفيذ.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
