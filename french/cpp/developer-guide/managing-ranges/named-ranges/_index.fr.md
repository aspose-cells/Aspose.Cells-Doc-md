---
title: Créer un classeur et des plages nommées avec C++
linktitle: Plage nommée
type: docs
weight: 40
url: /fr/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Apprenez à créer des plages nommées avec portée de classeur et de feuille de calcul avec C++ en utilisant Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux portées différentes : le classeur (également appelé portée globale) et la feuille de calcul.

- Les plages nommées avec une portée de classeur peuvent être accédées à partir de n'importe quelle feuille de calcul au sein de ce classeur en utilisant simplement son nom.
- Les plages nommées avec une portée de feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elle a été créée.

Aspose.Cells fournit la même fonctionnalité que Microsoft Excel pour ajouter des plages nommées au niveau du classeur et de la feuille de calcul. Lors de la création d'une plage nommée au niveau de la feuille de calcul, la référence à la feuille de calcul doit être utilisée dans la plage nommée pour la spécifier comme une plage nommée au niveau de la feuille de calcul.

{{% /alert %}} 

## **Ajout d'une plage nommée au niveau du classeur**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ajout d'une plage nommée avec une portée de feuille de calcul**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Créer un accès et copier des plages nommées](/cells/fr/cpp/create-access-and-copy-named-ranges/)
- [Formater et modifier des plages nommées](/cells/fr/cpp/format-and-modify-named-ranges/)
- [Obtenir une plage avec des liens externes](/cells/fr/cpp/get-range-with-external-links/)
- [Mise en œuvre de plages non séquentielles](/cells/fr/cpp/implementing-non-sequential-ranges/)

{{< app/cells/assistant language="cpp" >}}
