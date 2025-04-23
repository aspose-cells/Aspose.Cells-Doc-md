---
title: تشفير وفك تشفير ملفات ODS باستخدام Node.js عبر C++
linktitle: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: حماية بكلمة مرور وتشفير ملفات ODS باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
يدعم OpenOffice.org مجموعة مكتملة من الميزات، ويتيح حماية بكلمة مرور وتشفير الملفات. ومع ذلك، يمكن فتح ملف ODS المشفر فقط بواسطة OpenOffice بعد إدخال كلمة المرور. لا يمكن لـ Excel فتح ملف ODS المشفر، وقد يعرض رسائل تحذيرية. خيارات التشفير غير قابلة للتطبيق على ملفات ODS، على عكس أنواع الملفات الأخرى. 
يسمح Aspose.Cells لك بتشفير وفك تشفير ملفات ODS. يمكن فتح ملفات ODS المفككة في كل من Excel وOpenOffice.
{{% /alert %}}

## **التشفير باستخدام OpenOffice Calc**
1. اختر **حفظ باسم** وانقر على مربع **الحفظ بكلمة مرور**.
1. انقر على زر **حفظ**.
1. اكتب كلمة المرور المطلوبة في حقلي **أدخل كلمة المرور للفتح** و **تأكيد كلمة المرور** في نافذة تعيين كلمة المرور التي تفتح. 
1. انقر على زر **موافق** لحفظ الملف.

## **تشفير ملف ODS باستخدام Aspose.Cells for Node.js via C++**
لتشفير ملف ODS، قم بتحميل الملف واضبط قيمة [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) على كلمة المرور الفعلية قبل الحفظ. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **فك تشفير ملف ODS باستخدام Aspose.Cells for Node.js via C++**
لفك تشفير ملف ODS، قم بتحميل الملف من خلال إدخال كلمة المرور في [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). بمجرد تحميل الملف، اضبط سلسلة [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) على null.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
