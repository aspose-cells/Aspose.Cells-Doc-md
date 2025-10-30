---
title: Taglia e incolla intervallo con C++
linktitle: Taglia e Incolla Intervallo
type: docs
weight: 130
url: /it/cpp/cut-and-paste-cells/
description: Impara come tagliare e incollare celle all’interno di un foglio di lavoro usando Aspose.Cells for C++.
---

## **Taglia e Incolla Celle**

Aspose.Cells ti permette di tagliare e incollare celle all’interno di un foglio di lavoro usando il metodo [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) della collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) accetta i seguenti parametri:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): L'intervallo di celle da tagliare.
- Indice riga: L'indice della riga in cui inserire le celle.
- Indice colonna: L'indice della colonna in cui inserire le celle.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): La direzione di spostamento delle colonne.

L'esempio seguente mostra come tagliare e incollare celle all'interno di un foglio di lavoro.

## **Codice di Esempio**

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
