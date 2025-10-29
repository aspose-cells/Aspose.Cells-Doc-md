---
title: إنشاء خط توقيع في كتاب Excel باستخدام C++ مع Aspose.Cells
linktitle: إنشاء خط توقيع في مصنف إكسل
type: docs
weight: 150
url: /ar/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: تصف هذه المقالة كيفية إنشاء خط توقيع في كتاب Excel باستخدام رموز C++ مع Aspose.Cells for C++.
keywords: إنشاء خط توقيع في سجل عمل Excel، كيفية إنشاء خط توقيع في سجل عمل Excel، كيفية إضافة خط توقيع، كيفية إضافة خط توقيع إلى ملف Excel.
---

## **مقدمة**

توفر Microsoft Excel ميزة إضافة **سطر توقيع** في سجل Excel. يمكنك إضافة سطر توقيع عن طريق النقر فوق علامة **إدراج** ثم تحديد **سطر توقيع** من مجموعة **نص**.

## **كيفية إنشاء خط توقيع لإكسل**

توفر Aspose.Cells أيضًا هذه الميزة وقد عرضت الخاصية [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) لهذا الغرض. سيشرح هذا المقال كيفية استخدام هذه الخاصية لإضافة سطر توقيع باستخدام Aspose.Cells.

الشفرة النموذجية التالية تضيف خط توقيع باستخدام الخاصية [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) وتحفظ ورقة العمل.

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
