---
title: Définir un style WordArt prédéfini au texte de la forme avec C++
linktitle: Définir un style WordArt prédéfini au texte de la forme
type: docs
weight: 280
url: /fr/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Découvrez comment définir un style WordArt prédéfini au texte d une forme en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
 Vous pouvez définir un style WordArt prédéfini au texte de la forme en utilisant Aspose.Cells. Veuillez utiliser [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) ou [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) à cette fin.

## ** Définir un style WordArt prédéfini au texte de la forme**
 Le code suivant crée une zone de texte avec du texte, puis définit le style WordArt prédéfini de son texte en utilisant la méthode [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/). Voici à quoi ressemble le fichier Excel de sortie dans Microsoft Excel.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a textbox with some text
    TextBox textbox = worksheet.GetShapes().AddTextBox(0, 0, 0, 0, 100, 700);
    textbox.SetText(u"Aspose File Format APIs");
    textbox.GetFont().SetSize(44);

    // Sets preset WordArt style to the text of the shape.
    FontSetting fntSetting = textbox.GetRichFormattings()[0];
    fntSetting.SetWordArtStyle(PresetWordArtStyle::WordArtStyle3);

    // Save the workbook in xlsx format
    workbook.Save(u"..\\Data\\02_OutputDirectory\\outputSetPresetWordArtStyle.xlsx");

    std::cout << "Workbook saved successfully with preset WordArt style!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
