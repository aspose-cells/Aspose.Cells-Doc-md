---
title: تجميد أجزاء من ورقة عمل إكسل باستخدام C++
linktitle: تجميد الأجزاء
type: docs
weight: 190
url: /ar/cpp/how-to-freeze-panes-of-excel-worksheet
description: في هذه المقالة، ستتعلم كيفية تجميد أجزاء من أوراق عمل إكسل برمجيًا باستخدام مكتبة C++ مع واجهة برمجة تطبيقات Aspose.Cells.
keywords: تجميد الأجزاء، تجميد النافذة.
---

## **مقدمة**

في هذه المقالة، سنتعلم كيف نجمّد الأجزاء. عندما يكون لديك كمية كبيرة من البيانات تحت عنوان مشترك، لا يمكنك رؤية العنوان عند التمرير لأسفل ورقة العمل. ويحتوي كل سجل على العديد من البيانات. يمكنك تجميد الأجزاء بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية الرؤوس في الصفوف العليا أو الأعمدة الأولى. التجميد وفك التجميد للأجزاء يغير فقط عرض البيانات بدون تغيير البيانات نفسها.

## **في إكسل**

**![تجميد الأجزاء في إكسل](Freeze-panes.png)**

1. إذا كنت تريد تجميد الأجزاء، وتجميد الصفوف والأعمدة، فحدد أولاً خلية (مثل B2).
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر على تجميد الأجزاء.
4. إذا قمت بالتمرير لأسفل أو لليمين، فإن الصف الأول والعمود يظل معلقًا.

**![الأجزاء المجمدة](Frozen-Panes.png)**

كما ترى، الصف الأول والعمود A مجمدان، والصف الثاني هو 32، والعمود الثاني المرئي هو D.

تتيح لك خاصية تجميد الأجزاء عرض بياناتك الكبيرة بدون الحاجة إلى تتبع تسميات الصف أو العمود.

## **تجميد الأجزاء مع Aspose.Cells for C++**
من السهل جدًا تجميد الأجزاء باستخدام Aspose.Cells for C++. يرجى استخدام طريقة [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) لتجميد الأجزاء عند الخلية المحددة.
1. أنشئ مصنفًا لفتح الملف أو أنشئ ملفًا فارغًا.
2. قم بتجميد الأجزاء باستخدام طريقة Worksheet.FreezePanes().
3. حفظ الملف.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

المرفق [ملف الإكسيل عينة](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
