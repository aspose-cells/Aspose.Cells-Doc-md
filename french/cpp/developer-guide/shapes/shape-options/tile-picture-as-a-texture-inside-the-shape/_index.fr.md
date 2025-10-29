---
title: Tuiler une image comme texture à l intérieur de la forme avec C++
linktitle: Image tuilée comme une texture à l intérieur de la forme
type: docs
weight: 1700
url: /fr/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Découvrez comment tuiler une image en tant que texture à l intérieur d une forme en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsque l'image est petite et ne couvre pas toute la surface de la forme sans perdre en qualité, alors vous avez la possibilité de la tuiler. Le tuilage remplit la surface de la forme avec une petite image en les répétant comme s'ils étaient des carreaux.

## **Image tuilée comme une texture à l'intérieur de la forme**

Vous pouvez remplir la surface de la forme avec une certaine image et la tuiler en utilisant la propriété [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) et en la définissant sur **true**. Veuillez consulter le code d'exemple suivant, son [fichier Excel exemple](46465050.xlsx) ainsi que la capture d'écran pour référence.

## **Capture d'écran**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Code d'exemple**

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
