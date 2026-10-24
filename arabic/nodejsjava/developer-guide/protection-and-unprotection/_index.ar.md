---
title: حماية وفك الحماية
linktitle: التشفير والحماية
description: يقدم هذا القسم كيفية تشفير وفك تشفير ملفات Excel وحماية بيانات Excel، ويغطي تشفير الملفات، والحماية للقراءة فقط، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيعات الرقمية باستخدام كود JavaScript
keywords: Aspose.Cells, Node.js via Java, تشفير, فك تشفير, كلمة مرور, حماية, إلغاء حماية, حماية المصنف, حماية ورقة العمل, قراءة فقط, توقيع رقمي, JavaScript
type: docs
weight: 68
url: /ar/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

غالبًا ما تخزن مصنفات Excel معلومات مالية أو تجارية أو شخصية حساسة يجب حمايتها من الوصول غير المصرح به. يوفر Aspose.Cells for Node.js via Java مجموعة شاملة من ميزات الحماية التي تعكس إمكانيات Microsoft Excel، مما يسمح لك بتأمين بياناتك على مستوى الملف، ومستوى المصنف، ومستوى ورقة العمل.

{{% alert color="primary" %}}
يوفر Aspose.Cells for Node.js via Java مجموعة واسعة من ميزات الحماية، من مستوى الملف إلى مستوى البيانات، على غرار MS Excel. تشمل هذه الإمكانيات تشفير الملفات بكلمة مرور، وفرض الوصول للقراءة فقط من خلال كلمة مرور للتعديل، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيع رقميًا على المصنفات.
{{% /alert %}}

## تشفير وفك تشفير ملفات Excel
تمنع كلمة المرور المعينة على ملف Excel المستخدمين غير المصرح لهم من فتح محتوى المصنف أو عرضه. لتشفير مصنف، عيّن سلسلة كلمة مرور في `workbook.getSettings().setPassword(...)` ثم احفظ المصنف. يكتب Aspose.Cells الملف بشكل مشفر. لفتح مصنف مشفر لغرض فك التشفير، أنشئ كائن `LoadOptions`، وعيّن `loadOptions.setPassword(...)` على نفس كلمة المرور المستخدمة أثناء التشفير، ومررها إلى مُنشئ `Workbook`. يطبق Aspose.Cells كلمة المرور المقدمة بشفافية حتى يتمكن باقي الكود من التعامل مع المحتوى الذي تم فك تشفيره كما لو كان الملف مصنفًا عاديًا.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## حماية القراءة فقط (كلمة مرور للتعديل)
يدعم Excel طبقتين متميزتين من كلمات المرور. الأولى هي كلمة مرور الفتح، التي تشفّر الملف نفسه والتي تم تناولها في القسم السابق. الثانية هي كلمة مرور التعديل، التي لا تمنع المستخدمين من فتح المصنف؛ وبدلاً من ذلك، يوصي Excel بفتح الملف في وضع القراءة فقط ما لم يتم توفير كلمة مرور التعديل. يمكنك تكوين هذا السلوك في Aspose.Cells من خلال `workbook.getSettings().getWriteProtection()`. عيّن خاصية `Password` على كلمة مرور التعديل، وخاصية `Author` لتحديد من قام بتطبيق الحماية. استخدم الطريقة `writeProtection.validatePassword(string)` للتحقق مما إذا كانت كلمة مرور التعديل المقدمة صحيحة، حيث تُرجع `true` عند المطابقة و`false` خلاف ذلك.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// تكوين حماية الكتابة: تعيين كلمة المرور للتعديل والمؤلف
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// حفظ المصنف بحيث تستمر حماية الكتابة
workbook.save("WriteProtectedWorkbook.xlsx");
// التحقق من صحة كلمة المرور للتعديل باستخدام كلمة المرور الصحيحة
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// التحقق من صحة كلمة المرور للتعديل باستخدام كلمة مرور غير صحيحة لإظهار الفرع الآخر
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## حماية بنية المصنف وإلغاء حمايتها
تمنع حماية بنية المصنف المستخدمين الآخرين من عرض أوراق العمل المخفية، أو إضافة أوراق عمل جديدة، أو نقل أوراق العمل، أو حذفها، أو إخفائها، أو إعادة تسميتها. تنطبق الحالة المحمية على بنية الورقة بدلاً من محتويات الخلايا داخل أي ورقة. لتطبيق حماية البنية، استدعِ `workbook.protect(ProtectionType.Structure, "password")`. لإلغاء الحماية، استدعِ `workbook.unprotect("password")` ووفر كلمة المرور الصحيحة. تُستخدم قيمة التعداد `ProtectionType.Structure` هنا وتختلف عن أنواع الحماية الأخرى مثل `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// إضافة ورقة عمل ثانية
workbook.getWorksheets().add();
// كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// حماية بنية المصنف
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// حفظ المصنف باسم structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// إعادة تحميل الملف في نسخة Workbook جديدة
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// إلغاء حماية البنية
loadedWorkbook.unprotect("StructPwd");
// طباعة رسالة التأكيد
console.log("Structure protection has been successfully removed from the workbook.");
```

## حماية أوراق العمل وإلغاء حمايتها
تحمي حماية ورقة العمل خلايا ورقة العمل من التغييرات العرضية أو المتعمدة. لا يمكن للمستخدمين تحرير الخلايا المقفلة دون توفير كلمة المرور. هذه هي الحماية النموذجية المستخدمة لحماية الصيغ أو الرؤوس أو مناطق إدخال البيانات المخصصة في جداول البيانات المشتركة. لحماية ورقة عمل، استدعِ `worksheet.protect(ProtectionType.All, "password")`. يتيح استخدام `ProtectionType.All` جميع خيارات الحماية المتاحة مثل تحديد الخلايا المقفلة، وتنسيق الخلايا، وإدراج الصفوف والأعمدة، وحذف الصفوف والأعمدة. لإلغاء الحماية، استدعِ `worksheet.unprotect("password")` بكلمة المرور الصحيحة. يتوفر تحكم أكثر دقة من خلال دمج أنواع الحماية الأخرى مثل `Contents` و`Objects` و`Scenarios` باستخدام OR على مستوى البت.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## إضافة والتحقق من صحة التوقيعات الرقمية
يضمن التوقيع الرقمي للمستلمين أن محتوى المصنف أصلي ولم يتم تغييره منذ توقيعه. يوفر Aspose.Cells دعم التوقيعات الرقمية من خلال فئات مثل `AsposeCells.DigitalSignature` و`AsposeCells.DigitalSignatureCollection`. يُنشئ سير العمل النموذجي `AsposeCells.DigitalSignature` مباشرةً من ملف شهادة `.pfx` مع كلمة المرور وتعليقات التوقيع الخاصة به، ثم يضيف التوقيع إلى `DigitalSignatureCollection` ويطبّق المجموعة على المصنف عبر `workbook.addDigitalSignature(DigitalSignatureCollection)`. يمكن لخاصية `DigitalSignature.Comments` تسجيل سياق التوقيع مثل وقت التوقيع والغرض منه. أي تعديل يتم إجراؤه على المصنف بعد التوقيع يبطل التوقيع، لذا يمكن لخطوة التحقق من الصحة على الجانب المتلقي اكتشاف التلاعب.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}