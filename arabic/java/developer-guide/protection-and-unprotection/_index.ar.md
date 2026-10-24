---
title: تشفير، فك التشفير، حماية وإزالة الحماية من ملفات Excel
linktitle: التشفير والحماية
description: يقدم هذا القسم كيفية تشفير ملفات Excel وفك تشفيرها وحماية بيانات Excel، ويغطي تشفير الملفات، والحماية للقراءة فقط، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيعات الرقمية باستخدام كود Java
keywords: Aspose.Cells, Java, تشفير, فك تشفير, كلمة مرور, حماية, إلغاء حماية, حماية المصنف, حماية ورقة العمل, قراءة فقط, توقيع رقمي
type: docs
weight: 68
url: /ar/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

غالبًا ما تخزن مصنفات Excel معلومات مالية أو تجارية أو شخصية حساسة يجب حمايتها من الوصول غير المصرح به. يوفر Aspose.Cells for Java مجموعة شاملة من ميزات الحماية التي تعكس إمكانيات Microsoft Excel، مما يتيح لك تأمين بياناتك على مستوى الملف، ومستوى المصنف، ومستوى ورقة العمل.

{{% alert color="primary" %}}
يوفر Aspose.Cells for Java مجموعة واسعة من ميزات الحماية، من مستوى الملف إلى مستوى البيانات، على غرار MS Excel. تشمل هذه الإمكانيات تشفير الملفات بكلمة مرور، وفرض الوصول للقراءة فقط من خلال كلمة مرور للتعديل، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيع الرقمي على المصنفات.
{{% /alert %}}

