---
title: تقسيم الشاشة لورقة عمل Excel باستخدام C++
linktitle: شاشة مقسمة
type: docs
weight: 190
url: /ar/cpp/how-to-split-screen-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية عرض صفوف و/أو أعمدة معينة في ألواح منفصلة عن طريق تقسيم ورقة العمل إلى جزأين أو أربعة أجزاء برمجياً باستخدام C++.
keywords: تجميد الصفوف العليا، تجميد الصف العلوي.
---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية عرض صفوف و/أو أعمدة معينة في ألواح منفصلة عن طريق تقسيم ورقة العمل إلى جزأين أو أربعة أجزاء. عند العمل مع مجموعات البيانات الكبيرة، نحتاج إلى رؤية مناطق معينة من نفس ورقة العمل في وقت واحد للمقارنة بين مجموعات البيانات المختلفة. يمكن أن تلبي وظيفة تقسيم الشاشة احتياجاتك.

## **كيفية تقسيم الشاشة في إكسيل**
لتقسيم ورقة عمل إلى جزئين أو أربعة أجزاء، اتبع الخطوات التالية:

1. حدد الصف / العمود / الخلية قبل المكان الذي تريد وضع التقسيم فيه.
2. على علامة التبويب عرض، في مجموعة النوافذ، انقر فوق زر التقسيم.

**![شاشة مقسمة](Split-Screen.png)**

## **تقسيم ورقة العمل عمودياً على الأعمدة**

لفصل منطقتين في جدول البيانات بشكل عمودي، حدد العمود إلى اليمين من العمود الذي ترغب في ظهور التقسيم فيه، ثم انقر فوق زر التقسيم في Excel.

من السهل تقسيم ورقة العمل عمودياً على الأعمدة برمجياً باستخدام Aspose.Cells for C++، كل ما نحتاجه هو اختيار خلية واحدة في الصف العلوي كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تقسيم ورقة العمل أفقياً على الصفوف**
لفصل نافذة Excel أفقياً، حدد الصف أسفل الصف الذي ترغب في ظهور التقسيم فيه في Excel.

من السهل تقسيم ورقة العمل أفقياً على الصفوف برمجياً باستخدام Aspose.Cells for C++، كل ما نحتاجه هو اختيار خلية واحدة في العمود الأيسر كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تقسيم ورقة العمل إلى أربعة أجزاء**
لعرض أربعة أقسام مختلفة من نفس ورقة البيانات بشكل متزامن، قم بتقسيم الشاشة الخاصة بك عمودياً وأفقياً في Excel.

من السهل تقسيم ورقة العمل عمودياً على الأعمدة برمجياً باستخدام Aspose.Cells for C++، كل ما نحتاجه هو اختيار خلية واحدة غير في الصف والعمود الأول كخلية نشطة، ثم
تقسيم باستخدام الطريقة [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **كيفية إزالة التقسيم**
لإزالة تقسيم ورقة العمل، فقط انقر مرة أخرى فوق زر التقسيم.

يوفر Aspose.Cells for C++ طريقة [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) لإزالة إعدادات التقسيم.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
