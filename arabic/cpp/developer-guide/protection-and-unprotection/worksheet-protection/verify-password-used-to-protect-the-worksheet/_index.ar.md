---
title: التحقق من كلمة المرور المستخدمة لحماية ورقة العمل مع C++
linktitle: التحقق من الكلمة المستخدمة لحماية ورقة العمل
type: docs
weight: 370
url: /ar/cpp/verify-password-used-to-protect-the-worksheet/
description: تعلم كيفية التحقق من كلمة المرور المستخدمة لحماية ورقة العمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

قد قامت واجهات برمجة التطبيقات Aspose.Cells بتعزيز فئة [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) من خلال إدخال بعض الخصائص والوسائل المفيدة. إحدى هذه الوسائل هي [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) التي تسمح بتحديد كلمة مرور كنسخة من *string* والتحقق مما إذا كانت نفس كلمة المرور تم استخدامها لحماية [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

ترجع [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) **true** إذا كانت كلمة المرور المحددة تتطابق مع كلمة المرور المستخدمة لحماية ورقة العمل المعطاة و **false** إذا لم تتطابق. يستخدم المقطع التالي من الكود طريقة [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) جنبًا إلى جنب مع خاصية [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) لاكتشاف حماية كلمة المرور والتحقق منها.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
