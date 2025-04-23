---
title: دمج أو إلغاء دمج نطاق الخلايا باستخدام C++
linktitle: دمج أو إلغاء دمج مجموعة من الخلايا
type: docs
weight: 190
url: /ar/cpp/merge-or-unmerge-range-of-cells/
description: دمج وإلغاء دمج الخلايا في نطاق في Excel باستخدام كود C++.
keywords: دمج وإلغاء دمج الخلايا في نطاق باستخدام C++، دمج وإلغاء دمج الخلايا في النطاق باستخدام C++، دمج وإلغاء دمج الخلايا في النطاق مع C++، دمج وإلغاء دمج الخلايا في النطاق باستخدام C++، دمج وإلغاء دمج خلايا Excel باستخدام C++, دمج خلايا C++ في Excel، إلغاء دمج خلايا C++ في Excel، دمج خلايا في النطاق باستخدام C++
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لدمج أو تقسيم مجموعة من الخلايا. يوفر Aspose.Cells الأساليب [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) و [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) لهذا الغرض. يشرح هذا المقال كيفية دمج مجموعة من الخلايا في خلية واحدة.

{{% /alert %}}

## **مثال**

يعرض الكود النموذجي التالي أولاً إنشاء نطاق - A1:D4 - ثم دمج الخلايا في النطاق إلى خلية واحدة باستخدام الطريقة [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/). بالمثل، يمكنك تقسيم الخلايا عن طريق إنشاء نطاق واستدعاء الطريقة [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
