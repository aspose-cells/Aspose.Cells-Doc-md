---  
title: تشفير وفك تشفير ملفات إكسل مع Node.js عبر C++  
linktitle: تشفير وفك تشفير ملفات Excel  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: كيفية تشفير وفك تشفير ملفات إكسل باستخدام Node.js عبر C++. قفل وفتح ملفات إكسل.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) يتيح لك تشفير وحماية كلمة مرور جداول البيانات الخاصة بك. تستخدم خوارزميات المزود الخدمي الكريبتوجرافي، أو CSP، مجموعة من الخوارزميات الكريبتوجرافية ذات خصائص مختلفة. CSP الافتراضي هو 'Office 97/2000 Compatible' أو 'Weak Encryption (XOR)'. من المهم اختيار طول مفتاح التشفير المناسب. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يعتبر ذلك تشفير ضعيف. للحصول على تشفير قوي، يتطلب طول مفتاح أدنى لـ 128 بت. تحتوي نوافذ Microsoft على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'مزود تشفير قوي من Microsoft'. لإعطائك فكرة، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال مع أنظمة الخدمات المصرفية عبر الإنترنت الخاصة بهم.  

تسمح Aspose.Cells لك بتشفير وحماية ملفات Microsoft Excel بنوع التشفير الذي ترغب فيه.  
{{% /alert %}}  

## **استخدام Microsoft Excel**  

لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):  

1. من قائمة **الأدوات**، حدد **الخيارات**. ستظهر نافذة حوارية.  
2. اختر علامة التبويب **الأمان**.  
3. أدخل كلمة مرور وانقر على **مُتقدم**  
4. اختر نوع التشفير و confirms كلمة المرور.  

## **تشفير ملف إكسل باستخدام Aspose.Cells for Node.js via C++**  

يوضح المثال التالي كيفية تشفير وحماية كلمة المرور لملف إكسل باستخدام API الخاص بـ Aspose.Cells.  

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

### **تحديد خيار كلمة المرور للتعديل**  

المثال التالي يوضح كيفية ضبط خيار Microsoft Excel **كلمة المرور للتعديل** لملف موجود باستخدام واجهة برمجة التطبيقات Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **فك تشفير ملف إكسل باستخدام Aspose.Cells for Node.js via C++**  
من السهل جدًا فتح ملف إكسل محمي بكلمة مرور وفكه باستخدام API الخاص بـ Aspose.Cells كما هو موضح في الكود التالي:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **مواضيع متقدمة**  
- [تشفير وفك تشفير ملفات ODS](/cells/ar/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [ضبط نوع التشفير القوي](/cells/ar/nodejs-cpp/setting-strong-encryption-type/)  
- [تحديد المؤلف أثناء حماية كتاب العمل](/cells/ar/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [التحقق من كلمة مرور الملفات المشفرة](/cells/ar/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
