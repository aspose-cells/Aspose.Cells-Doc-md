---
title: تحديد لغة ملف Excel باستخدام خصائص المستند المدمجة باستخدام C++
linktitle: تحديد لغة ملف Excel
type: docs
weight: 30
url: /ar/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: تعلم كيفية تغيير لغة ملف Excel برمجيًا باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تغيير لغة ملف Excel بالنقر بزر الماوس الأيمن على الملف ثم اختيار الخصائص > التفاصيل ثم تحرير حقل اللغة. يرجى استخدام خاصية [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) لتغييره برمجياً باستخدام واجهات برمجة تطبيقات Aspose.Cells.

## **تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند**

يخلق الكود النموذجي التالي مصنفًا ويغير خاصية المستند المدمجة المسماة Language. يرجى مراجعة ملف الإكسل الناتج ([ملف الإكسل الناتج](64716891.xlsx)) الذي تم إنشاؤه بواسطة الكود، وصورة الشاشة التي تظهر تعديل حقل اللغة بواسطة خاصية [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
