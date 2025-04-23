---
title: قص ولصق النطاق باستخدام C++
linktitle: قص ولصق المجموعة
type: docs
weight: 130
url: /ar/cpp/cut-and-paste-cells/
description: تعلم كيفية قص ولصق الخلايا داخل ورقة العمل باستخدام Aspose.Cells for C++.
---

## **قص ولصق الخلايا**

يقدم Aspose.Cells القدرة على قص ولصق الخلايا داخل ورقة العمل باستخدام طريقة [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). تتقبل الطريقة [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) المعلمات التالية:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): مجموعة الخلايا التي سيتم قصها.
- فهرس الصف: فهرس الصف لإدراج الخلايا.
- فهرس العمود: فهرس العمود لإدراج الخلايا.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): اتجاه التحريك للأعمدة.

المثال التالي يوضح كيفية قص ولصق الخلايا داخل ورقة العمل.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(0, 2).SetValue(1);
    worksheet.GetCells().Get(1, 2).SetValue(2);
    worksheet.GetCells().Get(2, 2).SetValue(3);
    worksheet.GetCells().Get(2, 3).SetValue(4);

    Range namedRange = worksheet.GetCells().CreateRange(0, 2, 3, 1);
    namedRange.SetName(u"NamedRange");

    Range cut = worksheet.GetCells().CreateRange(u"C:C");

    worksheet.GetCells().InsertCutCells(cut, 0, 1, ShiftType::Right);

    workbook.Save(outDir + u"CutAndPasteCells.xlsx");

    std::cout << "Cells cut and pasted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
