---
title: ابحث عما إذا كانت ورقة العمل هي ورقة حوار باستخدام C++
linktitle: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 90
url: /ar/cpp/find-if-the-worksheet-is-dialog-sheet/
description: ورقة الحوار هي تنسيق قديم للورقة. تقدم هذه المقالة تعليمات وكود نمونه لتحديد برمجيًا ما إذا كانت ورقة عمل إكسل هي ورقة حوار باستخدام واجهة برمجة التطبيقات C++.
keywords: ابحث عن نوع ورقة إكسل حوار C++، ورقة حوار C++
---

## **سيناريوهات الاستخدام المحتملة**

ورقة الحوار هي صيغة قديمة من الورقة تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة من قبل إصدار أقدم من Microsoft Excel مثل الإصدار 2003 كما هو موضح في هذه الصورة. يمكن أيضاً إدراجها باستخدام VBA في الإصدارات الأحدث مثل Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة إذا كانت الورقة ورقة حوار أو نوع آخر من الأوراق باستخدام الخاصية [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) التي توفرها Aspose.Cells. إذا عادت قيمة التعداد [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) فهذا يعني أنك تتعامل مع ورقة حوار.

## **العثور على ورقة العمل هل هي ورقة حوار**

يقوم الكود النموذجي التالي بتحميل [ملف إكسل النموذجي](64716820.xlsx) الذي يحتوي على ورقة حوار. يتحقق من الخاصية [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) ويقارنها مع [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) ثم يطبع الرسالة. يرجى الاطلاع على ناتج وحدة التحكم للكود النموذجي أدناه للمزيد من المساعدة.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
