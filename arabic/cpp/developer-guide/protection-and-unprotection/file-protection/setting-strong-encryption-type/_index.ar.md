---
title: إعداد نوع التشفير القوي باستخدام C++
linktitle: ضبط نوع التشفير القوي
type: docs
weight: 60
url: /ar/cpp/setting-strong-encryption-type/
description: تعلم كيفية تطبيق التشفير القوي وحماية كلمة المرور لملفات Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يتيح Microsoft Excel (97-2007/2010) لك تشفير وحماية كلمة المرور لجداول البيانات. إنه يستخدم خوارزميات مقدمة من موفر خدمة التشفير. موفر خدمة التشفير (أو CSP) هو مجموعة من الخوارزميات التشفيرية ذات خصائص مختلفة. يعد موفر خدمة التشفير الافتراضي "متوافق مع Office 97/2000". هذا هو موفر خدمة تشفير مع بعض المشاكل الأمنية المعروفة علناً. يمكن كسر جداول البيانات التي تم تأمينها بـ "تشفير ضعيف (XOR)" أو بنوع التشفير "متوافق مع Office 97/2000" بسهولة.

لتجاوز هذه المشكلة، استخدم أحد أنواع التشفير القوية المقدمة من Microsoft Excel. يمكنك تغيير نوع التشفير إلى أقوى موفر خدمة تشفير متاح. للتشفير القوي، يتطلب طول مفتاح أدنى من 128 بت، على سبيل المثال، 'موفر خدمة التشفير القوي لشركة Microsoft'.

يمكنك أيضًا تشفير ملفات إكسل بنوع تشفير قوي وحمايتها بكلمة مرور باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

## **تطبيق التشفير مع مايكروسوفت إكسل**
لتنفيذ تشفير الملف في مايكروسوفت إكسل (مثلاً 2007):

١. من قائمة **الأدوات**, حدد **خيارات**.
١. حدد علامة التبويب **الأمان**.
١. أدخل قيمة لحقل **كلمة المرور للفتح**.
1. انقر على **متقدم**.
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **تطبيق التشفير مع Aspose.Cells**
تطبيق الشفرة أدناه يطبق تشفيرًا قويًا على ملف ويعين كلمة مرور.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "File encrypted and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
