---
title: حماية وإلغاء الحماية باستخدام C++
linktitle: التشفير والحماية
description: يتناول هذا القسم كيفية تشفير ملفات Excel وفك تشفيرها وحماية بيانات Excel، ويغطي تشفير الملفات والحماية للقراءة فقط وحماية بنية المصنف وحماية ورقة العمل والتوقيعات الرقمية باستخدام كود C++
keywords: Aspose.Cells, Aspose.Cells for C++, تشفير, فك تشفير, كلمة مرور, حماية, إلغاء حماية, حماية المصنف, حماية ورقة العمل, قراءة فقط, توقيع رقمي, C++
type: docs
weight: 68
url: /ar/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

غالبًا ما تخزّن مصنفات Excel معلومات مالية أو تجارية أو شخصية حساسة يجب حمايتها من الوصول غير المصرح به. يوفّر Aspose.Cells for C++ مجموعة شاملة من ميزات الحماية التي تعكس إمكانات Microsoft Excel، مما يتيح لك تأمين بياناتك على مستوى الملف والمصنف وورقة العمل.

{{% alert color="primary" %}}
يوفّر Aspose.Cells for C++ مجموعة واسعة من ميزات الحماية، من مستوى الملف إلى مستوى البيانات، على غرار MS Excel. وتشمل هذه الإمكانات تشفير الملفات بكلمة مرور، وفرض الوصول للقراءة فقط من خلال كلمة مرور للتعديل، وحماية بنية المصنف، وحماية أوراق العمل، والتوقيع الرقمي على المصنفات.
{{% /alert %}}

