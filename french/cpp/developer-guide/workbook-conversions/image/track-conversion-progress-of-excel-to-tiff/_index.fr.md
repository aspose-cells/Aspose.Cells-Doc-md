---
title: Suivi de la progression de conversion d’Excel en TIFF avec C++
linktitle: Suivre la progression de la conversion d Excel en TIFF
type: docs
weight: 190
url: /fr/cpp/track-conversion-progress-of-excel-to-tiff/
description: Apprenez à suivre la progression de la conversion de fichiers Excel en TIFF en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant cette période, vous pouvez vouloir afficher la progression de la conversion du document au lieu d’un simple écran de chargement pour améliorer l’utilisabilité de votre application. Aspose.Cells supporte le suivi de la progression de la conversion du document en fournissant l’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). L’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) fournit les méthodes [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) et [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme démontré dans la classe personnalisée *TestPageSavingCallback*.

## **Suivre la progression de la conversion d'Excel en TIFF**

Le code suivant charge le fichier Excel [source](95584311.xlsx) et affiche la progression de sa conversion dans la console en utilisant la classe personnalisée *TestPageSavingCallback* qui implémente l’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). Le fichier de sortie généré est joint pour votre référence.

[Output File](95584312.tiff)

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestTiffPageSavingCallback : public IPageSavingCallback {
public:
    void PageStartSaving(PageStartSavingArgs& args) override {
        // Implement page start saving logic here
    }

    void PageEndSaving(PageEndSavingArgs& args) override {
        // Implement page end saving logic here
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    ImageOrPrintOptions opts;
    opts.SetPageSavingCallback(new TestTiffPageSavingCallback());
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Tiff);

    WorkbookRender wr(workbook, opts);
    wr.ToImage(outDir + u"DocumentConversionProgressForTiff_out.tiff");

    std::cout << "Document converted to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Ce qui suit est le code de la classe personnalisée *TestTiffPageSavingCallback*.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestTiffPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages before page index 2.
        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages after page index 8.
        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **Sortie console**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
