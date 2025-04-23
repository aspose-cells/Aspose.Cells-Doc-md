---
title: تحويل Smart Art إلى شكل مجموعة باستخدام C++
linktitle: تحويل الرسوم البيانية الذكية إلى شكل مجموعة
type: docs
weight: 200
url: /ar/cpp/convert-the-smart-art-to-group-shape/
description: تعلم كيفية تحويل شكل Smart Art إلى شكل مجموعة باستخدام Aspose.Cells for C++ والوصول إلى أجزاء فردية من مجموعة الأشكال.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحويل شكل الرسوم البيانية الذكية إلى شكل مجموعة باستخدام الطريقة [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/). ستمكنك من التعامل مع شكل رسوم بيانية ذكية مثل شكل مجموعة. وبالتالي، ستكون لديك الوصول إلى الأجزاء أو الأشكال الفردية لشكل المجموعة.

## **تحويل الرسوم البيانية الذكية إلى شكل مجموعة**

الشيفرة النموذجية التالية تقوم بتحميل [ملف إكسل نموذج](55541793.xlsx) الذي يحتوي على شكل فن ذكي كما هو موضح في لقطة الشاشة هذه. ثم تقوم بتحويل شكل الفن الذكي إلى شكل مجموعة وطباعة خاصية Shape::IsGroup. يرجى الاطلاع على مخرجات وحدة التحكم للشيفرة النموذجية المعطاة أدناه.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
