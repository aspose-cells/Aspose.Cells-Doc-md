---
title: Réutilisation des objets de style avec C++
linktitle: Réutilisation d objets de style
description: Dans Aspose.Cells for C++, en créant et en utilisant des objets de style réutilisables, vous pouvez simplifier la gestion des styles et améliorer l efficacité du code. Notre guide vous aidera à exploiter les avantages des objets de style réutilisables et à les implémenter dans votre application.
keywords: Aspose.Cells for C++, Réutilisation des objets de style, Gestion des styles, Efficacité du code, Styles réutilisables, Développement d’applications, Référence API, Exemple de code, Téléchargement, Support.
type: docs
weight: 3000
url: /fr/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

La réutilisation d'objets de style peut économiser de la mémoire et rendre un programme plus rapide.

{{% /alert %}}

Pour appliquer une mise en forme à une grande plage de cellules dans une feuille de calcul :

1. Créer un objet de style.
1. Spécifier les attributs.
1. Appliquer le style aux cellules dans la plage.

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Parce que l'approche [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) utilise beaucoup moins de mémoire et est efficace, l'ancienne propriété Cell.Style, qui consommait beaucoup de mémoire inutile, a été supprimée avec la version Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
