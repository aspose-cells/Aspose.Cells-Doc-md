---
title: Générer des images de barres de données de formatage conditionnel avec C++
linktitle: Générer des images de mise en forme conditionnelle DataBars
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuilles de calcul. Elle supporte la génération de barres de données et d’images avec un formatage conditionnel, permettant aux utilisateurs de personnaliser l’affichage du classeur en fonction de la valeur des cellules. Cet article introduira comment utiliser la bibliothèque Aspose.Cells pour générer des barres de données et des images avec un formatage conditionnel.
keywords: Aspose.Cells, Mise en forme conditionnelle, Barres de données, Images, Feuilles de calcul
type: docs
weight: 40
url: /fr/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de barres de données de formatage conditionnel. Vous pouvez utiliser la méthode Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) pour générer ces images. Cet article montre comment générer une image de barre de données à l'aide d'Aspose.Cells.

{{% /alert %}}

Le code exemple suivant génère l’image de la barre de données de la cellule C1. Il accède d’abord à l’objet de condition de mise en forme de la cellule, puis depuis cet objet, il accède à l’objet [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) et utilise sa méthode [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) pour générer l’image de la cellule. Enfin, il enregistre l’image sur le disque.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
