---
title: حماية مستندات PDF مع C++
linktitle: مستندات PDF الآمنة
type: docs
weight: 120
url: /ar/cpp/secure-pdf-documents/
description: تعلم كيفية تأمين مستندات PDF بكلمات مرور المالك والمستخدم باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع ملفات PDF المُشفرة. على سبيل المثال:

- تأمين المستندات بكلمات مرور للمالك والمستخدم حتى لا يمكن لأي شخص فتحه.
- تعيين قيود أو أذونات للمستند بعد فتحه، على سبيل المثال: تقييد ما إذا كان بإمكان محتوى المستند أن يُطبع أو يستخرج.

يشرح هذا المقال كيفية تمرير خيارات أمان PDF عند حفظ الجداول الإلكترونية إلى PDF.

{{% /alert %}}

توفر Aspose.Cells [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) للعمل مع الأمان. يمكنك تعيين كلمات مرور المالك والمستخدم أثناء الحفظ إلى PDF. ستكون كلمة مرور المالك أو كلمة مرور المستخدم مطلوبة لفتح مستند PDF المشفر للمشاهدة.

- يمكن أن تكون كلمة المرور للمستخدم فارغة أو سلسلة فارغة، في هذه الحالة لن يكون هناك حاجة إلى كلمة مرور من المستخدم عند فتح مستند PDF.
- يتيح فتح مستند PDF بكلمة مرور المالك الصحيحة الوصول الكامل (بدون أي قيود وصول محددة) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور للمستخدم) يسمح بوصول محدود حيث تم تحديد الأذونات.

يصف الكود النموذجي أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

إذا كانت ورقة العمل تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل تصييرها إلى PDF. وهذا يضمن إعادة حساب القيم المعتمدة على الصيغ وتصحيح القيم المعروضة في PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
