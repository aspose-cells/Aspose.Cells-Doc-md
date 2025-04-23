---
title: Utiliser les options de vérification des erreurs avec C++
linktitle: Utiliser les options de vérification des erreurs
type: docs
weight: 140
url: /fr/cpp/use-error-checking-options/
description: Dans cet article, vous trouverez un code d exemple qui utilise de manière programmatique les options de vérification des erreurs des feuilles de calcul Excel, par exemple les nombres stockés en tant que texte, en utilisant l API ou la bibliothèque C++.
keywords: numéro de magasin en tant que texte dans Excel en utilisant C++, vérification des options Excel C++
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de définir des options et des règles de vérification des erreurs. Les utilisateurs voient souvent des vérifications d'erreur lors de la création de formules, un petit triangle en haut à droite d'une cellule met en évidence un problème. Excel fournit des informations pour aider les utilisateurs à corriger les problèmes courants.

{{% /alert %}}

## **Types d'erreurs**

Les erreurs qui signifient que la formule ne peut pas renvoyer un résultat - comme diviser un nombre par zéro - nécessitent une attention immédiate et une valeur d'erreur est affichée dans la cellule. En cliquant sur le triangle vert apparaît un point d'exclamation, en cliquant dessus ouvre une liste d'options.

L'erreur peut être résolue à l'aide des options ou être ignorée. Ignorer une erreur signifie que cette erreur n'apparaîtra pas dans d'autres vérifications d'erreur.

Aspose.Cells fournit des fonctionnalités d'options de vérification des erreurs. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) gère différents types de vérifications d'erreur, par exemple les nombres stockés sous forme de texte, les erreurs de calcul de formule et les erreurs de validation. Utilisez l'énumération [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/) pour définir la vérification d'erreur souhaitée.

## **Nombres stockés sous forme de texte**

Parfois, les nombres peuvent être formatés et stockés dans des cellules sous forme de texte. Cela peut causer des problèmes avec les calculs ou produire des ordres de tri confus. Les nombres formatés comme du texte sont alignés à gauche au lieu de droite dans la cellule. Si une formule qui devrait effectuer une opération mathématique sur des cellules ne renvoie pas de valeur, vérifiez l'alignement dans les cellules auxquelles la formule se réfère, certaines ou toutes ces cellules pourraient être des nombres formatés comme du texte.

Vous pouvez utiliser les options de vérification des erreurs pour convertir rapidement les nombres stockés sous forme de texte en nombres réels. Dans Microsoft Excel 2003 :

1. Dans le menu **Outils**, cliquez sur **Options**.
1. Sélectionnez l'onglet Vérification des erreurs.
   L'option **Nombre stocké comme texte** est activée par défaut.
1. Désactivez-la.

Le code d'exemple suivant montre comment désactiver l'option de vérification des erreurs pour les nombres stockés sous forme de texte pour une feuille de calcul dans le fichier XLS modèle à l'aide des API Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
