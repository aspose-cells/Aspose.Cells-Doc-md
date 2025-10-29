---
title: حذف النطاقات المسماة باستخدام C++
linktitle: حذف المدى المسمى
type: docs
weight: 90
url: /ar/cpp/delete-named-ranges/
description: تعلم كيفية إزالة الأسماء المعرفة أو النطاقات المسماة من ملفات Excel أو OpenOffice باستخدام Aspose.Cells for C++.
---

## **مقدمة**
إذا كان هناك الكثير من الأسماء المحددة أو النطاقات المسماة في ملفات Excel، يجب علينا مسح بعضها لأنها لم يتم الرجوع إليها مرة أخرى.

## **إزالة النطاق المسمى في MS Excel**

لإزالة نطاق مسمى من Excel، يمكنك اتباع هذه الخطوات:
1. افتح Microsoft Excel وافتح المصنف الذي يحتوي على النطاق المسمى.
2. انتقل إلى علامة "الصيغ" في شريط أدوات Excel.
3. انقر على زر "مدير الأسماء" في مجموعة "الأسماء المحددة". سيفتح ذلك صندوق حوار مدير الأسماء.
4. في صندوق حوار مدير الأسماء، حدد النطاق المسمى الذي تريد إزالته.
5. انقر على الزر "حذف". قم بتأكيد الحذف عندما يُطلب.
6. انقر على الزر "إغلاق" لإغلاق صندوق حوار مدير الأسماء.
7. احفظ المصنف للحفاظ على التغييرات.

## **حذف النطاق المسمي باستخدام Aspose.Cells for C++**
 مع Aspose.Cells for C++، يمكنك إزالة النطاقات المسماة أو الأسماء المعرفة عن طريق [نص](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/) أو [فهرس](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) في القائمة.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

ملاحظة: إذا تم الإشارة إلى الاسم المعرف بواسطة الصيغ، لا يمكن إزالته. يمكننا فقط إزالة صيغة الاسم المعرف.

## **إزالة بعض النطاقات المسماة**
عندما نقوم بإزالة اسم محدد، يجب علينا التحقق مما إذا كانت تتم الرجوع إليه في جميع الصيغ في الملف.
لتحسين أداء إزالة النطاقات المسماة، يمكننا إزالتها معًا.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إزالة الأسماء المحددة المكررة**
تصاب بعض ملفات Excel بالضرر بسبب تكرار الأسماء المعرفة. لذلك، يمكننا إزالة الأسماء المكررة لإصلاح الملف.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
