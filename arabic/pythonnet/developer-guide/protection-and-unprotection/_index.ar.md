---
title: حماية وفك الحماية
linktitle: التشفير والحماية
description: يقدم هذا القسم كيفية تشفير ملفات Excel وفك تشفيرها وحماية بيانات Excel، ويغطي تشفير الملفات، والحماية للقراءة فقط، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيعات الرقمية باستخدام كود Python
keywords: Aspose.Cells, Python via .NET, تشفير, فك تشفير, كلمة مرور, حماية, إلغاء حماية, حماية المصنف, حماية ورقة العمل, قراءة فقط, توقيع رقمي, Python
type: docs
weight: 68
url: /ar/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

غالبًا ما تخزن مصنفات Excel معلومات مالية أو تجارية أو شخصية حساسة يجب حمايتها من الوصول غير المصرح به. يوفر Aspose.Cells for Python via .NET مجموعة شاملة من ميزات الحماية التي تعكس إمكانيات Microsoft Excel، مما يتيح لك تأمين بياناتك على مستوى الملف، ومستوى المصنف، ومستوى ورقة العمل.

{{% alert color="primary" %}}
يقدم Aspose.Cells for Python via .NET مجموعة واسعة من ميزات الحماية، بدءًا من مستوى الملف وحتى مستوى البيانات، على غرار MS Excel. تتضمن هذه الإمكانيات تشفير الملفات بكلمة مرور، وفرض الوصول للقراءة فقط من خلال كلمة مرور التعديل، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيع الرقمي على المصنفات.
{{% /alert %}}

## تشفير ملفات Excel وفك تشفيرها
تمنع كلمة المرور المعيّنة على ملف Excel المستخدمين غير المصرح لهم من فتح محتوى المصنف أو عرضه. لتشفير مصنف، قم بتعيين سلسلة كلمة مرور إلى `workbook.settings.password` ثم احفظ المصنف. يكتب Aspose.Cells الملف بشكل مشفر. لفتح مصنف مشفر لفك التشفير، أنشئ كائنًا من `LoadOptions`، وعيّن `load_options.password` على كلمة المرور نفسها المستخدمة أثناء التشفير، ومرّره إلى مُنشئ `Workbook`. يطبّق Aspose.Cells كلمة المرور المقدمة بشفافية بحيث يمكن لبقية الكود الخاص بك التعامل مع المحتوى الذي تم فك تشفيره كما لو كان الملف مصنفًا عاديًا.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## حماية القراءة فقط (كلمة مرور التعديل)
يدعم Excel طبقتين متميزتين من كلمات المرور. الأولى هي كلمة مرور الفتح، التي تشفّر الملف نفسه وتمت تغطيتها في القسم السابق. والثانية هي كلمة مرور التعديل، التي لا تمنع المستخدمين من فتح المصنف؛ بل يوصي Excel بفتح الملف في وضع القراءة فقط ما لم يتم توفير كلمة مرور التعديل. يمكنك تكوين هذا السلوك في Aspose.Cells من خلال `workbook.settings.write_protection`. عيّن خاصية `password` الخاصة بها على كلمة مرور التعديل، وخاصية `author` الخاصة بها لتحديد من قام بتطبيق الحماية. استخدم الأسلوب `write_protection.validate_password(string)` للتحقق مما إذا كانت كلمة مرور التعديل المقدمة صحيحة، حيث يُرجع `true` عند التطابق و`false` خلاف ذلك.

