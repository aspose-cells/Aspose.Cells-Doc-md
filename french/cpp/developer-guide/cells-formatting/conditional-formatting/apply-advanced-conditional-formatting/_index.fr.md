---
title: Appliquer un formatage conditionnel avancé avec C++
linktitle: Appliquer le formatage conditionnel avancé
description: Comment utiliser la bibliothèque Aspose.Cells en C++ pour appliquer un formatage conditionnel avancé. En ajustant ces critères, vous avez plus de contrôle sur l’apparence des cellules.
keywords: Aspose.Cells, Formatage conditionnel avancé, C++, Conditionnel, Formatage
type: docs
weight: 70
url: /fr/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 et les versions ultérieures (2010/2013/2016) proposent des fonctionnalités avancées pour le formatage conditionnel. Par exemple, il vous permet d'appliquer un ombrage de cellule, des bordures, des icônes colorées, des flèches, des drapeaux et un formatage de police, etc., ce qui est devenu assez sophistiqué.

{{% /alert %}}

## **Appliquer un formatage conditionnel avancé aux fichiers Microsoft Excel**
Le formatage conditionnel peut :

- Ajouter des barres de données ombrées pour améliorer graphiquement les chiffres sous-jacents en intégrant un simple graphique à barres dans les cellules.
- Ombrer automatiquement les cellules avec des échelles de couleurs en fonction de leur relation avec les valeurs des autres cellules de la plage. Les paramètres par défaut ombragent la plus faible valeur en rouge jusqu'à la plus élevée en vert.
- Utiliser des ensembles d'icônes de manière similaire aux échelles de couleurs, mais au lieu d'ombrer les cellules, il ajoute de petites icônes, telles que des flèches et des feux de signalisation, aux cellules.

Aspose.Cells prend en charge pleinement le formatage conditionnel fourni par Microsoft Excel 2007 et les versions ultérieures au format XLSX sur les cellules en cours d'exécution. Cet exemple montre un exercice pour les types de formatage conditionnel avancé, y compris IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom et d'autres règles avec différents ensembles d'attributs.

### **Calculer la couleur choisie par Microsoft Excel pour le formatage conditionnel de l'échelle de couleurs**
Aspose.Cells vous permet de calculer la couleur sélectionnée par Microsoft Excel lorsque le formatage conditionnel de l'échelle de couleurs est utilisé dans un fichier modèle. Consultez le code d'exemple ci-dessous pour apprendre comment calculer la couleur sélectionnée par Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
