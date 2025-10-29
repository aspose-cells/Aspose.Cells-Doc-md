---
title: Вырезание и вставка диапазона с помощью C++
linktitle: Вырезать и вставить диапазон
type: docs
weight: 130
url: /ru/cpp/cut-and-paste-cells/
description: Узнайте, как вырезать и вставлять ячейки внутри рабочего листа с помощью Aspose.Cells for C++.
---

## **Вырезать и вставить ячейки**

Aspose.Cells позволяет вам вырезать и вставлять ячейки внутри рабочего листа, используя метод [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) принимает следующие параметры:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): Диапазон ячеек для вырезания.
- Индекс строки: Индекс строки для вставки ячеек.
- Индекс столбца: Индекс столбца для вставки ячеек.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): Направление сдвига столбцов.

В следующем примере показано, как вырезать и вставить ячейки в пределах рабочего листа.

## **Образец кода**

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
{{< app/cells/assistant language="cpp" >}}