```python
import aspose.cells as ac
# إنشاء مصنف جديد من البداية
workbook = ac.Workbook()
# كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# تكوين حماية الكتابة: تعيين كلمة المرور للتعديل والمؤلف
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# حفظ المصنف بحيث تستمر حماية الكتابة
workbook.save("WriteProtectedWorkbook.xlsx")
# التحقق من كلمة المرور للتعديل باستخدام كلمة المرور الصحيحة
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# التحقق من كلمة المرور للتعديل باستخدام كلمة مرور غير صحيحة لإظهار الفرع الآخر
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## حماية بنية المصنف وإلغاء حمايتها
تمنع حماية بنية المصنف المستخدمين الآخرين من عرض أوراق العمل المخفية، أو إضافة أوراق عمل جديدة، أو نقل أوراق العمل، أو حذف أوراق العمل، أو إخفاء أوراق العمل، أو إعادة تسمية أوراق العمل. تنطبق حالة الحماية على بنية الأوراق وليس على محتويات الخلايا داخل أي ورقة. لتطبيق حماية البنية، استدعِ `workbook.protect(ProtectionType.STRUCTURE, "password")`. لإلغاء الحماية، استدعِ `workbook.unprotect("password")` وقم بتوفير كلمة المرور الصحيحة. تُستخدم قيمة التعداد `ProtectionType.STRUCTURE` هنا وهي متميزة عن أنواع الحماية الأخرى مثل `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# إنشاء مصنف جديد
workbook = ac.Workbook()
# إضافة ورقة عمل ثانية
workbook.worksheets.add()
# كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# حماية بنية المصنف
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# حفظ المصنف باسم structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# إعادة تحميل الملف في نسخة Workbook جديدة
loaded_workbook = ac.Workbook(file_path)
# إلغاء حماية البنية
loaded_workbook.unprotect("StructPwd")
# طباعة رسالة التأكيد
print("Structure protection has been successfully removed from the workbook.")
```

## حماية أوراق العمل وإلغاء حمايتها
تقفل حماية ورقة العمل خلايا ورقة العمل ضد التغييرات العرضية أو المتعمدة. لا يمكن للمستخدمين تحرير الخلايا المقفلة دون توفير كلمة المرور. هذه هي الحماية النموذجية المستخدمة لحماية الصيغ، أو الرؤوس، أو مناطق إدخال البيانات المخصصة في جداول البيانات المشتركة. لحماية ورقة عمل، استدعِ `worksheet.protect(ProtectionType.ALL, "password")`. يفعّل استخدام `ProtectionType.ALL` جميع خيارات الحماية المتاحة مثل تحديد الخلايا المقفلة، وتنسيق الخلايا، وإدراج الصفوف والأعمدة، وحذف الصفوف والأعمدة. لإلغاء الحماية، استدعِ `worksheet.unprotect("password")` بكلمة المرور الصحيحة. يتوفر تحكم أكثر دقة من خلال دمج أنواع حماية أخرى مثل `Contents` و`Objects` و`Scenarios` باستخدام العامل المنطقي OR على مستوى البت.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## إضافة التوقيعات الرقمية والتحقق منها
يضمن التوقيع الرقمي للمستلمين أن محتوى المصنف أصلي ولم يتم تغييره منذ توقيعه. يوفر Aspose.Cells دعمًا للتوقيع الرقمي من خلال مساحة الأسماء `aspose.cells.digital_signatures`. يقوم سير العمل النموذجي بتحميل ملف شهادة `.pfx` من خلال `System.Security.Cryptography.X509Certificates.X509Certificate2`، ويلفّه في كائن `aspose.cells.digital_signatures.DigitalSignature`، ويضيف التوقيع إلى `DigitalSignatureCollection`، ويطبّق المجموعة على المصنف من خلال `workbook.add_digital_signature(DigitalSignatureCollection)`. يمكن لخاصية `digital_signature.comments` تسجيل سياق التوقيع مثل وقت التوقيع والغرض منه. يؤدي أي تعديل يتم إجراؤه على المصنف بعد التوقيع إلى إبطال التوقيع، لذا يمكن لخطوة التحقق من جهة الاستقبال اكتشاف التلاعب.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## مقالات ذات صلة
- [تشفير ملفات Excel وفك تشفيرها](/cells/ar/python-net/encrypt-and-decrypt-excel-files/)
- [حماية بنية المصنف وإلغاء حمايتها](/cells/ar/python-net/protect-and-unprotect-workbook-structure/)
- [حماية ورقة العمل وإلغاء حمايتها](/cells/ar/python-net/protect-and-unprotect-worksheets/)
- [حماية المصنف المشترك بكلمة مرور أو إلغاء حمايته](/cells/ar/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [تعيين والتحقق من صحة التوقيعات الرقمية](/cells/ar/python-net/assign-and-validate-digital-signatures/)
- [التحقق من كلمة مرور التعديل باستخدام Aspose.Cells](/cells/ar/python-net/check-password-to-modify-using-aspose-cells/)
- [اكتشاف تنسيق الملف لملفات Office Open XML المشفرة - OOXML](/cells/ar/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [تشفير ملفات Excel](/cells/ar/python-net/encrypting-excel-files/)
- [كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا](/cells/ar/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}