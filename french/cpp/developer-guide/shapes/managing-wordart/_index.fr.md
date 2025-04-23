---
title: Ajouter un filigrane WordArt à la feuille de calcul avec C++
linktitle: Gestion de WordArt
type: docs
weight: 180
url: /fr/cpp/add-wordart-watermark-to-worksheet/
description: Apprenez comment ajouter des filigranes WordArt aux feuilles de calcul Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Utilisez WordArt pour ajouter des effets de texte spéciaux aux feuilles de calcul. Par exemple, étirez un titre sur le dessus du fichier, décorez du texte et faites en sorte que le texte s'adapte à une forme prédéfinie, ou appliquez du texte à une feuille Excel en tant que filigrane en arrière-plan. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans les feuilles de calcul pour ajouter une décoration.

{{% /alert %}} 

L'exemple suivant montre comment ajouter une forme WordArt pour définir un filigrane en arrière-plan pour une feuille de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajouter un texte Word Art avec des styles intégrés](/cells/fr/cpp/add-word-art-text-with-built-in-styles/)
- [Verrouillage du filigrane WordArt](/cells/fr/cpp/locking-wordart-watermark/)
- [Définir un style de WordArt prédéfini pour le texte de la forme](/cells/fr/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
