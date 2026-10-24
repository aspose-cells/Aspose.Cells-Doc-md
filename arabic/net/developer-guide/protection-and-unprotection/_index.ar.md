---
title: الحماية وإلغاء الحماية
linktitle: الحماية وإلغاء الحماية
description: يقدم هذا القسم كيفية تشفير ملفات Excel وفك تشفيرها وحماية بيانات Excel، ويغطي تشفير الملفات والحماية للقراءة فقط وحماية بنية المصنف وحماية أوراق العمل والتوقيعات الرقمية باستخدام كود C#
keywords: Aspose.Cells, .NET, تشفير, فك تشفير, كلمة مرور, حماية, إلغاء حماية, حماية المصنف, حماية ورقة العمل, قراءة فقط, توقيع رقمي, C#
type: docs
weight: 68
url: /ar/net/protect-and-unprotect/
alias: [/net/security-features/]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

غالبًا ما تخزن مصنفات Excel معلومات مالية أو تجارية أو شخصية حساسة يجب حمايتها من الوصول غير المصرح به. يوفر Aspose.Cells for .NET مجموعة شاملة من ميزات الحماية التي تعكس إمكانيات Microsoft Excel، مما يتيح لك تأمين بياناتك على مستوى الملف ومستوى المصنف ومستوى ورقة العمل.

{{% alert color="primary" %}}
يوفر Aspose.Cells for .NET نطاقًا واسعًا من ميزات الحماية، من مستوى الملف إلى مستوى البيانات، على غرار MS Excel. تتضمن هذه الإمكانيات تشفير الملفات بكلمة مرور، وفرض الوصول للقراءة فقط من خلال كلمة مرور للتعديل، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيع رقميًا على المصنفات.
{{% /alert %}}

## تشفير ملفات Excel وفك تشفيرها
تمنع كلمة المرور المعينة على ملف Excel المستخدمين غير المصرح لهم من فتح محتوى المصنف أو عرضه. لتشفير مصنف، عيّن سلسلة كلمة مرور إلى `Workbook.Settings.Password` ثم احفظ المصنف. يكتب Aspose.Cells الملف في شكل مشفر. لفتح مصنف مشفّر لفك التشفير، أنشئ كائنًا من `LoadOptions`، وعيّن `LoadOptions.Password` إلى نفس كلمة المرور المستخدمة أثناء التشفير، ومرّره إلى مُنشئ `Workbook`. يطبق Aspose.Cells كلمة المرور المقدمة بشفافية بحيث يمكن لبقية الكود لديك التعامل مع المحتوى الذي تم فك تشفيره كما لو أن الملف مصنف عادي.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## الحماية للقراءة فقط (كلمة مرور للتعديل)
يدعم Excel طبقتين متميزتين من كلمات المرور. الأولى هي كلمة مرور للفتح، التي تشفّر الملف نفسه وتمت تغطيتها في القسم السابق. والثانية هي كلمة مرور للتعديل، التي لا تمنع المستخدمين من فتح المصنف؛ وبدلاً من ذلك يوصي Excel بفتح الملف في وضع القراءة فقط ما لم تُقدَّم كلمة مرور التعديل. اضبط هذا السلوك في Aspose.Cells من خلال `Workbook.Settings.WriteProtection`. عيّن خاصية `Password` الخاصة به إلى كلمة مرور التعديل وخاصية `Author` الخاصة به لتحديد من طبّق الحماية. استخدم الطريقة `WriteProtection.ValidatePassword(string)` للتحقق مما إذا كانت كلمة مرور التعديل المقدّمة صحيحة، حيث تُرجع `true` عند التطابق و`false` خلاف ذلك.

