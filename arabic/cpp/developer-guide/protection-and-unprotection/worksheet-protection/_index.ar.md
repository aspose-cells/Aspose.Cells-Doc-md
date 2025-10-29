---
title: حماية وإلغاء حماية ورقة العمل باستخدام C++
linktitle: حماية وإلغاء الحماية لورق العمل
type: docs
weight: 40
url: /ar/cpp/protect-and-unprotect-worksheets/
description: حماية وإلغاء حماية ورقة عمل ملفات إكسل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}
لمنع مستخدمين آخرين من تغيير البيانات في ورقة العمل عن طريق الخطأ أو بشكل متعمد، يمكنك قفل الخلايا في ورقة العمل الخاصة بك ثم حماية الورقة بكلمة مرور. 
{{% /alert %}}

## **حماية وإلغاء حماية ورقة العمل في MS Excel**

**![حماية وإلغاء حماية ورقة العمل](protect-and-unprotect-worksheet.png)**

١. انقر فوق **مراجعة > حماية ورقة عمل**.
١. أدخل كلمة مرور في **مربع الكلمة السرية**.
١. حدد خيارات **السماح**.
١. حدد **موافق**, أدخل كلمة المرور مرة أخرى لتأكيدها، ثم حدد **موافق** مجددًا.

## **حماية ورقة العمل باستخدام Aspose.Cells for C++**
متطلبات الترميز البسيطة التالية فقط لتنفيذ حماية هيكل دفتر العمل لملفات Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إلغاء حماية ورقة العمل باستخدام Aspose.Cells for C++**
إلغاء الحماية لورقة العمل سهل مع واجهة برمجة تطبيقات Aspose.Cells. إذا كانت ورقة العمل محمية بكلمة مرور، فقد تكون هناك حاجة إلى كلمة مرور صحيحة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إعدادات الحماية المتقدمة منذ Excel XP](/cells/ar/cpp/advanced-protection-settings-since-excel-xp/)
- [الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور](/cells/ar/cpp/detect-if-worksheet-is-password-protected/)
- [حماية ورق العمل](/cells/ar/cpp/protecting-worksheets/)
- [إلغاء حماية ورقة العمل](/cells/ar/cpp/unprotect-a-worksheet/)
- [التحقق من الكلمة المستخدمة لحماية ورقة العمل](/cells/ar/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
