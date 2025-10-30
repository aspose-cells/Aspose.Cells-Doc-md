---
title: Klipp och klistra område med C++
linktitle: Klipp och Klistra Range
type: docs
weight: 130
url: /sv/cpp/cut-and-paste-cells/
description: Lär dig hur man klipper och klistrar celler inom ett kalkylblad med Aspose.Cells for C++.
---

## **Klipp och klistra celler**

Aspose.Cells ger dig möjligheten att klippa och klistra celler inom ett kalkylblad med hjälp av metoden [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) i [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen. Metoden [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) tar emot följande parametrar:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): Området med celler som ska klippas.
- Radindex: Index för raden att infoga celler.
- Kolumnindex: Index för kolumnen att infoga celler.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): Kolumnernas förflyttningsriktning.

Följande exempel visar hur du klipper och klistrar celler inom en arbetsbok.

## **Exempelkod**

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
