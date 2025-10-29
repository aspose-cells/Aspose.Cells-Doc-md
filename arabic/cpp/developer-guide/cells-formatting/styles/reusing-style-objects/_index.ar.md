---
title: إعادة استخدام كائنات النمط مع C++
linktitle: إعادة استخدام كائنات النمط
description: في Aspose.Cells for C++، يمكنك من خلال إنشاء واستخدام كائنات نمط قابلة لإعادة الاستخدام تبسيط إدارة الأنماط وتحسين كفاءة الكود. ستساعدك دليلاتنا على استغلال مزايا الكائنات النمطية المعاد استخدامها وتنفيذها في تطبيقك.
keywords: Aspose.Cells for C++، إعادة استخدام كائنات النمط، إدارة النمط، كفاءة الكود، أنماط قابلة لإعادة الاستخدام، تطوير التطبيقات، مرجع API، كود نموذجي، تحميل، دعم.
type: docs
weight: 3000
url: /ar/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

يمكن لإعادة استخدام كائنات النمط توفير الذاكرة وجعل البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

نظرًا لأن النهج [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) يستخدم أقل من الذاكرة بكثير، وهو كفء، تمت إزالة خاصية Cell.Style القديمة التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
