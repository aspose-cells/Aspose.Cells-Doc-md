---
title: حماية وفك الحماية
linktitle: الحماية
description: يقدم هذا القسم كيفية تشفير ملفات Excel وفك تشفيرها وحماية بيانات Excel، بما يشمل تشفير الملفات، والحماية للقراءة فقط، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيعات الرقمية باستخدام كود Python
keywords: Aspose.Cells, Python via Java, تشفير, فك تشفير, كلمة مرور, حماية, إلغاء حماية, حماية المصنف, حماية ورقة العمل, قراءة فقط, توقيع رقمي, Python
type: docs
weight: 68
url: /ar/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

غالبًا ما تخزن مصنفات Excel معلومات مالية أو تجارية أو شخصية حساسة يجب حمايتها من الوصول غير المصرح به. يوفر Aspose.Cells for Python via Java مجموعة شاملة من ميزات الحماية التي تعكس إمكانيات Microsoft Excel، مما يتيح لك تأمين بياناتك على مستوى الملف، ومستوى المصنف، ومستوى ورقة العمل.

{{% alert color="primary" %}}
يوفر Aspose.Cells for Python via Java مجموعة واسعة من ميزات الحماية، من مستوى الملف إلى مستوى البيانات، على غرار MS Excel. تتضمن هذه الإمكانيات تشفير الملفات بكلمة مرور، وفرض الوصول للقراءة فقط من خلال كلمة مرور للتعديل، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيع الرقمي على المصنفات.
{{% /alert %}}

