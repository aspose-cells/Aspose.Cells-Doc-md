---
title: Trouver si la feuille de calcul est une feuille de dialogue avec C++
linktitle: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 90
url: /fr/cpp/find-if-the-worksheet-is-dialog-sheet/
description: Une feuille de dialogue est un ancien format de feuille. Cet article fournit des instructions et un code d exemple pour déterminer de manière programmatique si une feuille de calcul Excel est une feuille de dialogue en utilisant l API C++.
keywords: trouver le type de dialogue de la feuille de calcul excel c++, feuille de dialogue c++
---

## **Scénarios d'utilisation possibles**

La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille peut être insérée par une ancienne version de Microsoft Excel, par exemple 2003 comme le montre cette capture d'écran. Elle peut également être insérée avec VBA dans des versions plus récentes comme Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez déterminer si la feuille est une feuille de dialogue ou un autre type de feuille avec la propriété [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) fournie par Aspose.Cells. Si cela renvoie la valeur d'énumération [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/), cela signifie que vous avez affaire à une feuille de dialogue.

## **Trouver si la Feuille de calcul est une Feuille de dialogue**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716820.xlsx) contenant une feuille de dialogue. Il vérifie la propriété [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/), la compare avec [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) et affiche le message. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
