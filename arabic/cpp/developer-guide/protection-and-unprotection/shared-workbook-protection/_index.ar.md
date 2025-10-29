---
title: حماية أو إلغاء حماية المصنف المشترك بكلمة مرور باستخدام C++
linktitle: حماية كلمة المرور أو إلغاء حمايتها لكتاب العمل المشترك
type: docs
weight: 10
url: /ar/cpp/password-protect-or-unprotect-the-shared-workbook/
description: تعلم كيفية حماية أو إلغاء حماية مصنف مشترك بكلمة مرور باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك حماية أو إلغاء حماية كتاب العمل المشترك مع Microsoft Excel كما هو موضح في لقطة الشاشة التالية. تدعم Aspose.Cells أيضًا هذه الميزة باستخدام الطرق [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) و [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **حماية كلمة المرور أو إلغاء حمايتها لكتاب العمل المشترك**

الرمز البريدي العيني التالي ينشئ كتاب عمل ويحميه أثناء تمكين العمل المشترك ويحفظه كملف Excel الناتج. تبين لقطة الشاشة أنه عند محاولة إلغاء حمايته ، يطلب منك Microsoft Excel إدخال كلمة المرور لإلغاء حمايته.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
