---
title: Travailler avec l effet de glow d une forme ou d un graphique avec C++
linktitle: Travailler avec l effet de lueur de la forme ou du graphique
type: docs
weight: 240
url: /fr/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Découvrez comment travailler avec l effet de glow des formes ou des graphiques en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
 Aspose.Cells fournit la propriété [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) ainsi que la classe [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) pour travailler avec l'effet de glow d'une forme ou d'un graphique. La classe [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) contient les propriétés suivantes qui peuvent être définies pour atteindre différents résultats selon les exigences de l'application.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Travailler avec l'effet de lueur de la forme ou du graphique**
Le code suivant charge le [fichier Excel source](5115407.xlsx) et accède à la première shape dans la première feuille de calcul, puis définit les sous-propriétés de la propriété [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) avant d'enregistrer le classeur dans le [fichier Excel de sortie](5115414.xlsx).

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

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
