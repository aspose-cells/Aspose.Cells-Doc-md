---
title: Rendre une feuille de calcul dans un contexte graphique avec C++
linktitle: Rendre la feuille de calcul dans le contexte graphique
type: docs
weight: 300
url: /fr/cpp/render-worksheet-to-graphic-context/
description: Apprenez comment rendre une feuille de calcul dans un contexte graphique en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells peut désormais rendre une feuille de calcul dans un contexte graphique. Le contexte graphique peut être n'importe quoi comme un fichier image, un écran, ou une imprimante, etc. Veuillez utiliser l'une des deux méthodes suivantes pour rendre une feuille de calcul dans un contexte graphique.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

Le code suivant illustre comment utiliser Aspose.Cells pour rendre une feuille de calcul dans un contexte graphique. Une fois le code exécuté, il imprimera la feuille entière et remplira l'espace vide restant avec une couleur bleue dans le contexte graphique, puis enregistrera l'image sous le nom de **OutputImage_out_.png**. Vous pouvez utiliser n'importe quel fichier Excel source pour tester ce code. Veuillez également lire les commentaires à l'intérieur du code pour une meilleure compréhension.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
