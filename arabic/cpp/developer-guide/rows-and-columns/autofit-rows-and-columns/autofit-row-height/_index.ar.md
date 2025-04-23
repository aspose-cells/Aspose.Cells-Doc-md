---
title: ملائمة الصفوف تلقائيًا عند تحميل الملف باستخدام C++
linktitle: تكييف ارتفاع الصف تلقائياً عند تحميل الملف
type: docs
weight: 120
url: /ar/cpp/autofit-row-height/
description: تعلم كيفية ملائمة الصفوف التي لا تتم تهيئتها باستخدام Aspose.Cells مع C++.
keywords: تكييف ارتفاع الصف تلقائياً عند تحميل الملف، ضبط ارتفاع الصف تلقائيًا عند فتح ملف إكسل.
---

## **سيناريوهات الاستخدام المحتملة**
تتناسب ارتفاع الصف تلقائيًا مع خط المحتوى، ولكن عندما لا يتطابق ارتفاع الصف المخزن مع ارتفاع المحتوى في الملف، سيقوم MS Excel تلقائيًا بضبط ارتفاع الصف عند تحميل الملف، بينما لن يقوم Aspose.Cells بضبطه تلقائيًا لتحسين الأداء. إذا كنت بحاجة إلى استخدام برنامج Aspose.Cells لمطابقة ارتفاعات السطر تلقائيًا عند تحميل الملفات، يمكنك تحقيق الهدف من خلال المعامل [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

يرجى الرجوع إلى البيانات التالية للصورة. يمكننا مراقبة ارتفاع الصف المخزن في السطر 11 وهو 15، ولكن أكسل ضبط آلياً ارتفاع الصف عند تحميل الملف.
<br>
<img src="1.png" width=70% />

## **ضبط ارتفاع الصف باستخدام Aspose.Cells**
إذا قمت بتحميل الملف مباشرة وحفظه في تنسيق PDF، فلن يتم عرض البيانات بالكامل في ملف PDF لأن ارتفاع الصف المخزن 15 فقط.
<br>
<img src="2.png" width=70% />
<br>
إذا قمت بضبط المعامل [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) على true عند تحميل الملف، فسيقوم Aspose.Cells تلقائيًا بضبط ارتفاع الصف. يمكن لارتفاع السطر المعدل تلبية متطلبات عرض النص بشكل فعال.
<br>
<img src="3.png" width=70% />

## **كود نموذج C++**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
