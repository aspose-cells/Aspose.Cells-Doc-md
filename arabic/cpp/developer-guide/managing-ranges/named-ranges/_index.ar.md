---
title: إنشاء مجلد عمل وورق عمل مجالي الأسماء باستخدام C++
linktitle: النطاق المسمى
type: docs
weight: 40
url: /ar/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: تعلم إنشاء نطاقات أسماء مجدية على مستوى دفتر العمل وورقة العمل باستخدام C++ باستخدام Aspose.Cells.
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بتحديد مجالات مسماة بنطاقين مختلفين: نطاق العمل (المعروف أيضا باسم نطاق عالمي) ونطاق الورقة العمل.

- يمكن الوصول إلى مجالات مسماة ذات نطاق العمل من أي ورقة عمل ضمن هذا المصنف ببساطة عن طريق استخدام اسمها.
- تتم الوصول إلى مجالات المسميات ذات نطاق ورقة العمل باستخدام مرجع لورقة العمل المعينة التي تم إنشاء المسمى فيها.

يوفر Aspose.Cells نفس الوظائف كما في Microsoft Excel لإضافة نطاقات مسماة في نطاق كتيب أو ورق العمل. عند إنشاء نطاق بتسمية نطاق ورق العمل، يجب استخدام مرجع ورق العمل في النطاق المسمى لتحديده كنطاق مسمى بنطاق ورق العمل.

{{% /alert %}} 

## **إضافة نطاق مسمى بنطاق سجل العمل**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إضافة نطاق مسمى بنطاق ورق العمل**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إنشاء الوصول ونسخ نطاقات مسماة](/cells/ar/cpp/create-access-and-copy-named-ranges/)
- [تنسيق وتعديل نطاقات مسماة](/cells/ar/cpp/format-and-modify-named-ranges/)
- [الحصول على نطاق مع روابط خارجية](/cells/ar/cpp/get-range-with-external-links/)
- [تنفيذ نطاقات غير متتابعة](/cells/ar/cpp/implementing-non-sequential-ranges/)

