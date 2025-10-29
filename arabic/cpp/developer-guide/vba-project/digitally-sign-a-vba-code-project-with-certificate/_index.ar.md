---
title: توقيع مشروع كود VBA رقميًا باستخدام شهادة في C++
linktitle: التوقيع الرقمي لمشروع كود VBA بشهادة
type: docs
weight: 110
url: /ar/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: تعلم كيفية توقيع مشروع كود VBA رقميًا باستخدام Aspose.Cells for C++ مع شهادة.
---

{{% alert color="primary" %}} 

يمكنك توقيع مشروع كود VBA رقميًا باستخدام Aspose.Cells مع طريقتها [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). يرجى اتباع هذه الخطوات للتحقق مما إذا كان ملف إكسل الخاص بك موقعًا رقمياً بشهادة.

- انقر **المرجع البرمجي المرئي** من علامة التبويب **المطور** لفتح **بيئة تطوير Visual Basic for Applications**.
- انقر **الأدوات** > **التوقيعات الرقمية...** في **بيئة تطوير Visual Basic for Applications**.

سيعرض نموذج **التوقيع الرقمي** موضحًا ما إذا كان المستند موقعًا رقمياً بشهادة أم لا.

{{% /alert %}} 

## **توقيع مشروع كود VBA رقميًا باستخدام شهادة في C++**

يُوضح الشفرة النموذجية التالية كيفية استخدام طريقة [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). إليك ملفات الإدخال والإخراج للشفرة النموذجية. يمكنك استخدام أي ملف إكسل وأي شهادة لاختبار هذا الكود.

- [ملف Excel المصدر](5115028.xlsm) المستخدم في الكود العيني.
- [ملف pfx العيني](5115039.pfx) لإنشاء توقيع رقمي. يرجى تثبيته على جهاز الكمبيوتر الخاص بك لتشغيل هذا الكود. كلمة المرور الخاصة به هي 1234.
- [ملف Excel الناتج](5115029.xlsm) الذي تم إنشاؤه بواسطة الكود العيني.

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String password(u"1234");
    U16String pfxPath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.pfx";
    U16String comment(u"Signing Digital Signature using Aspose.Cells");

    Vector<uint8_t> certData;

    std::time_t now = std::time(nullptr);
    std::tm* now_tm = std::localtime(&now);
    int year = now_tm->tm_year + 1900;
    int month = now_tm->tm_mon + 1;
    int day = now_tm->tm_mday;
    int hour = now_tm->tm_hour;
    int minute = now_tm->tm_min;
    int second = now_tm->tm_sec;

    DigitalSignature digitalSignature(certData, password, comment, Date{year, month, day, hour, minute, second, 0});

    U16String inputFilePath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.xlsm";
    Workbook workbook(inputFilePath);

    workbook.GetVbaProject().Sign(digitalSignature);

    U16String outputFilePath = outDir + u"outputDigitallySignVbaProjectWithCertificate.xlsm";
    workbook.Save(outputFilePath);

    std::cout << "VBA project digitally signed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
