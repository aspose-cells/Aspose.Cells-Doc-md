---
title: Copier des formes entre feuilles de calcul avec C++
linktitle: Copier les formes
type: docs
weight: 200
url: /fr/cpp/copy-shapes-between-worksheets/
description: Apprenez comment copier des formes, graphiques et autres objets de dessin entre feuilles avec Aspose.Cells en C++.
---

{{% alert color="primary" %}}

Parfois, vous devez copier des éléments d'une feuille, par exemple des images, graphiques et autres objets de dessin, entre feuilles. Aspose.Cells prend en charge cette fonctionnalité. Les graphiques, images et autres objets peuvent être copiés avec la plus grande précision.

Cet article vous donne une compréhension détaillée de comment copier des formes entre les feuilles de calcul.

{{% /alert %}}

## **Copier une image d'une feuille de calcul à une autre**

Pour copier une image d'une feuille de calcul à une autre, utilisez la méthode [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) comme indiqué dans le code exemple ci-dessous.

```cpp
#include <iostream>
#include <memory>
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
    U16String outputFilePath = outDir + u"PictureCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Picture from the "Picture" worksheet
    Worksheet pictureSheet = workbook.GetWorksheets().Get(u"Picture");
    Picture picturesource = pictureSheet.GetPictures().Get(0);

    // Get picture data
    Vector<uint8_t> pictureData = picturesource.GetData();

    // Copy the picture to the Result Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetPictures().Add(picturesource.GetUpperLeftRow(), picturesource.GetUpperLeftColumn(), pictureData, picturesource.GetWidthScale(), picturesource.GetHeightScale());

    // Save the Worksheet
    workbook.Save(outputFilePath);

    std::cout << "Picture copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Copier un graphique d'une feuille de calcul à une autre**

Le code suivant démontre l'utilisation de la méthode [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) pour copier un graphique d'une feuille de calcul à une autre.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
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
    U16String outputFilePath = outDir + u"ChartCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Chart from the "Chart" worksheet
    Worksheet chartSheet = workbook.GetWorksheets().Get(u"Chart");
    Chart chartSource = chartSheet.GetCharts().Get(0);

    // Get the ChartShape object
    ChartShape cshape = chartSource.GetChartObject();

    // Copy the Chart to the "Result" Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(cshape, 20, 0, 2, 0);

    // Save the Workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Copier les contrôles et autres objets de dessin d'une feuille de calcul à une autre**

Pour copier les contrôles et autres objets de dessin, utilisez la méthode [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) comme indiqué dans l'exemple ci-dessous.

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
    U16String inputFilePath = srcDir + u"sample2.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ControlsCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Shapes from the "Control" worksheet
    Worksheet controlSheet = workbook.GetWorksheets().Get(u"Control");
    ShapeCollection shapes = controlSheet.GetShapes();

    // Copy the Textbox to the Result Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(shapes.Get(0), 5, 0, 2, 0);

    // Copy the Oval Shape to the Result Worksheet
    resultSheet.GetShapes().AddCopy(shapes.Get(1), 10, 0, 2, 0);

    // Save the Worksheet
    workbook.Save(outputFilePath);

    std::cout << "Shapes copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
