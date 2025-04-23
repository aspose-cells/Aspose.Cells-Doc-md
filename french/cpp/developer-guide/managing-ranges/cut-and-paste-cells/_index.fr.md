---
title: Couper et coller une plage avec C++
linktitle: Couper et coller la plage
type: docs
weight: 130
url: /fr/cpp/cut-and-paste-cells/
description: Apprenez comment couper et coller des cellules dans une feuille de calcul en utilisant Aspose.Cells for C++.
---

## **Couper et coller des cellules**

Aspose.Cells vous permet de couper et coller des cellules dans une feuille de calcul en utilisant la méthode [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) accepte les paramètres suivants :

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) : La plage de cellules à couper.
- Index de ligne : L'index de la ligne pour insérer les cellules.
- Index de colonne : L'index de la colonne pour insèrer les cellules.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/) : La direction du décalage des colonnes.

L'exemple suivant montre comment couper et coller des cellules dans une feuille de calcul.

## **Code d'exemple**

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
