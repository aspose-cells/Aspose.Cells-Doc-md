---
title: تحديد إصدار المستند لملف Excel باستخدام خصائص المستند المدمجة باستخدام C++
linktitle: تحديد إصدار المستند
type: docs
weight: 20
url: /ar/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: تعلم كيفية تحديد إصدار مستند Excel باستخدام خصائص المستند المدمجة مع Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تغيير **رقم الإصدار** الخاص بملف Excel بالنقر بزر الماوس الأيمن على الملف ثم اختيار الخصائص > التفاصيل ثم تحرير حقل **رقم الإصدار**. يرجى استخدام خاصية [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) لتغييره برمجياً باستخدام واجهات برمجة التطبيقات Aspose.Cells.

## **تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة**

يخلق الكود النموذجي التالي مصنفًا ويغير خصائص المستند المدمجة التي تشمل العنوان، والمؤلفين، ورقم الإصدار. يرجى مراجعة ملف الإكسل الناتج ([ملف الإكسل الناتج](64716811.xlsx)) الذي تم إنشاؤه بواسطة الكود، ولقطة الشاشة التي تظهر تعديل رقم الإصدار بواسطة خاصية [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **الكود المثالي**

```cpp
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

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
