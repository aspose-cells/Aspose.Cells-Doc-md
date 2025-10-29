---
title: إلغاء تجميد الصفوف أو الأعمدة في ورقة عمل Excel باستخدام C++
linktitle: إلغاء تجميد الأجزاء
type: docs
weight: 190
url: /ar/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية إلغاء تجميد الصفوف أو الأعمدة أو الألواح في أوراق عمل Excel برمجياً باستخدام API Aspose.Cells for C++.
keywords: إلغاء تجميد الألواح، إلغاء تجميد الصفوف، إلغاء تجميد الأعمدة، إلغاء تجميد النافذة.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية إلغاء تجميد الصفوف والأعمدة والألواح في أوراق عمل Excel. إذا كانت أوراق العمل في ملفات Excel مجمدة، فغالباً ما نرغب في إلغاء تجميد الورقة أو تعديل الصفوف والأعمدة والألواح المجمدة.

## **في إكسل**

1. انقر على علامة التبويب **عرض** > **تجميد الألواح** > **إلغاء تجميد الألواح**.

**![إلغاء تجميد الألواح في إكسل](Unfreeze-Panes.png)**

## **إلغاء تجميد الصفوف، الأعمدة، أو الألواح باستخدام Aspose.Cells for C++**
من السهل إلغاء تجميد الألواح باستخدام Aspose.Cells for C++. استخدم طريقة [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) لإلغاء تجميد الألواح.

1. أنشئ كائن `Workbook` لفتح الملف المجمد.
2. قم بإلغاء تجميد الألواح باستخدام طريقة `Worksheet.UnFreezePanes()`.
3. حفظ الملف.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

المرفق [ملف إكسل عيني](Frozen.xlsx).
{{< app/cells/assistant language="cpp" >}}
