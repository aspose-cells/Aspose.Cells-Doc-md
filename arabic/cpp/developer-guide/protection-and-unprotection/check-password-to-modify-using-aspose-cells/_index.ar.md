---
title: التحقق من كلمة المرور للتعديل باستخدام Aspose.Cells مع C++
linktitle: التحقق من كلمة المرور للتعديل
type: docs
weight: 2400
url: /ar/cpp/check-password-to-modify-using-aspose-cells/
description: تحقق مما إذا كانت كلمة المرور المقدمة مطابقة لكلمة المرور للتعديل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى التحقق إذا كانت كلمة المرور المقدمة تتطابق مع **كلمة المرور للتعديل** برمجيًا. يوفر Aspose.Cells طريقة WorkbookSettings.WriteProtection.ValidatePassword() والتي يمكن استخدامها للتحقق مما إذا كانت كلمة المرور للتعديل صحيحة أم لا.

{{% /alert %}}

## **التحقق من كلمة المرور للتعديل في Microsoft Excel**

يمكنك تعيين **كلمة السر للفتح** و**كلمة السر للتعديل** أثناء إنشاء جداول البيانات الخاصة بك في Microsoft Excel. يُرجى الرجوع إلى هذا اللقط الشاشة الذي يظهر واجهة Microsoft Excel المُقدمة لتحديد هذه الكلمات السرية.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **التحقق من كلمة المرور للتعديل باستخدام Aspose.Cells**

يقوم الأكواد العينة التالية بتحميل ملف الإكسل المصدري. يحتوي على كلمة سر لفتح الملف 1234 وكلمة سر للتعديل 5678. تقوم الكود أولاً بالتحقق مما إذا كانت 567 كلمة سر للتعديل صحيحة ويُعيد القيمة false وبعد ذلك يتحقق مما إذا كانت 5678 كلمة سر للتعديل ويُعيد القيمة true.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **مخرجات الوحدة**

إليك مخرجات الكونسول للشيفرة العينة أعلاه بعد تحميل ملف الإكسل المصدري.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
