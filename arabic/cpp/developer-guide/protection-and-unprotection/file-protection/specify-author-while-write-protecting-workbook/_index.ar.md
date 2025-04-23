---
title: تحديد المؤلف أثناء حماية الكتاب بكلمة مرور باستخدام C++
linktitle: تحديد المؤلف أثناء حماية كتاب العمل
type: docs
weight: 40
url: /ar/cpp/specify-author-while-write-protecting-workbook/
description: تعلم كيف يمكن تحديد اسم المؤلف أثناء حماية الكتاب باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك تحديد اسم المؤلف أثناء حماية كتابك باستخدام واجهة برمجة التطبيقات Aspose.Cells. يرجى استخدام الخاصية [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) لهذا الغرض.

## **تحديد المؤلف أثناء حماية كتاب العمل**

يوضح الكود النموذجي التالي كيفية استخدام خاصية [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) لإضافة توقيعات رقمية إلى ملفات Excel الموقعة مسبقًا. ينشئ الكود كتاب عمل فارغًا، يحمى بكلمة مرور، يحدد اسم المؤلف، ويحفظه كملف Excel ناتج. يوضح لقطة الشاشة التالية تأثير الكود على ملف Excel الناتج للمرجع الخاص بك.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