## تشفير ملفات Excel وفك تشفيرها
تمنع كلمة المرور المعيّنة على ملف Excel المستخدمين غير المصرح لهم من فتح المصنف أو عرض محتوياته. لتشفير المصنف، عيّن سلسلة كلمة المرور على `workbook.GetSettings().SetPassword()` ثم احفظ المصنف. يكتب Aspose.Cells الملف في صورة مشفرة. ولفتح مصنف مشفر لإجراء فك التشفير، أنشئ كائن `LoadOptions`، وعيّن `LoadOptions.SetPassword()` على كلمة المرور نفسها المستخدمة أثناء التشفير، ثم مرّرها إلى مُنشئ `Workbook`. يطبّق Aspose.Cells كلمة المرور المقدمة بشفافية، بحيث يتفاعل بقية التعليمات البرمجية مع المحتوى الذي تم فك تشفيره كما لو كان الملف مصنفًا عاديًا.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## الحماية للقراءة فقط (كلمة مرور للتعديل)
يدعم Excel طبقتين مختلفتين لكلمات المرور. الأولى هي كلمة مرور للفتح، وهي كلمة المرور التي تشفّر الملف نفسه وقد وردت في القسم السابق. أما الثانية فهي كلمة مرور للتعديل، وهي لا تمنع المستخدمين من فتح المصنف؛ بل يوصي Excel بفتح الملف في وضع للقراءة فقط ما لم تُقدَّم كلمة مرور التعديل. اضبط هذا السلوك في Aspose.Cells من خلال `workbook.GetSettings().GetWriteProtection()`. عيّن خاصية `Password` الخاصة بها على كلمة مرور التعديل، وخاصية `Author` الخاصة بها لتحديد من قام بتطبيق الحماية. استخدم أسلوب `WriteProtection.ValidatePassword()` للتحقق مما إذا كانت كلمة مرور التعديل المقدمة صحيحة؛ إذ يُرجع `true` عند المطابقة و`false` في حالة أخرى.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## حماية بنية المصنف وإلغاء الحماية
تمنع حماية بنية المصنف المستخدمين الآخرين من عرض أوراق العمل المخفية أو إضافة أوراق عمل جديدة أو نقلها أو حذفها أو إخفائها أو إعادة تسميتها. تنطبق حالة الحماية على بنية الأوراق بدلاً من محتويات الخلايا داخل أي ورقة. لتطبيق حماية البنية، استدعِ `workbook.Protect(ProtectionType::Structure, "password")`. ولإلغاء الحماية، استدعِ `workbook.Unprotect("password")` مع كلمة المرور الصحيحة. تُستخدم هنا قيمة تعداد `ProtectionType::Structure`، وهي مختلفة عن أنواع الحماية الأخرى مثل `ProtectionType::Windows`.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // إنشاء مصنف جديد
    Workbook workbook;
    // إضافة ورقة عمل ثانية
    workbook.GetWorksheets().Add();
    // كتابة قيمة عينة في الخلية A1 من ورقة العمل الأولى
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // حماية بنية المصنف
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // حفظ المصنف كملف structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // إعادة تحميل الملف في مثيل Workbook جديد
    Workbook loadedWorkbook(filePath);
    // إلغاء حماية البنية
    loadedWorkbook.Unprotect(u"StructPwd");
    // طباعة رسالة التأكيد
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## حماية أوراق العمل وإلغاء الحماية
تمنع حماية ورقة العمل تعديل الخلايا المقفلة في ورقة العمل، سواء عن طريق الخطأ أو عن قصد. لا يمكن للمستخدمين تحرير الخلايا المقفلة دون توفير كلمة المرور. وهذه هي الحماية المعتادة المستخدمة لحماية الصيغ أو رؤوس الصفوف أو مناطق إدخال البيانات المخصصة في جداول البيانات المشتركة. لحماية ورقة عمل، استدعِ `worksheet.Protect(ProtectionType::All, "password")`. يتيح استخدام `ProtectionType::All` تفعيل جميع خيارات الحماية المتاحة، مثل تحديد الخلايا المقفلة وتنسيق الخلايا وإدراج الصفوف والأعمدة وحذف الصفوف والأعمدة. ولإلغاء الحماية، استدعِ `worksheet.Unprotect("password")` مع كلمة المرور الصحيحة. يتوفر تحكم أدق من خلال دمج أنواع حماية أخرى مثل `Contents` و`Objects` و`Scenarios` باستخدام عامل OR على مستوى البتات.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## إضافة التوقيعات الرقمية والتحقق منها
تضمن التوقيعات الرقمية للمستلمين أن محتوى المصنف أصلي ولم يتم تغييره منذ توقيعه. يوفّر Aspose.Cells دعمًا للتوقيعات الرقمية من خلال مساحة الاسم ‏`Aspose::Cells::DigitalSignatures`. يتطلب سير العمل المعتاد تحميل ملف شهادة ‏`.pfx`، وتغليفه في `Aspose::Cells::DigitalSignatures::DigitalSignature`، ثم إضافة التوقيع إلى `DigitalSignatureCollection`، وتطبيق المجموعة على المصنف من خلال `workbook.AddDigitalSignature(DigitalSignatureCollection)`. يمكن لخاصية `DigitalSignature.GetComments()` تسجيل سياق التوقيع، مثل وقت التوقيع وسببه. يُبطل أي تعديل يُجرى على المصنف بعد التوقيع التوقيع، لذا يمكن لخطوة التحقق في جانب الاستلام اكتشاف أي عبث بالبيانات.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## مقالات ذات صلة
- [تشفير ملفات Excel وفك تشفيرها](/cells/ar/cpp/encrypt-and-decrypt-excel-files/)
- [حماية بنية المصنف وإلغاء الحماية](/cells/ar/cpp/protect-and-unprotect-workbook-structure/)
- [حماية ورقة العمل وإلغاء الحماية](/cells/ar/cpp/protect-and-unprotect-worksheets/)
- [حماية المصنف المشترك بكلمة مرور أو إلغاء الحماية](/cells/ar/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [التحقق من كلمة مرور التعديل باستخدام Aspose.Cells](/cells/ar/cpp/check-password-to-modify-using-aspose-cells/)
- [اكتشاف تنسيق الملفات المشفرة بصيغة Office Open XML - OOXML](/cells/ar/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [تشفير ملفات Excel](/cells/ar/cpp/encrypting-excel-files/)
- [كيفية اكتشاف تنسيق ملف والتحقق مما إذا كان الملف مشفّرًا](/cells/ar/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}