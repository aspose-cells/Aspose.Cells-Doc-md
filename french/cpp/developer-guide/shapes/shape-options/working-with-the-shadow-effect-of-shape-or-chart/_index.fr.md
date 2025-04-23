---
title: Travailler avec l effet d ombre d une forme ou d un graphique avec C++
linktitle: Travailler avec l effet d ombre de la forme ou du graphique
type: docs
weight: 220
url: /fr/cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Découvrez comment manipuler l effet d ombre des formes ou des graphiques en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la méthode [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) ainsi que la classe [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) pour travailler avec l'effet d'ombre des formes ou des graphiques. La classe [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) contient les propriétés suivantes qui peuvent être définies pour obtenir différents résultats selon les besoins de l'application.

- [GetAngle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [GetBlur()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [GetColor()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [GetDistance()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [GetPresetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [GetSize()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [GetTransparency()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **Travailler avec l'effet d'ombre de la forme ou du graphique**
Le code d'exemple suivant charge le [fichier Excel source](5115425.xlsx) et accède à la première forme de la première feuille de calcul, puis modifie les sous-propriétés de la propriété [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) avant d'enregistrer le classeur dans le [fichier Excel de sortie](5115411.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
