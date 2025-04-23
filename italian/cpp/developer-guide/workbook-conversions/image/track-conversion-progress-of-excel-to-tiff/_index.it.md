---
title: Monitora lo stato di avanzamento della conversione di Excel in TIFF con C++
linktitle: Monitora il progresso della conversione di Excel in TIFF
type: docs
weight: 190
url: /it/cpp/track-conversion-progress-of-excel-to-tiff/
description: Impara come monitorare lo stato di avanzamento della conversione di file Excel in formato TIFF usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

 A volte, convertire grandi file Excel può richiedere del tempo. Durante questo periodo, potresti voler mostrare lo stato di avanzamento della conversione del documento invece di una semplice schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il monitoraggio dello stato di avanzamento della conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) fornisce i metodi [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) e [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestPageSavingCallback*.

## **Monitora il progresso della conversione di Excel in TIFF**

 Il seguente esempio di codice carica il file Excel di origine e stampa lo stato di avanzamento della conversione nel console utilizzando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). Il file di output generato è allegato per riferimento.

[Output File](95584312.tiff)

## **Codice di Esempio**

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

Di seguito è riportato il codice per la classe personalizzata *TestTiffPageSavingCallback*.

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

## **Output della console**

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
