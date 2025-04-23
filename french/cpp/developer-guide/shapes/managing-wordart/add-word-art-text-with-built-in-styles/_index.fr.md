---
title: Ajouter un texte WordArt avec des styles intégrés avec C++
linktitle: Ajouter un texte WordArt avec des styles intégrés
type: docs
weight: 270
url: /fr/cpp/add-word-art-text-with-built-in-styles/
description: Découvrez comment ajouter un texte WordArt avec des styles intégrés en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
 Vous pouvez ajouter un texte WordArt avec des styles intégrés en utilisant Aspose.Cells. Veuillez utiliser la méthode [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) à cette fin.

## **Ajouter un texte Word Art avec des styles intégrés**
Le code d'échantillon suivant ajoute des textes Word Art avec différents styles intégrés. Veuillez vérifier le [fichier Excel de sortie](5115470.xlsx) généré avec ce code. Voici à quoi ressemble le [fichier Excel de sortie](5115470.xlsx) dans Microsoft Excel.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

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
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
