---
title: Ajouter des cellules à la fenêtre de surveillance des formules de Microsoft Excel avec C++
linktitle: Ajouter des cellules à la fenêtre de surveillance des formules
description: Apprenez comment utiliser Aspose.Cells for C++ pour ajouter des cellules à la fenêtre de surveillance des formules dans Excel. Chargez ou créez un fichier Excel, manipulez les cellules, définissez des formules et enregistrez le fichier modifié.
keywords: Aspose.Cells, Excel, Fenêtre de surveillance des formules, Cellules, Ajout, C++
type: docs
weight: 60
url: /fr/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Scénarios d'utilisation possibles**

La fenêtre de surveillance d'Excel de Microsoft est un outil pratique permettant de surveiller facilement les valeurs des cellules et leurs formules dans une fenêtre. Vous pouvez ouvrir la *Fenêtre de surveillance* dans Microsoft Excel en cliquant sur *Formules > Fenêtre de surveillance*. Elle possède un bouton *Ajouter une surveillance* qui peut être utilisé pour ajouter des cellules à inspecter. De même, vous pouvez utiliser la méthode [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) pour ajouter des cellules à la *Fenêtre de surveillance* en utilisant l'API Aspose.Cells.

## **Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel**

Le code d'exemple suivant définit la formule des cellules C1 et E1 et les ajoute toutes deux à la fenêtre de surveillance. Il enregistre ensuite le classeur en tant que fichier Excel de sortie (67338481.xlsx). Si vous ouvrez le fichier Excel de sortie et consultez la *Fenêtre de surveillance*, vous verrez les deux cellules comme indiqué dans cette capture d'écran.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
