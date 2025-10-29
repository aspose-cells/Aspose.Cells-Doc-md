---
title: تنسيق المقطع باستخدام C++
linktitle: تنسيق المنقي
type: docs
weight: 20
url: /ar/cpp/formatting-slicer/
description: تنسيق مقاطع التصفح في Microsoft Excel باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تنسيق مقطع التصفح في Microsoft Excel عن طريق تعيين عدد الأعمدة أو نمطه، إلخ. يسمح لك Aspose.Cells أيضًا بفعل ذلك باستخدام خصائص [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) و [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/).

## **تنسيق المنقي**

يرجى الاطلاع على الكود التالي؛ يقوم بتحميل ملف Excel النموذجي الذي يحتوي على مقطع تصفح. يصل إلى مقطع التصفح ويحدد عدد أعمدته ونوع النمط ويحفظه كملف Excel مخرجات. تُظهر لقطة الشاشة كيف يبدو مقطع التصفح بعد تنفيذ الكود النموذجي.

![todo:image_alt_text](formatting-slicer_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
