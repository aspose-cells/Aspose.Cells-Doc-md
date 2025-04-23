---
title: Définir la couleur de l onglet de la feuille avec C++
linktitle: Définir la couleur de l onglet de la feuille de calcul
type: docs
weight: 120
url: /fr/cpp/set-worksheet-tab-color/
description: Cet article démontre un code exemple qui définit la couleur de l onglet de la feuille Excel de manière programmatique en utilisant l API ou la bibliothèque C++.
keywords: définir la couleur de l onglet Excel c++, code pour définir la couleur de l onglet Excel c++,
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de changer la couleur des onglets de feuille de calcul individuels pour les rendre plus visibles par rapport au reste. Par exemple, vous pouvez mettre Dépenses en rouge, Ventes en vert, Actifs en bleu, etc.

{{% /alert %}}

## **Définition de la couleur de l'onglet de feuille de calcul avec Microsoft Excel**
1. Cliquez avec le bouton droit sur un onglet dans la feuille d'onglets en bas de la feuille de calcul actuelle.
1. Sélectionnez **Couleur d'onglet**.
1. Sélectionnez une couleur dans la palette.
1. Cliquez sur **OK**.

## **Définir la couleur de l'onglet de la feuille de calcul avec Aspose.Cells**
Le code d'exemple ci-dessous montre comment définir la couleur de l'onglet avec Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