## تشفير ملفات Excel وفك تشفيرها
تمنع كلمة المرور المعيّنة على ملف Excel المستخدمين غير المصرح لهم من فتح محتوى المصنف أو عرضه. لتشفير مصنف، عيّن سلسلة كلمة مرور إلى `Workbook.Settings.Password` (التي يتم الوصول إليها عبر `workbook.getSettings().setPassword(...)`) ثم احفظ المصنف. يكتب Aspose.Cells الملف بشكل مشفر. لفتح مصنف مشفر لفك التشفير، أنشئ كائنًا من `LoadOptions`، وعيّن `LoadOptions.Password` (عبر `loadOptions.setPassword(...)`) إلى نفس كلمة المرور المستخدمة أثناء التشفير، ومررها إلى منشئ `Workbook`. يطبق Aspose.Cells كلمة المرور المقدمة بشفافية بحيث يمكن لبقية الكود الخاص بك التعامل مع المحتوى الذي تم فك تشفيره كما لو كان الملف مصنفًا عاديًا.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## الحماية للقراءة فقط (كلمة مرور للتعديل)
يدعم Excel طبقتين متميزتين من كلمات المرور. الأولى هي كلمة مرور الفتح، التي تشفر الملف نفسه ومغطاة في القسم السابق. والثانية هي كلمة مرور التعديل، التي لا تمنع المستخدمين من فتح المصنف؛ وبدلاً من ذلك، يوصي Excel بفتح الملف في وضع القراءة فقط ما لم يتم توفير كلمة مرور التعديل. يمكنك تكوين هذا السلوك في Aspose.Cells من خلال `Workbook.Settings.WriteProtection` (التي يتم الوصول إليها عبر `workbook.getSettings().getWriteProtection()`). عيّن خاصية `Password` الخاصة بها (عبر `writeProtection.setPassword(...)`) إلى كلمة مرور التعديل، وخاصية `Author` (عبر `writeProtection.setAuthor(...)`) لتحديد من قام بتطبيق الحماية. استخدم طريقة `WriteProtection.validatePassword(String)` للتحقق مما إذا كانت كلمة مرور التعديل المقدمة صحيحة، حيث تُرجع `true` عند المطابقة و`false` خلاف ذلك.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## حماية بنية المصنف وإلغاء حمايتها
تمنع حماية بنية المصنف المستخدمين الآخرين من عرض أوراق العمل المخفية، أو إضافة أوراق عمل جديدة، أو نقل أوراق العمل، أو حذف أوراق العمل، أو إخفاء أوراق العمل، أو إعادة تسمية أوراق العمل. تنطبق الحالة المحمية على بنية الأوراق بدلاً من محتويات الخلايا داخل أي ورقة. لتطبيق حماية البنية، استدعِ `workbook.protect(ProtectionType.STRUCTURE, "password")`. لإلغاء الحماية، استدعِ `workbook.unprotect("password")` وقدم كلمة المرور الصحيحة. تُستخدم قيمة التعداد `ProtectionType.STRUCTURE` هنا وهي مميزة عن أنواع الحماية الأخرى مثل `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// إنشاء مصنف جديد
Workbook workbook = new Workbook();
// إضافة ورقة عمل ثانية
workbook.getWorksheets().add();
// كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// حماية بنية المصنف
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// حفظ المصنف باسم structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// إعادة تحميل الملف في نسخة Workbook جديدة
Workbook loadedWorkbook = new Workbook(filePath);
// إلغاء حماية البنية
loadedWorkbook.unprotect("StructPwd");
// طباعة رسالة التأكيد
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## حماية أوراق العمل وإلغاء حمايتها
تقفل حماية ورقة العمل خلايا ورقة العمل ضد التغييرات العرضية أو المتعمدة. لا يمكن للمستخدمين تحرير الخلايا المقفلة دون تقديم كلمة المرور. هذه هي الحماية النموذجية المستخدمة لحماية الصيغ أو العناوين أو مناطق إدخال البيانات المحددة في جداول البيانات المشتركة. لحماية ورقة عمل، استدعِ `worksheet.protect(ProtectionType.ALL, "password")`. يتيح استخدام `ProtectionType.ALL` جميع خيارات الحماية المتاحة مثل تحديد الخلايا المقفلة، وتنسيق الخلايا، وإدراج الصفوف والأعمدة، وحذف الصفوف والأعمدة. لإلغاء الحماية، استدعِ `worksheet.unprotect("password")` بكلمة المرور الصحيحة. يتوفر تحكم أكثر دقة من خلال دمج أنواع حماية أخرى مثل `CONTENTS` و`OBJECTS` و`SCENARIOS` باستخدام عامل التشغيل OR على مستوى البت.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## إضافة التوقيعات الرقمية والتحقق منها
يضمن التوقيع الرقمي للمستلمين أن محتوى المصنف أصيل ولم يتم تغييره منذ توقيعه. يوفر Aspose.Cells دعم التوقيع الرقمي من خلال الحزمة `com.aspose.cells.DigitalSignatures`. يقوم سير العمل النموذجي بتحميل ملف شهادة `.pfx` من خلال واجهات برمجة التطبيقات الأمنية في Java (مثل `java.security.KeyStore` و`java.security.cert.X509Certificate`)، ويلفه في `com.aspose.cells.DigitalSignatures.DigitalSignature`، ويضيف التوقيع إلى `DigitalSignatureCollection`، ويطبق المجموعة على المصنف من خلال `workbook.addDigitalSignature(DigitalSignatureCollection)`. يمكن لخاصية `DigitalSignature.getComments()` تسجيل سياق التوقيع مثل وقت التوقيع والغرض منه. يُبطل أي تعديل يتم إجراؤه على المصنف بعد التوقيع، لذا يمكن لخطوة التحقق من جهة الاستقبال اكتشاف التلاعب.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## مقالات ذات صلة
- [تشفير ملفات Excel وفك تشفيرها](/cells/ar/java/encrypt-and-decrypt-excel-files/)
- [حماية بنية المصنف وإلغاء حمايتها](/cells/ar/java/protect-and-unprotect-workbook-structure/)
- [حماية ورقة العمل وإلغاء حمايتها](/cells/ar/java/protect-and-unprotect-worksheet/)
- [حماية المصنف المشترك بكلمة مرور أو إلغاء حمايته](/cells/ar/java/password-protect-or-unprotect-the-shared-workbook/)
- [تعيين التوقيعات الرقمية والتحقق منها](/cells/ar/java/assign-and-validate-digital-signatures/)
- [اكتشاف تنسيق الملف لملفات Office Open XML المشفرة - OOXML](/cells/ar/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا](/cells/ar/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}