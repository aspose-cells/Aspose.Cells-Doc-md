---
title: Appliquer un formatage conditionnel dans les feuilles de calcul avec C++
linktitle: Appliquer un formatage conditionnel
description: Comment utiliser la bibliothèque Aspose.Cells en C++ pour appliquer un formatage conditionnel dans les feuilles de calcul. En ajustant ces critères, vous avez plus de contrôle sur l’aspect des cellules.
keywords: Aspose.Cells, Formatage conditionnel, C++, Feuille, Formatage
type: docs
weight: 130
url: /fr/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de comment ajouter un formatage conditionnel à une plage de cellules dans une feuille de calcul.

Le formatage conditionnel est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une plage de cellules et d'avoir ce formatage modifié en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte pourrait être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de formatage, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de formatage, le formatage par défaut de la cellule est utilisé.

Il est possible d'appliquer un formatage conditionnel avec l'automatisation Microsoft Office, mais cela présente des inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse. La principale raison de trouver une autre solution est que Microsoft recommande fortement de ne pas utiliser l'automatisation Office pour les solutions logicielles.

Cet article montre comment créer une application console, ajouter un formatage conditionnel sur des cellules avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour Appliquer un Formatage Conditionnel Basé sur la Valeur de la Cellule**

1. **Téléchargez et Installez Aspose.Cells**.
   1. Téléchargez Aspose.Cells for C++.
1. Installez-le sur votre ordinateur de développement.
   Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.
1. **Créer un projet**.
   Démarrez votre environnement de développement C++ et créez une nouvelle application console.
1. **Ajouter des références**.
   Ajoutez une référence à Aspose.Cells à votre projet, par exemple ajoutez une référence à ....\ Program Files\ Aspose\ Aspose.Cells\ Bin\ Net1.0\ Aspose.Cells.dll
1. ** Appliquer une mise en forme conditionnelle en fonction de la valeur de la cellule **.
   Voici le code utilisé pour réaliser la tâche. Il applique un formatage conditionnel sur une cellule.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Lorsque le code ci-dessus est exécuté, le formatage conditionnel est appliqué à la cellule “A1” de la première feuille du fichier de sortie (output.xls). Le formatage conditionnel appliqué à A1 dépend de la valeur de la cellule. Si la valeur d’A1 est comprise entre 50 et 100, la couleur de fond est rouge en raison du formatage conditionnel appliqué.

## **Utilisation d'Aspose.Cells pour appliquer une mise en forme conditionnelle en fonction de la formule**

1. **Application du formatage conditionnel selon la formule (Extrait de code)**
   Voici le code pour accomplir la tâche. Il applique une mise en forme conditionnelle sur B3.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Lorsque le code ci-dessus est exécuté, le formatage conditionnel est appliqué à la cellule “B3” de la première feuille du fichier de sortie (output.xls). Le formatage dépend de la formule qui calcule la valeur de “B3” comme la somme de B1 et B2.
