---
title: Verrouiller le filigrane WordArt avec C++
linktitle: Verrouiller le filigrane WordArt
type: docs
weight: 170
url: /fr/cpp/locking-wordart-watermark/
description: Découvrez comment verrouiller les filigranes WordArt dans les feuilles de calcul Excel en utilisant Aspose.Cells for C++. Empêchez la modification, le déplacement et la sélection des filigranes de manière programmatique.
---

{{% alert color="primary" %}}

 Les API Aspose.Cells permettent d'ajouter des filigranes WordArt sur la feuille de calcul de manière à ce que le WordArt devienne un objet que vous pouvez déplacer et positionner sur la feuille. Il est également possible de verrouiller l'objet WordArt pour toute interaction comme la modification, le déplacement et la sélection. Cet article explique l'utilisation de la méthode [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) pour verrouiller certains aspects du filigrane.

{{% /alert %}}

 Les API Aspose.Cells permettent de verrouiller certains aspects du filigrane afin que l'interaction de l'utilisateur puisse être limitée ou complètement bloquée. Le code suivant démontre l'utilisation de l'API Aspose.Cells for C++ pour verrouiller la sélection, le déplacement, la modification et le redimensionnement du filigrane en créant une feuille de calcul à partir de zéro.

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

    // Lock Shape Aspects
    wordart.SetIsLocked(true);
    wordart.SetLockedProperty(ShapeLockType::Selection, true);
    wordart.SetLockedProperty(ShapeLockType::ShapeType, true);
    wordart.SetLockedProperty(ShapeLockType::Move, true);
    wordart.SetLockedProperty(ShapeLockType::Resize, true);
    wordart.SetLockedProperty(ShapeLockType::Text, true);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the color
    wordArtFormat.SetOneColorGradient(Color::Red(), 0.2, GradientStyleType::Horizontal, 2);

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    wordart.SetHasLine(false);

    // Save the file
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
