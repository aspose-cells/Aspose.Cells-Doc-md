---
title: Erfassen Sie DrawObject und Bound beim Rendern in PDF mit C++ unter Verwendung der DrawObjectEventHandler Klasse
linktitle: DrawObject und Bound beim Rendern in PDF erhalten
type: docs
weight: 70
url: /de/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Erfahren Sie, wie man die DrawObjectEventHandler Klasse in C++ verwendet, um DrawObject und Bound beim Rendern von Excel Dateien in PDF oder Bilder zu erfassen.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet eine abstrakte Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/), die eine Methode [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) hat. Der Benutzer kann [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) implementieren und die Methode [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) nutzen, um den [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) und Bound beim Rendern von Excel in PDF oder Bild zu erhalten. Hier ist eine kurze Beschreibung der Parameter der Methode [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) wird initialisiert und beim Rendern zurückgegeben

- x: Links von [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: Oben von [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- width: Breite von [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- height: Höhe von [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

Wenn Sie eine Excel-Datei in PDF umwandeln, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) mit [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) verwenden. Wenn Sie eine Excel-Datei in ein Bild konvertieren, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) mit [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) verwenden.

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF unter Verwendung der DrawObjectEventHandler-Klasse**

Siehe den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](64716821.xlsx) und speichert sie als [Ausgabepdf](64716822.pdf). Während der Konvertierung in PDF nutzt es die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) und erfasst [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) und Bound vorhandener Zellen und Objekte, z.B. Bilder. Wenn der [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) Typ Cell ist, gibt er Bound und StringValue aus. Wenn der [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) Typ Image ist, gibt er Bound und Shape-Name aus. Sehen Sie sich die Konsolenausgabe des Beispielcodes unten für weitere Hilfe an.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
