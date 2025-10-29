--- 
title: Comment vérifier l’état de verrouillage sans Excel avec C++ 
linktitle: État figé 
type: docs 
weight: 190 
url: /fr/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: Dans cet article, vous apprendrez comment vérifier l’état de gel d’une feuille de calcul Excel de manière programmatique en utilisant C++ avec l’API Aspose.Cells. 
--- 

## **Introduction** 

Dans cet article, nous apprendrons comment vérifier l’état de gel d’une feuille de calcul Excel de manière programmatique. Nous pouvons simplement déterminer si la feuille de calcul est gelée ou divisée dans MS Excel. Mais existe-t-il une méthode pour savoir si elle est gelée ou divisée avec C++ ? Nous pouvons le faire avec Aspose.Cells for C++. 

## **Les volets de fenêtre sont-ils gelés** 
Avec Aspose.Cells for C++, nous pouvons vérifier si la fenêtre est verrouillée et combien de lignes et colonnes sont bloquées. 

Veuillez utiliser la propriété [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) pour vérifier l’état des volets de la fenêtre et obtenir les lignes et colonnes verrouillées avec la méthode [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/). 
1. Construisez un classeur pour ouvrir le fichier. 
2. Vérifiez si la feuille de calcul est gelée. 
3. Obtenez les lignes et colonnes verrouillées. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

{{< app/cells/assistant language="cpp" >}}
