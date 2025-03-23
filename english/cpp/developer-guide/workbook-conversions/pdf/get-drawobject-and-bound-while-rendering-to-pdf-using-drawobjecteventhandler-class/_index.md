---
title: Get DrawObject and Bound while rendering to PDF with C++ using DrawObjectEventHandler class
linktitle: Get DrawObject and Bound while rendering to PDF
type: docs
weight: 70
url: /cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Learn how to use the DrawObjectEventHandler class in C++ to capture DrawObject and Bound while rendering Excel files to PDF or images.
---

## **Possible Usage Scenarios**

Aspose.Cells provides an abstract class [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) which has a [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) method. The user can implement [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) and utilize the [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) method to get the [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) and Bound while rendering Excel to PDF or Image. Here is a brief description of the parameters of the [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) method.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) will be initialized and returned when rendering

- x: Left of [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: Top of [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- width: Width of [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- height: Height of [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

If you are rendering an Excel file to PDF, then you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) class with [**PdfSaveOptions.GetDrawObjectEventHandler()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/.paginatedsaveoptions/getdrawobjecteventhandler/). Similarly, if you are rendering an Excel file to Image, you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) class with [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **Get DrawObject and Bound while rendering to Pdf using DrawObjectEventHandler class**

Please see the following sample code. It loads the [sample Excel file](64716821.xlsx) and saves it as [output PDF](64716822.pdf). While rendering to PDF, it utilizes [**PdfSaveOptions.GetDrawObjectEventHandler()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/.paginatedsaveoptions/getdrawobjecteventhandler/) property and captures the [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) and Bound of existing cells and objects e.g. images etc. If the [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) type is Cell, it prints its Bound and StringValue. And if the [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) type is Image, it prints its Bound and Shape Name. Please see the console output of the sample code given below for more help.

## **Sample Code**

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

## **Console Output**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}