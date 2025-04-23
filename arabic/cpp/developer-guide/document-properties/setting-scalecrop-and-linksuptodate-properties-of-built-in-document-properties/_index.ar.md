---
title: تعيين خصائص ScaleCrop وLinksUpToDate لخصائص المستند المدمجة باستخدام C++
linktitle: تعيين خصائص ScaleCrop وLinksUpToDate
type: docs
weight: 320
url: /ar/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: تعلم كيفية تعيين خصائص ScaleCrop وLinksUpToDate لخصائص المستند المدمجة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) و [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) هما مجموعتان موسعتان من خصائص المستند المدمجة المعرفة ضمن تنسيق OpenXml. الغرض من هذه الخصائص هو كما يلي:

## **1) ScaleCrop**
يشير هذا العنصر إلى وضع عرض الصورة المصغرة للمستند. قم بتعيين هذا العنصر إلى **TRUE** لتمكين تحجيم الصورة المصغرة للعرض. قم بتعيين هذا العنصر إلى **FALSE** لتمكين قص الصورة المصغرة لإظهار أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **2) LinksUpToDate**
يشير هذا العنصر إلى ما إذا كانت الروابط الفائقة في مستند محدثة. قم بتعيين هذا العنصر إلى **TRUE** للإشارة إلى أن الروابط الفائقة تم تحديثها. قم بتعيين هذا العنصر إلى **FALSE** للدلالة على أن الروابط الفائقة قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **تعيين خصائص ScaleCrop وLinksUpToDate لخصائص المستند المدمجة**
يتم إعداد الكود النموذجي التالي خصائص المستند المدمجة الموسعة [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) و [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) للملف العمل. يرجى التحقق من ملف الإكسل الناتج ([ملف الإكسل الناتج](5115500.xlsx)) الذي تم إنشاؤه باستخدام هذا الكود، وتغييره إلى ملحق .zip، ثم فك ضغط محتوياته، وعرض ملف app.xml كما هو موضح في الصورة أعلاه.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