```csharp
using System;
using Aspose.Cells;
// إنشاء مصنف جديد من البداية
Workbook workbook = new Workbook();
// كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// تكوين حماية الكتابة: تعيين كلمة المرور للتعديل والمؤلف
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// حفظ المصنف بحيث يتم الاحتفاظ بحماية الكتابة
workbook.Save("WriteProtectedWorkbook.xlsx");
// التحقق من صحة كلمة المرور للتعديل باستخدام كلمة المرور الصحيحة
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// التحقق من صحة كلمة المرور للتعديل باستخدام كلمة مرور غير صحيحة لتوضيح الفرع الآخر
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## حماية بنية المصنف وإلغاء حمايتها
تمنع حماية بنية المصنف المستخدمين الآخرين من عرض أوراق العمل المخفية، أو إضافة أوراق عمل جديدة، أو نقل أوراق العمل، أو حذف أوراق العمل، أو إخفاء أوراق العمل، أو إعادة تسمية أوراق العمل. تنطبق الحالة المحمية على بنية الأوراق بدلاً من محتويات الخلايا داخل أي ورقة. لتطبيق حماية البنية، استدعِ `workbook.Protect(ProtectionType.Structure, "password")`. لإزالة الحماية، استدعِ `workbook.Unprotect("password")` وقدم كلمة المرور الصحيحة. تُستخدم قيمة التعداد `ProtectionType.Structure` هنا وهي مميزة عن أنواع الحماية الأخرى مثل `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// إنشاء مصنف جديد
Workbook workbook = new Workbook();
// إضافة ورقة عمل ثانية
workbook.Worksheets.Add();
// كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// حماية بنية المصنف
workbook.Protect(ProtectionType.Structure, "StructPwd");
// حفظ المصنف باسم structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// إعادة تحميل الملف في مثيل Workbook جديد
Workbook loadedWorkbook = new Workbook(filePath);
// إزالة حماية البنية
loadedWorkbook.Unprotect("StructPwd");
// طباعة رسالة التأكيد
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## حماية أوراق العمل وإلغاء حمايتها
تقفل حماية ورقة العمل خلايا ورقة العمل ضد التغييرات العرضية أو المتعمدة. لا يمكن للمستخدمين تحرير الخلايا المقفلة دون تقديم كلمة المرور. هذه هي الحماية النموذجية المستخدمة لحماية الصيغ أو العناوين أو مناطق إدخال البيانات المعينة في جداول البيانات المشتركة. لحماية ورقة العمل، استدعِ `worksheet.Protect(ProtectionType.All, "password")`. يفعّل استخدام `ProtectionType.All` كل خيار حماية متاح مثل تحديد الخلايا المقفلة وتنسيق الخلايا وإدراج الصفوف والأعمدة وحذف الصفوف والأعمدة. لإزالة الحماية، استدعِ `worksheet.Unprotect("password")` بكلمة المرور الصحيحة. يتوفر تحكم أدق من خلال دمج أنواع حماية أخرى مثل `Contents` و`Objects` و`Scenarios` باستخدام العامل المنطقي OR على مستوى البت.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## إضافة التوقيعات الرقمية والتحقق منها
يضمن التوقيع الرقمي للمستلمين أن محتوى المصنف أصلي ولم يتم تغييره منذ توقيعه. يوفر Aspose.Cells دعم التوقيع الرقمي من خلال مساحة الأسماء `Aspose.Cells.DigitalSignatures`. يقوم سير العمل النموذجي بتحميل ملف شهادة `.pfx` من خلال `System.Security.Cryptography.X509Certificates.X509Certificate2`، ويلفّه في `Aspose.Cells.DigitalSignatures.DigitalSignature`، ويضيف التوقيع إلى `DigitalSignatureCollection`، ويطبق المجموعة على المصنف من خلال `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. يمكن لخاصية `DigitalSignature.Comments` تسجيل سياق التوقيع مثل وقت التوقيع والغرض منه. أي تعديل يتم على المصنف بعد التوقيع يبطل التوقيع، لذا يمكن لخطوة التحقق على جانب الاستقبال اكتشاف العبث.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## مقالات ذات صلة
- [تشفير ملفات Excel وفك تشفيرها](/cells/ar/net/encrypt-and-decrypt-excel-files/)
- [حماية بنية المصنف وإلغاء حمايتها](/cells/ar/net/protect-and-unprotect-workbook-structure/)
- [حماية ورقة العمل وإلغاء حمايتها](/cells/ar/net/protect-and-unprotect-worksheets/)
- [حماية المصنف المشترك بكلمة مرور أو إلغاء حمايته](/cells/ar/net/password-protect-or-unprotect-the-shared-workbook/)
- [تعيين التوقيعات الرقمية والتحقق منها](/cells/ar/net/assign-and-validate-digital-signatures/)
- [التحقق من كلمة مرور التعديل باستخدام Aspose.Cells](/cells/ar/net/check-password-to-modify-using-aspose-cells/)
- [الكشف عن تنسيق ملف ملفات Office Open XML المشفرة - OOXML](/cells/ar/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [تشفير ملفات Excel](/cells/ar/net/encrypting-excel-files/)
- [كيفية الكشف عن تنسيق ملف والتحقق مما إذا كان الملف مشفرًا](/cells/ar/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}