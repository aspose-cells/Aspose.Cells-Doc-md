---
title: Envoyer une forme en avant ou en arrière dans la feuille de calcul avec C++
linktitle: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 3400
url: /fr/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Apprenez comment changer la position z order des formes dans une feuille de calcul en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsque plusieurs formes sont présentes au même endroit, leur visibilité est déterminée par leur position dans l'ordre z. Aspose.Cells fournit la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/), qui modifie la position z de la forme. Si vous souhaitez envoyer une forme en arrière-plan, utilisez un nombre négatif comme -1, -2, -3, etc. Si vous souhaitez amener une forme en avant-plan, utilisez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code d'exemple suivant montre comment utiliser la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/). Veuillez voir le [fichier Excel d'exemple](50528330.xlsx) utilisé dans le code et le [fichier Excel en sortie](50528331.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple lors de l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

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

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
