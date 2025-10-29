---
title: Spécifiez le nombre maximum de lignes pour une formule partagée avec C++
linktitle: Spécifier le nombre maximum de lignes de formule partagée
type: docs
weight: 40
url: /fr/cpp/specify-maximum-rows-of-shared-formula/
description: Apprenez comment spécifier le nombre maximum de lignes d une formule partagée dans les fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Le nombre maximum par défaut de lignes pour la formule partagée est 64. Il peut être n'importe quel chiffre e.g., 1000. La performance de la formule partagée varie selon le nombre de lignes. Par conséquent, Aspose.Cells fournit la propriété [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) qui peut être utilisée pour spécifier le nombre maximum de lignes. La formule partagée sera divisée en plusieurs formules partagées si le nombre total de lignes dépasse cette valeur, comme illustré dans la capture d'écran suivante.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Spécifier le nombre maximum de lignes de formule partagée**

Le code d'exemple suivant explique l'utilisation de la propriété [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). Il définit le nombre maximum de lignes de la formule partagée à 5 et ajoute la formule partagée dans la cellule D1 pour 100 lignes, puis enregistre dans un fichier Excel [output Excel](61767856.xlsx). Si vous extrayez le contenu du fichier Excel de sortie et vérifiez *sheet1.xml*, vous verrez que la formule partagée se divise toutes les 5 lignes, comme indiqué dans la capture d'écran ci-dessus.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
