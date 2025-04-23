---
title: Utilisez la propriété Sheet.SheetId d OpenXml avec C++
linktitle: Utilisez la propriété Sheet.SheetId d OpenXml
type: docs
weight: 200
url: /fr/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Cet article montre comment utiliser la propriété Sheet.SheetId d OpenXml en utilisant l API ou la bibliothèque de manipulation Excel en C++ de manière programmatique.
keywords: propriété de l id de feuille openxml c++, feuille id excel worksheet c++
---

## **Scénarios d'utilisation possibles**

La propriété *Sheet.SheetId* se trouve dans l'espace de noms *DocumentFormat.OpenXml.Spreadsheet* et fait partie d'OpenXml. Vous pouvez voir cette propriété et sa valeur à l'intérieur de *workbook.xml* comme le montre la capture d'écran suivante. Aspose.Cells fournit la propriété équivalente comme [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells**

Le code d'exemple suivant charge le [fichier Excel d'exemple](51740716.xlsx), lit son ID de feuille ou de tabulation, lui attribue un nouvel ID de tabulation et le sauvegarde en tant que [fichier Excel de sortie](51740717.xlsx). Veuillez également consulter la sortie de la console du code donné ci-dessous à titre de référence.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Sortie console**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
