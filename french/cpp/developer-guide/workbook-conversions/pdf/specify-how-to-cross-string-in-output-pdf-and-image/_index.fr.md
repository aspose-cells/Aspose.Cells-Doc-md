---
title: Spécifier comment faire traverser les chaînes dans le PDF et l image de sortie avec C++
linktitle: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image
type: docs
weight: 120
url: /fr/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Apprenez comment contrôler le débordement du texte dans les sorties PDF et image en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne plus longue que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lors de la sauvegarde de votre fichier Excel en PDF ou Image, vous pouvez contrôler ce débordement en spécifiant le type de traversée à l'aide de l'énumération [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). Il possède les valeurs suivantes :

- **TextCrossType.Default** : Affiche le texte comme MS Excel, en dépendant de la cellule suivante. Si la cellule suivante est nulle, la chaîne traversera ou sera tronquée.

- **TextCrossType.CrossKeep** : Affiche la chaîne comme l'exportation PDF/Image de MS Excel.

- **TextCrossType.CrossOverride** : Affiche tout le texte en croisant d'autres cellules et en écrasant le texte des cellules croisées.

- **TextCrossType.StrictInCell**: Affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser une chaîne dans le PDF de sortie/une image en utilisant TextCrossType**

Le code d'exemple suivant charge le fichier Excel d'exemple et le sauvegarde au format PDF/Image en spécifiant différents [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés depuis les liens suivants :

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Code d'exemple

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
