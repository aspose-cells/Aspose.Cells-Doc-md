---
title: Suivi de la progression de conversion du document avec C++
linktitle: Suivre l avancement de la conversion du document
type: docs
weight: 970
url: /fr/cpp/track-document-conversion-progress/
description: Apprenez comment suivre la progression de la conversion du document en C++ en utilisant Aspose.Cells pour améliorer la convivialité de l application.
---

## **Scénarios d'utilisation possibles**

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant ce temps, vous pouvez vouloir afficher la progression de la conversion du document au lieu d'un simple écran de chargement pour améliorer l'utilisabilité de votre application. Aspose.Cells supporte le suivi de la progression de la conversion du document en fournissant l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). L'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) fournit [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) et [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) méthodes que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme démontré dans la classe personnalisée `TestPageSavingCallback`.

## **Suivre la progression de la conversion des documents**

Le code suivant charge le fichier Excel [source](94896151.xlsx) et affiche la progression de sa conversion dans la console en utilisant la classe personnalisée `TestPageSavingCallback` qui implémente l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/).

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " is starting to save." << std::endl;
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " has been saved." << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"PagesBook1.xlsx";
    U16String outputFilePath = outDir + u"DocumentConversionProgress.pdf";

    Workbook workbook(inputFilePath);
    PdfSaveOptions pdfSaveOptions;

    TestPageSavingCallback callback;
    pdfSaveOptions.SetPageSavingCallback(&callback);

    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Document conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Voici le code pour la classe personnalisée `TestPageSavingCallback`.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **Sortie console**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
