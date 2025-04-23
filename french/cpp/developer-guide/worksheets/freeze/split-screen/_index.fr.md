---
title: Division de l’écran de la feuille de calcul Excel avec C++
linktitle: Écran scindé
type: docs
weight: 190
url: /fr/cpp/how-to-split-screen-of-excel-worksheet
description: Dans cet article, vous apprendrez comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties de manière programmatique à l’aide de C++.
keywords: Figer les premières lignes, Figer la première ligne.
---

## **Introduction**

Dans cet article, nous apprendrons comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties. Lorsqu'on travaille avec de grands ensembles de données, il est nécessaire de voir quelques zones de la même feuille à la fois pour comparer différents sous-ensembles de données. La fonction de division d’écran peut répondre à vos besoins.

## **Comment scinder l'écran dans Excel**
Pour diviser une feuille de calcul en deux ou quatre parties, procédez comme suit :

1. Sélectionnez la ligne/colonne/cellule avant laquelle vous souhaitez placer la division.
2. Sur l'onglet Affichage, dans le groupe Fenêtres, cliquez sur le bouton Fractionner.

**![Écran partagé](Split-Screen.png)**

## **Fractionner la feuille de calcul verticalement sur les colonnes**

Pour séparer deux zones de la feuille de calcul verticalement, sélectionnez la colonne à droite de la colonne où vous souhaitez afficher la division et cliquez sur le bouton Fractionner dans Excel.

Il est facile de diviser la feuille de calcul verticalement en colonnes de manière programmée avec Aspose.Cells for C++, il suffit de sélectionner une cellule dans la ligne du haut comme cellule active, puis
fractionner avec la méthode [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Fractionner la feuille de calcul horizontalement sur les lignes**
Pour séparer votre fenêtre Excel horizontalement, sélectionnez la ligne en dessous de la ligne où vous souhaitez que la division se produise dans Excel.

Il est facile de diviser la feuille de calcul horizontalement en lignes de manière programmée avec Aspose.Cells for C++, il suffit de sélectionner une cellule dans la colonne de gauche comme cellule active, puis
fractionner avec la méthode [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Fractionner la feuille de calcul en quatre parties**
Pour afficher quatre sections différentes de la même feuille de calcul simultanément, divisez votre écran à la fois verticalement et horizontalement dans Excel.

Il est facile de diviser la feuille de calcul verticalement en colonnes de manière programmée avec Aspose.Cells for C++, il suffit de sélectionner une cellule qui n’est pas dans la première ligne et la première colonne comme cellule active, puis
fractionner avec la méthode [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **Comment supprimer la division**
Pour supprimer la division de la feuille de calcul, il suffit de cliquer à nouveau sur le bouton Fractionner.

Aspose.Cells for C++ fournit une méthode [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) pour supprimer la configuration de division.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
