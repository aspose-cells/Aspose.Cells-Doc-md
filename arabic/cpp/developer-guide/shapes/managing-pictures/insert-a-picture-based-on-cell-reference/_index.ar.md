---
title: إدراج صورة استنادًا إلى مرجع خلية باستخدام C++
linktitle: إدراج صورة بناءً على مرجع الخلية
type: docs
weight: 150
url: /ar/cpp/insert-a-picture-based-on-cell-reference/
description: تعلم كيفية إدراج صورة استنادًا إلى مرجع الخلية باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا يكون لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تحديد إشارة للخلية في شريط الصيغة. تدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).

{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

تدعم Aspose.Cells عرض محتوى خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية أو نطاق الخلية مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها على البيانات في تلك الخلية أو نطاق الخلية تظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل عن طريق استدعاء الطريقة [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) لمجموعة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (المغلفة في كائن [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). حدد نطاق الخلية باستخدام السمة [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) لكائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### مثال على الكود

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
