---
title: Ottieni DrawObject e Bound durante il rendering in PDF con C++ usando la classe DrawObjectEventHandler
linktitle: Ottieni DrawObject e Bound durante il rendering in PDF
type: docs
weight: 70
url: /it/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Impara come usare la classe DrawObjectEventHandler in C++ per catturare DrawObject e Bound durante il rendering di file Excel in PDF o immagini.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce una classe astratta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) che ha un metodo [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/). L'utente può implementare [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) e utilizzare il metodo [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) per ottenere il [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) e Bound mentre si renderizza Excel in PDF o immagine. Ecco una breve descrizione dei parametri del metodo [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) verrà inizializzato e restituito durante la resa

- x: Sinistra di [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: Alto di [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- larghezza: larghezza di [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- altezza: altezza di [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

Se stai rendendo un file Excel in PDF, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) con la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). Analogamente, se stai convertendo un file Excel in Immagine, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) con [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **Ottieni DrawObject e Bound durante il rendering in Pdf usando la classe DrawObjectEventHandler**

Si prega di consultare il seguente esempio di codice. Carica il file Excel di esempio [sample Excel](64716821.xlsx) e lo salva come [PDF di output](64716822.pdf). Durante il rendering in PDF, utilizza la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) e cattura i [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) e il limite dei celle e oggetti esistenti, ad esempio immagini ecc. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) è Cell, stampa il suo Bound e StringValue. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) è Image, stampa il suo Bound e il nome della Forma. Si prega di consultare l'output della console del codice di esempio riportato di seguito per ulteriori chiarimenti.

## **Codice di Esempio**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class ClsDrawObjectEventHandler : public DrawObjectEventHandler
{
public:
    void Draw(DrawObject& drawObject, float x, float y, float width, float height) override
    {
        std::cout << std::endl;

        if (drawObject.GetType() == DrawObjectEnum::Cell)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Cell Value]: " << drawObject.GetCell().GetStringValue().ToUtf8() << std::endl;
        }

        if (drawObject.GetType() == DrawObjectEnum::Image)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Shape Name]: " << drawObject.GetShape().GetName().ToUtf8() << std::endl;
        }

        std::cout << "----------------------" << std::endl;
    }
};

void Run()
{
    Workbook wb(u"sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");
    PdfSaveOptions opts;
    auto drawObjectEventHandler = std::make_shared<ClsDrawObjectEventHandler>();
    opts.SetDrawObjectEventHandler(drawObjectEventHandler.get());
    wb.Save(u"outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
