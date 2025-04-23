---
title: الكشف عن الخلايا المدمجة في ورقة عمل باستخدام C++
linktitle: اكتشاف الخلايا المدمجة
description: مكتبة Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات. تدعم الكشف عن الخلايا المندمجة في ورقة العمل، مما يسهل على المستخدمين تحديد هذه الخلايا ومعالجتها. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لاكتشاف الخلايا المدمجة.
keywords: Aspose.Cells، ورقة العمل، دمج الخلايا، كشف، تحديد، تشغيل
type: docs
weight: 80
url: /ar/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

يوفر هذا المقال معلومات حول كيفية الحصول على مناطق الخلايا المدمجة في ورقة العمل.

تسمح Aspose.Cells لك بالحصول على مناطق الخلايا المدمجة في ورقة العمل. يمكنك أيضًا فصلها (تقسيمها). يعرض هذا المقال الكود الأبسط باستخدام API الخلايا الذي يسمح بأداء المهمة.

{{% /alert %}}

يوفر المكون طريقة [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) التي يمكنها الحصول على جميع الخلايا المدمجة. يظهر لك نموذج الشفرة التالي كيفية اكتشاف الخلايا المدمجة في ورقة العمل.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
