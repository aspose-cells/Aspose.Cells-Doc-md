---
title: تجميد الصف العلوي (الصفوف) لورقة عمل إكسل باستخدام ++C
linktitle: تجميد الصفوف
type: docs
weight: 190
url: /ar/cpp/how-to-freeze-rows-of-excel-worksheet
description: في هذا المقال، ستتعلم كيف تقوم بتجميد الصفوف العلوية من أوراق عمل إكسل برمجياً باستخدام مكتبة C++ مع API Aspose.Cells.
keywords: تجميد الصفوف العليا، تجميد الصف العلوي.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية تجميد الصف العلوي (الصفوف العلوية). عند وجود كمية هائلة من البيانات تحت عنوان مشترك، قد لا تتمكن من رؤية العنوان عند التمرير لأسفل عبر الورقة. يمكنك تجميد الصفوف العلوية حتى تتمكن من رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية رؤوس الأعمدة في الصفوف العلوية.

## **تجميد الصفوف في إكسل**

**![تجميد الصفوف العلوية في إكسل](Freeze-Rows.png)**

1. إذا أردت تجميد الصف العلوي، فابدأ بتحديد الصف تحت الصف الذي يحتاج إلى تجميده.
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر على تجميد الصف العلوي.
4. إذا قمت بالتمرير لأسفل، سيكون الصف الأول دائماً في أعلى العرض.

**![صف مجمد](Frozen-Row.png)**

كما ترى، تم تجميد الصف الأول، ويظل دائمًا في أعلى العرض عند التمرير لأسفل.

تمكّن خاصية تجميد الصفوف من عرض بياناتك الكبيرة بدون فقدان تتبع تسميات الصف.

## **تجميد الصفوف باستخدام رقم Aspose.Cells for C++**
من السهل تجميد الصفوف باستخدام رقم Aspose.Cells for C++. 
يرجى استخدام طريقة [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) لتجميد الصف عند الصف المحدد.
1. أنشئ مصنفًا لفتح الملف أو أنشئ ملفًا فارغًا.
2. قم بتجميد الصف الأول باستخدام طريقة Worksheet.FreezePanes().
3. حفظ الملف.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

[ملف Excel مصدري عينة مرفق](../Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
