---
title: Supprimer un tableau croisé dynamique d une feuille de calcul avec C++
linktitle: Supprimer le tableau croisé dynamique
type: docs
weight: 60
url: /fr/cpp/delete-pivot-table-from-a-worksheet/
description: Code C++ pour supprimer un tableau croisé dynamique des feuilles Excel en utilisant Aspose.Cells.
keywords: c++ supprimer le tableau croisé dynamique de la feuille, c++ supprimer le tableau croisé dynamique d Excel, comment supprimer un tableau croisé dynamique avec c++, supprimer le tableau croisé dynamique avec c++, supprimer un tableau croisé dynamique d’Excel avec c++, c++ supprimer tableau croisé dynamique, c++ retirer tableau croisé dynamique, retirer tableau croisé dynamique, supprimer tableau croisé dynamique, comment supprimer un tableau croisé dynamique
---

{{% alert color="primary" %}}

Aspose.Cells offre une fonctionnalité pour supprimer ou retirer un tableau croisé dynamique d'une feuille de calcul. Vous pouvez supprimer le tableau croisé dynamique en utilisant l'objet tableau croisé dynamique ou la position du tableau croisé dynamique. Veuillez utiliser la méthode [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) pour supprimer le tableau croisé dynamique en utilisant l'objet tableau croisé dynamique et la méthode [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) pour supprimer l'objet tableau croisé dynamique en utilisant sa position dans la collection de tableaux croisés dynamiques.

{{% /alert %}}

Le code d'exemple suivant supprime deux tableaux croisés dynamiques de la feuille. Il commence par supprimer un tableau croisé dynamique en utilisant la méthode [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) puis en utilise la méthode [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
