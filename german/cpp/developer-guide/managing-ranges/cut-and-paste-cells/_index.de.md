---
title: Bereich zuschneiden und einfügen mit C++
linktitle: Bereich ausschneiden und einfügen
type: docs
weight: 130
url: /de/cpp/cut-and-paste-cells/
description: Lernen Sie, wie Sie Zellen innerhalb eines Arbeitsblatts mit Aspose.Cells for C++ zuschneiden und einfügen.
---

## **Zellen ausschneiden und einfügen**

Aspose.Cells ermöglicht es Ihnen, Zellen innerhalb eines Arbeitsblatts mithilfe der [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/)-Methode der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung auszuschneiden und einzufügen. Die [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/)-Methode akzeptiert die folgenden Parameter:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): Der Bereich von Zellen, die ausgeschnitten werden sollen.
- Zeilenindex: Der Index der Zeile zum Einfügen von Zellen.
- Spaltenindex: Der Index der Spalte zum Einfügen von Zellen.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): Die Verschiebungsrichtung der Spalten.

Das folgende Beispiel zeigt, wie man Zellen innerhalb eines Arbeitsblatts ausschneiden und einfügen kann.

## **Beispielcode**

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
