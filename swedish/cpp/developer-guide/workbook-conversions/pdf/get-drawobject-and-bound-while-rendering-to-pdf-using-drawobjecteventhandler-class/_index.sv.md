---
title: Hämta DrawObject och Bound vid rendering till PDF med C++ med DrawObjectEventHandler klass
linktitle: Hämta DrawObject och Bound vid rendering till PDF
type: docs
weight: 70
url: /sv/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Lär dig hur man använder DrawObjectEventHandler klassen i C++ för att fånga DrawObject och Bound vid rendering av Excel filer till PDF eller bilder.
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en abstrakt klass [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) som har en [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/)-metod. Användaren kan implementera [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) och använda [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/)-metoden för att få [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) och Bound vid rendering av Excel till PDF eller bild. Här är en kort beskrivning av parametrarna till metoden [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) kommer att initialiseras och returneras vid rendering

- x: Vänster om [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: Topp om [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- bredd: Bredd av [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- höjd: Höjd av [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

Om du renderar en Excel-fil till PDF kan du använda [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)-klass med [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). På samma sätt, om du renderar en Excel-fil till bild, kan du använda [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)-klass med [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **Få DrawObject och Bound medan du renderar till Pdf med hjälp av DrawObjectEventHandler-klassen**

Se följande exempel. Det laddar [exempel-Excelfilen](64716821.xlsx) och sparar den som [utdata-PDF](64716822.pdf). Vid rendering till PDF använder det egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) och fångar [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) och Bound för befintliga celler och objekt, t.ex. bilder. Om typen [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) är Cell, skriver den ut dess Bound och StringValue. Och om typen [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) är Image, skriver den ut dess Bound och Shape-namn. Se konsolutmatningen av exempelkoden nedan för mer hjälp.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
