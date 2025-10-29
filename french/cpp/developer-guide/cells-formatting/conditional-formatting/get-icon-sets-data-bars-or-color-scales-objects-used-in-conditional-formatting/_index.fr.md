---
title: Obtenir les objets Jeux d’icônes, Barres de données ou Échelles de couleurs utilisés dans le formatage conditionnel avec C++
linktitle: Obtenir les ensembles d icônes, les barres de données ou les objets de palettes de couleurs
description: Aspose.Cells for C++ est une bibliothèque pour travailler avec les fichiers de tableur. Elle supporte l utilisation d ensembles d icônes, de barres de données et de palettes de couleurs dans la mise en forme conditionnelle pour afficher les données des tableurs. Cet article décrit comment utiliser la bibliothèque Aspose.Cells pour récupérer des données pour ces objets.
keywords: Aspose.Cells, Mise en forme conditionnelle, Ensemble d icônes, Barre de données, Échelle de couleurs, Feuille de calcul
type: docs
weight: 10
url: /fr/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

Parfois, vous avez besoin de récupérer les ensembles d'icônes utilisés dans la mise en forme conditionnelle d'une cellule ou d'une plage de cellules et vous souhaitez créer un fichier image basé sur cela. Vous pourriez avoir besoin de lire les barres de données ou les échelles de couleurs utilisées dans la mise en forme conditionnelle. Aspose.Cells for C++ prend en charge cette fonctionnalité.

{{% /alert %}} 

L'exemple de code suivant montre comment lire les ensembles d'icônes utilisés pour la mise en forme conditionnelle. Avec l'API simple d'Aspose.Cells, les données d'image de l'ensemble d'icônes sont enregistrées en tant qu'image.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