## تشفير وفك تشفير ملفات Excel
تمنع كلمة المرور المعينة على ملف Excel المستخدمين غير المصرح لهم من فتح محتوى المصنف أو عرضه. لتشفير مصنف، قم بتعيين سلسلة كلمة مرور إلى `workbook.getSettings().setPassword(...)` ثم احفظ المصنف. يكتب Aspose.Cells الملف بشكل مشفر. لفتح مصنف مشفر لفك التشفير، قم بإنشاء كائن `LoadOptions`، وتعيين كلمة المرور عبر `load_options.setPassword(...)` إلى نفس كلمة المرور المستخدمة أثناء التشفير، وتمريرها إلى مُنشئ `Workbook`. يطبق Aspose.Cells كلمة المرور المقدمة بشفافية بحيث يمكن لبقية التعليمات البرمجية التفاعل مع المحتوى الذي تم فك تشفيره كما لو كان الملف مصنفًا عاديًا.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## حماية القراءة فقط (كلمة مرور للتعديل)
يدعم Excel طبقتين مميزتين من كلمات المرور. الأولى هي كلمة مرور الفتح، والتي تشفّر الملف نفسه وقد تم تناولها في القسم السابق. الثانية هي كلمة مرور التعديل، والتي لا تمنع المستخدمين من فتح المصنف؛ وبدلاً من ذلك، يوصي Excel بفتح الملف في وضع القراءة فقط ما لم يتم توفير كلمة مرور التعديل. قم بتكوين هذا السلوك في Aspose.Cells من خلال `workbook.getSettings().getWriteProtection()`. عيّن كلمة المرور عبر `setPassword(...)` إلى كلمة مرور التعديل، والمؤلف عبر `setAuthor(...)` لتحديد من قام بتطبيق الحماية. استخدم الطريقة `writeProtection.validatePassword(String)` للتحقق مما إذا كانت كلمة مرور التعديل المقدمة صحيحة، حيث تُرجع `true` عند التطابق و`false` خلاف ذلك.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# إنشاء مصنف جديد من البداية
workbook = Workbook()
# كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# تكوين حماية الكتابة: تعيين كلمة المرور للتعديل والمؤلف
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# حفظ المصنف بحيث تستمر حماية الكتابة
workbook.save("WriteProtectedWorkbook.xlsx")
# التحقق من صحة كلمة المرور للتعديل باستخدام كلمة المرور الصحيحة
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# التحقق من صحة كلمة المرور للتعديل باستخدام كلمة مرور غير صحيحة لتوضيح الفرع الآخر
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## حماية بنية المصنف وإلغاء حمايتها
تمنع حماية بنية المصنف المستخدمين الآخرين من عرض أوراق العمل المخفية، أو إضافة أوراق عمل جديدة، أو نقل أوراق العمل، أو حذف أوراق العمل، أو إخفاء أوراق العمل، أو إعادة تسمية أوراق العمل. تنطبق الحالة المحمية على بنية الورقة بدلاً من محتويات الخلايا داخل أي ورقة. لتطبيق حماية البنية، اتصل بـ `workbook.protect(ProtectionType.STRUCTURE, "password")`. لإلغاء الحماية، اتصل بـ `workbook.unprotect("password")` ووفر كلمة المرور الصحيحة. تُستخدم قيمة التعداد `ProtectionType.STRUCTURE` هنا وتختلف عن أنواع الحماية الأخرى مثل `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# إنشاء مصنف جديد
workbook = Workbook()
# إضافة ورقة عمل ثانية
workbook.getWorksheets().add()
# كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# حماية بنية المصنف
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# حفظ المصنف باسم structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# إعادة تحميل الملف في نسخة Workbook جديدة
loaded_workbook = Workbook(file_path)
# إلغاء حماية البنية
loaded_workbook.unprotect("StructPwd")
# طباعة رسالة التأكيد
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## حماية أوراق العمل وإلغاء حمايتها
تقوم حماية ورقة العمل بقفل خلايا ورقة العمل ضد التغييرات العرضية أو المتعمدة. لا يمكن للمستخدمين تحرير الخلايا المقفلة دون توفير كلمة المرور. هذه هي الحماية النموذجية المستخدمة لحماية الصيغ أو العناوين أو مناطق إدخال البيانات المحددة في جداول البيانات المشتركة. لحماية ورقة عمل، اتصل بـ `worksheet.protect(ProtectionType.ALL, "password")`. يتيح استخدام `ProtectionType.ALL` جميع خيارات الحماية المتاحة مثل تحديد الخلايا المقفلة، وتنسيق الخلايا، وإدراج الصفوف والأعمدة، وحذف الصفوف والأعمدة. لإلغاء الحماية، اتصل بـ `worksheet.unprotect("password")` بكلمة المرور الصحيحة. يتوفر تحكم أكثر دقة من خلال دمج أنواع الحماية الأخرى مثل `ProtectionType.CONTENTS` و`ProtectionType.OBJECTS` و`ProtectionType.SCENARIOS` باستخدام OR على مستوى البت.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## إضافة والتحقق من صحة التوقيعات الرقمية
يضمن التوقيع الرقمي للمستلمين أن محتوى المصنف أصيل ولم يتم تغييره منذ توقيعه. يوفر Aspose.Cells دعم التوقيع الرقمي من خلال مساحة الاسم `Aspose.Cells.DigitalSignatures`. يقوم سير العمل النموذجي بتحميل ملف شهادة `.pfx` من خلال `java.security.KeyStore`، ولفه في `Aspose.Cells.DigitalSignatures.DigitalSignature`، وإضافة التوقيع إلى `DigitalSignatureCollection`، وتطبيق المجموعة على المصنف من خلال `workbook.addDigitalSignature(digitalSignatureCollection)`. يمكن لخاصية `digitalSignature.getComments()` تسجيل سياق التوقيع مثل وقت التوقيع والغرض منه. أي تعديل يتم إجراؤه على المصنف بعد التوقيع يبطل التوقيع، لذا يمكن لخطوة التحقق من جانب المستلم اكتشاف التلاعب.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# تحميل الشهادة من ملف PFX باستخدام Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# الحصول على الشهادة
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# إنشاء توقيع رقمي
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# إنشاء المصنف وإضافة التوقيع
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## مقالات ذات صلة
- [تشفير وفك تشفير ملفات Excel](/cells/ar/python-java/encrypt-and-decrypt-excel-files/)
- [حماية بنية المصنف وإلغاء حمايتها](/cells/ar/python-java/protect-and-unprotect-workbook-structure/)
- [حماية ورقة العمل وإلغاء حمايتها](/cells/ar/python-java/protect-and-unprotect-worksheet/)
- [التحقق من كلمة مرور التعديل باستخدام Aspose.Cells](/cells/ar/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}