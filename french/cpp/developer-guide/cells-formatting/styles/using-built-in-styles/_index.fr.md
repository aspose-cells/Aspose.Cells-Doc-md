---
title: Utilisation des styles intégrés avec C++
linktitle: Utilisation de styles intégrés
type: docs
weight: 80
url: /fr/cpp/using-built-in-styles/
description: Code C++ pour utiliser les styles intégrés d’Excel avec l’API Aspose.Cells for C++
keywords: c++ utiliser les styles intégrés d’Excel, c++ appliquer des styles de manière programmatique dans le classeur, appliquer des styles dans le classeur de manière programmatique, c++ appliquer les styles intégrés dans Excel, c++ appliquer les styles intégrés dans le classeur, c++ code pour appliquer les styles intégrés dans le classeur, c++ code pour appliquer les styles intégrés dans le classeur Excel
---

{{% alert color="primary" %}}

Aspose.Cells fournit une vaste collection de styles réutilisables pour formater une cellule dans un document de feuille de calcul. Nous pouvons utiliser des styles intégrés dans notre classeur et également créer des styles personnalisés.

{{% /alert %}}

## **Comment utiliser les styles intégrés**

La méthode [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) et l'énumération [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) rendent pratique l'utilisation des styles intégrés. Voici une liste de tous les styles intégrés possibles:

- VINGT_POURCENT_ACCENT_1
- VINGT_POURCENT_ACCENT_2
- VINGT_POURCENT_ACCENT_3
- VINGT_POURCENT_ACCENT_4
- VINGT_POURCENT_ACCENT_5
- VINGT_POURCENT_ACCENT_6
- QUARANTE_POURCENT_ACCENT_1
- QUARANTE_POURCENT_ACCENT_2
- QUARANTE_POURCENT_ACCENT_3
- QUARANTE_POURCENT_ACCENT_4
- QUARANTE_POURCENT_ACCENT_5
- QUARANTE_POURCENT_ACCENT_6
- SOIXANTE_POURCENT_ACCENT_1
- SOIXANTE_POURCENT_ACCENT_2
- SOIXANTE_POURCENT_ACCENT_3
- SOIXANTE_PERCENT_ACCENT_4
- SOIXANTE_PERCENT_ACCENT_5
- SOIXANTE_PERCENT_ACCENT_6
- ACCENT_1
- ACCENT_2
- ACCENT_3
- ACCENT_4
- ACCENT_5
- ACCENT_6
- MAUVAIS
- CALCUL
- VÉRIFIER_CELLULE
- VIRGULE
- VIRGULE_1
- DEVISE
- DEVISE_1
- TEXTE_EXPOLICATIF
- BIEN
- EN-TÊTE_1
- EN-TÊTE_2
- TITRE_3
- TITRE_4
- HYPERLINK
- LIEN_HYPERTEXTUEL_SUIVI
- SAISIE
- CELLULE_LIEE
- NEUTRE
- NORMAL
- NOTE
- SORTIE
- POURCENTAGE
- TITRE
- TOTAL
- TEXTE_AVERTISSEMENT
- NIVEAU_LIGNE
- NIVEAU_COLONNE

## Code C++ pour utiliser les styles intégrés

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
