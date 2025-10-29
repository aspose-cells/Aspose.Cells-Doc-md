---
title: Insérer ou supprimer des lignes dans une feuille de calcul Excel avec C++
linktitle: Insérer ou supprimer des lignes
type: docs
weight: 20
url: /fr/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Cet article fournit le code C++ pour insérer et supprimer des lignes dans une feuille de calcul Excel.
keywords: insérer ou supprimer des lignes dans une feuille de calcul Excel en C++, insérer ou supprimer des lignes dans Excel en C++, insérer des lignes dans Excel en C++, supprimer des lignes dans Excel en C++, insérer ou supprimer des lignes dans une feuille de calcul Excel avec C++, insérer ou supprimer des lignes dans Excel avec C++, insérer des lignes dans Excel avec C++, supprimer des lignes dans Excel avec C++
---

{{% alert color="primary" %}}

Lors de la création d'une nouvelle feuille de calcul ou du travail avec une feuille de calcul existante, vous pourriez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir des données. À d'autres moments, vous pourriez avoir besoin de supprimer des lignes ou des colonnes à des positions spécifiées dans la feuille de calcul.

{{% /alert %}}

Aspose.Cells offre deux méthodes pour insérer et supprimer des lignes : [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) et [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Ces méthodes sont optimisées pour les performances et font le travail très rapidement.

Pour insérer ou supprimer un certain nombre de lignes, nous vous recommandons d'utiliser toujours les méthodes [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) et [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) au lieu d'utiliser les méthodes [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) ou [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) dans une boucle.

Aspose.Cells fonctionne de la même manière que Microsoft Excel. Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est déplacé vers le bas et vers la droite. Lorsque des lignes ou des colonnes sont supprimées, le contenu de la feuille de calcul est déplacé vers le haut ou vers la gauche. Toutes les références dans les autres feuilles de calcul et cellules sont mises à jour lorsque des lignes sont ajoutées ou supprimées.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
