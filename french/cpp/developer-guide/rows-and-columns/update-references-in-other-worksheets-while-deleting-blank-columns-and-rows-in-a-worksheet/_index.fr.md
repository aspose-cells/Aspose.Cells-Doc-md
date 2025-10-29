---
title: Mettre à jour les références dans d autres feuilles tout en supprimant les colonnes et lignes vides dans une feuille avec C++
linktitle: Mettre à jour les références dans d autres feuilles
type: docs
weight: 5000
url: /fr/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Apprenez comment mettre à jour les références dans d autres feuilles tout en supprimant les colonnes et lignes vides dans une feuille en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Lorsque vous supprimez des colonnes et lignes vides dans une feuille, ses références dans d'autres feuilles deviennent invalides. Si vous souhaitez éviter ce comportement et vous assurer que les références à la feuille en cours dans d'autres feuilles sont également mises à jour, utilisez la propriété [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) et définissez-la sur **true**.

{{% /alert %}}

## **Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul**

Veuillez voir le code d'exemple suivant et sa sortie console. La cellule E3 dans la deuxième feuille contient une formule `=Sheet1!C3`, qui fait référence à la cellule C3 dans la première feuille. Si vous définissez la propriété [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) sur **true**, cette formule sera mise à jour en `=Sheet1!A1` après avoir supprimé les colonnes et lignes vides dans la première feuille. Cependant, si vous définissez la propriété [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) sur **false**, la formule dans la cellule E3 de la deuxième feuille restera `=Sheet1!C3` et deviendra invalide.

### **Exemple de programmation**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Add second sheet with name Sheet2
    wb.GetWorksheets().Add(u"Sheet2");

    // Access first sheet and add some integer value in cell C1
    // Also add some value in any cell to increase the number of blank rows and columns
    Worksheet sht1 = wb.GetWorksheets().Get(0);
    sht1.GetCells().Get(u"C1").PutValue(4);
    sht1.GetCells().Get(u"K30").PutValue(4);

    // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
    Worksheet sht2 = wb.GetWorksheets().Get(1);
    sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
    std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
    DeleteOptions opts;
    opts.SetUpdateReference(true);

    // Delete all blank rows and columns with delete options
    sht1.GetCells().DeleteBlankColumns(opts);
    sht1.GetCells().DeleteBlankRows(opts);

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsque la propriété [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) est définie sur **true**.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4

{{< /highlight >}}

Voici la sortie console du code d'exemple ci-dessus lorsque la propriété [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) est définie sur **false**. Comme vous pouvez le voir, la formule dans la cellule E3 de la deuxième feuille n'est pas mise à jour, et sa valeur de cellule est maintenant 0 au lieu de 4, ce qui est invalide.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
