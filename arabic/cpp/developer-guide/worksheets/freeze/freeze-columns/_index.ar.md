---
title: تجميد العمود الأول (الأعمدة الأولى) لورقة عمل إكسل باستخدام ++C
linktitle: تجميد الأعمدة
type: docs
weight: 190
url: /ar/cpp/how-to-freeze-columns-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية تجميد الأعمدة اليسرى من أوراق عمل إكسل برمجياً باستخدام مكتبة C++ مع API Aspose.Cells.
keywords: تجميد الأعمدة اليسرى، تجميد الأعمدة الأولى، قفل العمود/الأعمدة
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية تجميد العمود/الأعمدة اليسرى. عندما يكون لديك كمية هائلة من البيانات في صف، قد لا تتمكن من رؤية الأعمدة اليسرى عند التمرير أفقياً عبر الورقة. يمكنك تجميد وقفل العمود/الأعمدة الأولى بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية رؤوس الأعمدة في الأعمدة اليسرى.

## **تجميد الأعمدة في Excel**

**![تجميد الأعمدة اليسرى في Excel](freeze-columns.png)**

1. إذا أردت تجميد العمود/الأعمدة اليسرى، فابدأ بتحديد العمود تحت العمود الذي يحتاج إلى تجميده.
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر على تجميد العمود الأول.
4. إذا قمت بالتمرير لأسفل، سيكون العمود الأول دائماً في العرض الأيسر.

**![عمود مجمد](frozen-columns.png)**

كما ترى، تم تجميد العمود الأول، ويظل دائماً في أعلى العرض عند التمرير أفقياً.

تمكّن خاصية تجميد الأعمدة من عرض بياناتك الطويلة بدون الحاجة لمتابعة العمود الأول.

## **تجميد الأعمدة باستخدام رقم Aspose.Cells for C++**
من السهل تجميد الأعمدة الأولى باستخدام رقم Aspose.Cells for C++. 
يرجى استخدام طريقة [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) لتجميد الأعمدة عند العمود المحدد.
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.
2. قم بتجميد العمود الأول باستخدام طريقة Worksheet.FreezePanes().
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

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

المرفق [ملف الإكسيل عينة](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
