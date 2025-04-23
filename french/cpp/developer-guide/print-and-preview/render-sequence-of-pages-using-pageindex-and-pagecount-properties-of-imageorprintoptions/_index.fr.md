---
title: Rendu d une séquence de pages en utilisant les propriétés PageIndex et PageCount des ImageOrPrintOptions avec C++
linktitle: Rendu d une séquence de pages
type: docs
weight: 110
url: /fr/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: Rendre une séquence de pages d un fichier Excel en images en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez rendre une séquence de pages de votre fichier Excel en images en utilisant Aspose.Cells avec les propriétés [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) et [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/). Ces propriétés sont utiles lorsqu'il y a un grand nombre, par exemple des milliers de pages dans votre feuille de calcul, mais que vous ne voulez en rendre que certaines. Cela permet non seulement d'économiser du temps de traitement, mais aussi de réduire la consommation de mémoire du processus de rendu.

## **Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541781.xlsx) et ne rend que les pages 4, 5, 6 et 7 en utilisant les propriétés [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) et [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/). Voici les pages rendues générées par le code.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Code d'exemple**

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleImageOrPrintOptions_PageIndexPageCount.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetPageIndex(3);
    opts.SetPageCount(4);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(ws, opts);

    for (int i = opts.GetPageIndex(); i < sr.GetPageCount(); i++)
    {
        std::wstring pageNum = std::to_wstring(i + 1);
        U16String filePath = outDir + U16String(u"outputImage-") + 
            U16String(reinterpret_cast<const char16_t*>(pageNum.c_str())) + 
            U16String(u".png");
        sr.ToImage(i, filePath);
    }

    std::cout << "Images generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
