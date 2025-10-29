---
title: تشفير ملفات إكسل باستخدام Node.js عبر C++
linktitle: تشفير ملفات Excel
type: docs
weight: 90
url: /ar/nodejs-cpp/encrypting-excel-files/
description: تعلم كيفية تشفير وحماية ملفات إكسل بكلمة مرور باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) يتيح لك تشفير وحماية كلمة مرور جداول البيانات الخاصة بك. تستخدم خوارزميات المزود الخدمي الكريبتوجرافي، أو CSP، مجموعة من الخوارزميات الكريبتوجرافية ذات خصائص مختلفة. CSP الافتراضي هو 'Office 97/2000 Compatible' أو 'Weak Encryption (XOR)'. من المهم اختيار طول مفتاح التشفير المناسب. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يعتبر ذلك تشفير ضعيف. للحصول على تشفير قوي، يتطلب طول مفتاح أدنى لـ 128 بت. تحتوي نوافذ Microsoft على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'مزود تشفير قوي من Microsoft'. لإعطائك فكرة، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال مع أنظمة الخدمات المصرفية عبر الإنترنت الخاصة بهم.

تسمح Aspose.Cells لك بتشفير وحماية ملفات Microsoft Excel بنوع التشفير الذي ترغب فيه.

{{% /alert %}}

## **استخدام Microsoft Excel**

لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**. ستظهر نافذة حوارية.
١. حدد علامة التبويب **الأمان**.
1. أدخل كلمة مرور وانقر **متقدم**
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **التشفير باستخدام Aspose.Cells for Node.js via C++**

المثال التالي يوضح كيفية تشفير وحماية ملف Excel بكلمة مرور باستخدام واجهة برمجة التطبيقات Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```

### **تحديد كلمة المرور لخيار تعديل**

المثال التالي يوضح كيفية ضبط خيار Microsoft Excel **كلمة المرور للتعديل** لملف موجود باستخدام واجهة برمجة التطبيقات Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```

## **تحقق من كلمة المرور للملف المُشفر**

لتحقق من كلمة مرور الملف المشفر، يوفر Aspose.Cells for Node.js via C++ طريقة [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). تقبل هذه الطرق معاملين، تيار الملف وكلمة المرور التي يجب التحقق منها.
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```

## **تشفير/فك تشفير ملف ODS بـ Aspose.Cells**

يسمح Aspose.Cells بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS المفكوك في كل من Excel وOpenOffice، ولكن لا يمكن فتح ملف ODS المشفر إلا بواسطة OpenOffice بعد إدخال كلمة المرور. لا يمكن لExcel فتح ملف ODS المشفر وقد يظهر رسالة تحذير. خيارات التشفير غير قابلة للتطبيق على ملفات ODS على عكس أنواع الملفات الأخرى. لتشفير ملف ODS، قم بتحميل الملف وضبط قيمة [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) على كلمة المرور الفعلية قبل حفظه. يمكن فتح ملف ODS المشفر الناتج فقط في OpenOffice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

لفك تشفير ملف ODS، قم بتحميل الملف عن طريق تقديم كلمة مرور في [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). بمجرد تحميل الملف، ضبط السلسلة [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) على القيمة الخالية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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
{{< app/cells/assistant language="nodejs-cpp" >}}
