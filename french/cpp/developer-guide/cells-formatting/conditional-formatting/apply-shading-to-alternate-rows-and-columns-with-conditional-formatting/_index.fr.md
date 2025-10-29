---
title: Appliquer un hachurage sur les rangées et colonnes alternées avec le formatage conditionnel en C++
linktitle: Appliquer un hachurage sur les rangées et colonnes alternées
description: Comment utiliser la bibliothèque Aspose.Cells en C++ pour appliquer des ombres de formatage conditionnel aux rangées et colonnes alternées. En ajustant ces critères, vous avez plus de contrôle sur l’aspect des cellules.
keywords: Aspose.Cells, Formatage conditionnel, C++, Rangées alternées, Colonnes alternées, Ombres
type: docs
weight: 30
url: /fr/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Les API Aspose.Cells permettent d’ajouter et de manipuler des règles de formatage conditionnel pour l’objet [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Ces règles peuvent être adaptées de plusieurs manières pour obtenir le format désiré en fonction de conditions ou de règles. Cet article démontrera l’utilisation de l’API Aspose.Cells for C++ pour appliquer un hachurage sur des rangées et colonnes alternées à l’aide de règles de formatage conditionnel et des fonctions intégrées d’Excel.

{{% /alert %}}

Cet article utilise des fonctions intégrées à Excel telles que ROW, COLUMN & MOD. Voici quelques détails sur ces fonctions pour une meilleure compréhension de l'extrait de code fourni ci-après.

- La fonction **ROW()** renvoie le numéro de ligne d'une référence de cellule. Si le paramètre de référence est omis, il suppose que la référence est l'adresse de la cellule dans laquelle la fonction ROW a été saisie.
- La fonction **COLUMN()** renvoie le numéro de colonne d'une référence de cellule. Si le paramètre de référence est omis, il suppose que la référence est l'adresse de la cellule dans laquelle la fonction COLUMN a été saisie.
- La fonction **MOD()** retourne le reste après la division d'un nombre par un diviseur, où le premier paramètre de la fonction est la valeur numérique dont vous souhaitez trouver le reste et le deuxième paramètre est le nombre utilisé pour diviser le paramètre de nombre. Si le diviseur est 0, alors il retournera l'erreur #DIV/0!.

Commençons à écrire du code pour atteindre cet objectif avec l’aide de l’API Aspose.Cells for C++.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

La capture d'écran suivante montre la feuille de calcul résultante chargée dans l'application Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Pour appliquer l'ombrage aux colonnes alternatives, il vous suffit de changer la formule **=MOD(ROW(),2)=0** en **=MOD(COLUMN(),2)=0**, c'est-à-dire; au lieu d'obtenir l'index de ligne, modifier la formule pour récupérer l'index de colonne. 
La feuille de calcul résultante, dans ce cas, ressemblera comme suit.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
