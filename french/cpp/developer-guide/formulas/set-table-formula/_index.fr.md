---
title: Propagation automatique des formules dans un tableau ou un objet liste lors de la saisie de nouvelles lignes avec C++
linktitle: Définit la formule de tableau
type: docs
weight: 260
url: /fr/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Apprenez comment propager automatiquement les formules dans les tableaux ou objets liste lors de la saisie de nouvelles données en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez qu'une formule dans votre tableau ou objet liste se propage automatiquement dans de nouvelles lignes lors de la saisie de nouvelles données. C'est le comportement par défaut de Microsoft Excel. Pour obtenir la même fonctionnalité avec Aspose.Cells, utilisez la méthode [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/)

## **Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes**
Le code d'exemple suivant crée un tableau ou objet de liste de manière à ce que la formule dans la colonne B se propage automatiquement aux nouvelles lignes lorsque vous saisissez de nouvelles données. Veuillez vérifier le [fichier Excel généré](5115469.xlsx) avec ce code. Si vous entrez un quelconque chiffre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.

```c++
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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
