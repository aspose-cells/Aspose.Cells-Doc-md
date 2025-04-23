---
title: تحديد ما إذا كان الشكل هو شكل فن ذكي باستخدام C++
linktitle: تحديد ما إذا كانت الشكل شكل رسوم بيانية ذكية
type: docs
weight: 400
url: /ar/cpp/determine-if-shape-is-smart-art-shape/
description: تعلم كيفية تحديد ما إذا كان الشكل هو شكل فن ذكي باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

الأشكال الفنية الذكية هي أشكال خاصة في ميكروسوفت إكسل تسمح لك بإنشاء رسوم بيانية معقدة تلقائيًا. يمكنك التحقق مما إذا كان الشكل هو شكل فن ذكي أو شكل عادي باستخدام [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/).

## **تحديد ما إذا كان الشكل هو شكل ذكاء ذكي**

الرمز العيني التالي يحمل [ملف إكسل عيني](55541792.xlsx) الذي يحتوي على شكل فني رائع كما هو موضح في هذه اللقطة. ثم يطبع قيمة [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) للشكل الأول. يرجى الاطلاع على إخراج وحدة التحكم للرمز العيني الوارد أدناه.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
