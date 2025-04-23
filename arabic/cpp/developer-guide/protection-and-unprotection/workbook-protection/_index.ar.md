---
title: حماية وإلغاء حماية هيكل المصنف باستخدام C++
linktitle: حماية وإلغاء حماية هيكل دفتر العمل
type: docs
weight: 40
url: /ar/cpp/protect-and-unprotect-workbook-structure/
description: حماية وإلغاء حماية هيكل ملف إكسل باستخدام C++ مع Aspose.Cells.
---

{{% alert color="primary" %}}
لمنع المستخدمين الآخرين من عرض أوراق عمل مخفية، أو إضافتها، أو نقلها، أو حذفها، أو إخفاءها، أو إعادة تسميتها، يمكنك حماية هيكل دفتر العمل الخاص بك بكلمة مرور.
{{% /alert %}}

## **حماية وإلغاء حماية هيكل المصنف في MS Excel**

**![حماية وإلغاء حماية هيكل دفتر العمل](protect-and-unprotect-workbook-structure.png)**

1. انقر على **مراجعة > حماية الدفتر**.
١. أدخل كلمة مرور في **مربع الكلمة السرية**.
١. حدد **موافق**, أدخل كلمة المرور مرة أخرى لتأكيدها، ثم حدد **موافق** مجددًا.

## **حماية هيكل المصنف باستخدام Aspose.Cells for C++**
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

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إلغاء حماية هيكل المصنف باستخدام Aspose.Cells for C++**
إلغاء حماية هيكل الدفتر بسيط مع واجهة برمجة تطبيقات Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
ملاحظة: كلمة مرور صحيحة مطلوبة.
{{% /alert %}}
