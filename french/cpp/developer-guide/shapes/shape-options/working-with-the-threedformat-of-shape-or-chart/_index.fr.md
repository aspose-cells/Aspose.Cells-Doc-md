---
title: Travailler avec le ThreeDFormat de Shape ou Chart avec C++
linktitle: Travailler avec le ThreeDFormat de la forme ou du graphique
type: docs
weight: 250
url: /fr/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Apprenez comment manipuler le format 3D des formes ou des graphiques en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) ainsi que la classe [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) pour travailler avec le format 3D des formes ou des graphiques. La classe [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) contient différentes propriétés qui peuvent être définies pour obtenir différents résultats selon les besoins de l'application.

## **Travailler avec le ThreeDFormat de la forme ou du graphique**
Le code d'exemple suivant charge le [fichier Excel source](5115419.xlsx) et accède à la première forme de la première feuille de calcul. Il définit ensuite les sous-propriétés de la propriété [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) puis enregistre le classeur dans le [fichier Excel de sortie](5115410.xlsx).

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

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
