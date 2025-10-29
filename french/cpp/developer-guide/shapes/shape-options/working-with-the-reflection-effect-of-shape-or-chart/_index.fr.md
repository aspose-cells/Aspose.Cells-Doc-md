---
title: Travailler avec l effet de réflexion d une forme ou d un graphique avec C++
linktitle: Travailler avec l effet de réflexion de la forme ou du graphique
type: docs
weight: 210
url: /fr/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Découvrez comment travailler avec l effet de réflexion des formes ou des graphiques en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**
 Aspose.Cells fournit la propriété [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) ainsi que la classe [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) pour travailler avec l'effet de réflexion d'une forme ou d'un graphique. La classe [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) contient les propriétés suivantes qui peuvent être définies pour atteindre différents résultats selon les exigences de l'application.

- [Flou](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [Direction](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [Distance](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [DirectionDeFondu](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [RotationAvecForme](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [Taille](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [Transparence](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [Type](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **Travailler avec l'effet de réflexion de la forme ou du graphique**
 Le code suivant charge le [fichier Excel source](5115424.xlsx) et accède à la première forme dans la feuille de travail par défaut, puis définit différentes propriétés de la classe [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) avant d'enregistrer le classeur dans le [fichier Excel de sortie](5115423.xlsx).

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

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
